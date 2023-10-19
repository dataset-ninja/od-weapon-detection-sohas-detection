import supervisely as sly
import os
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, get_file_name_with_ext
import xml.etree.ElementTree as ET

from tqdm import tqdm

def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:        
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path
    
def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    ds_path = os.path.join("OD-WeaponDetection-master","Weapons and similar handled objects","Sohas_weapon-Detection")
    test_dir_img = os.path.join(ds_path,"images_test")
    test_dir_ann = os.path.join(ds_path,"annotations_test","xmls")

    train_dir_img = os.path.join(ds_path,"images")
    train_dir_ann = os.path.join(ds_path,"annotations","xmls")

    errors = []

    batch_size = 30

    images_ext = ".jpg"
    anns_ext = ".xml"

    def create_ann(image_path):
        labels = []

        image_name = get_file_name(image_path)
        if ds_name == 'test':
            anns_path = test_dir_ann
        elif ds_name == 'train':
            anns_path = train_dir_ann
        ann_path = os.path.join(anns_path, image_name + anns_ext)

        tree = ET.parse(ann_path)
        root = tree.getroot()
        img_height = int(root.find(".//height").text)
        img_wight = int(root.find(".//width").text)
        objects_content = root.findall(".//object")
        for obj_data in objects_content:
            name = obj_data.find(".//name").text
            obj_class = meta.get_obj_class(name)
            bndbox = obj_data.find(".//bndbox")
            top = int(bndbox.find(".//ymin").text)
            left = int(bndbox.find(".//xmin").text)
            bottom = int(bndbox.find(".//ymax").text)
            right = int(bndbox.find(".//xmax").text)

            rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
            label = sly.Label(rectangle, obj_class)
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    classes = ['pistol', 'smartphone', 'knife', 'monedero', 'billete', 'tarjeta']
    obj_classes = [sly.ObjClass(name, sly.Rectangle) for name in classes]


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes)
    api.project.update_meta(project.id, meta.to_json())

    project_dict = {'test':test_dir_img, 'train':train_dir_img}

    for ds_name in project_dict:
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
        image_pathes = [os.path.join(project_dict[ds_name], img) for img in os.listdir(project_dict[ds_name])]

        progress = sly.Progress("Create dataset {}".format(ds_name), len(image_pathes))

        for img_pathes_batch in sly.batched(image_pathes, batch_size=batch_size):
            img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project
