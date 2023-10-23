Authors introduce **OD-WeaponDetection: Sohos Detection** dataset, featuring a corpus of 5859 images meticulously labeled with 6446 objects spanning six distinct classes, which include *knives*, *pistols*, *smartphones*, as well as *wallet*, *banknote*, and *credit_card* categories. This dataset is strategically divided into two key segments: a *train* split comprising 5002 images and a *test* split with 857 images. Just as in the example dataset, the authors present this resource as a pivotal contribution to the field of object detection, particularly focusing on weapons and objects of interest within images. The dataset's rich content is sourced from a myriad of internet-based sources, including frames extracted from YouTube videos and surveillance footage, ensuring it encapsulates real-world challenges. It boasts the inclusion of various knives, mirroring the diverse types, shapes, colors, sizes, and materials that such weapons can embody. Additionally, the dataset addresses complex scenarios where knives are partially obscured by hands and objects simulating their handling, enhancing its practicality. With a diverse array of indoor and outdoor settings, the dataset equips researchers, security professionals, and developers with a versatile resource for advancing object detection models. Detailed information and experimental results are available in a related publication, making the OD-WeaponDetection: Sohos Detection dataset an essential component of the broader Weapon Detection Open Data initiative.

## More about Weapon Detection Open Data

The weapon datasets available here are specifically tailored for the development of intelligent video surveillance automatic systems.

An automatic weapon detection system can provide the early detection of potentially violent situations that is of paramount importance for citizens security. One way to prevent these situations is by detecting the presence of dangerous objects such as handguns and knives in surveillance videos. Deep Learning techniques based on Convolutional Neural Networks can be trained to detect this type of object.

The weapon detection task can be performed by different approaches of combining a region proposal technique with a classifier, or integrating both into one model. However, any deep learning model requires to learn a quality image dataset and an annotation according to the classification or detection tasks.

Weapon detection Open Data provides quality image datasets built for training Deep Learning models under the development of an automatic weapon detection system. Weapons datasets for image classification and object detection tasks are described and can be downloaded below. The public datasets are organized depending on the included objects in the dataset images and the target task. 

## Weapon Detection Open Data structure

## Classification

The datasets included in this section have been designed for the classification task based on CNN deep learning models. After the training stage on these datasets, the classification models must distinguish between weapons and different common objects present in the background or handled similarly.

- OD-WeaponDetection: Knife Classification (10 039 images, 100 classes) [(available on DatasetNinja)](https://datasetninja.com/od-weapon-detection-knife-classification)
- OD-WeaponDetection: Pistol Classification (9 857 images, 102 classes) [(available on DatasetNinja)](https://datasetninja.com/od-weapon-detection-pistol-classification)
- OD-WeaponDetection: Sohas Classification (9 544 images, 6 classes) [(available on DatasetNinja)](https://datasetninja.com/od-weapon-detection-sohas-classification)

## Detection

The datasets included in this section have been designed for the object detection task based on Deep Learning architectures with a CNN backbone. The selected images contain weapons and objects but also consider an enriched context of different background objects as well as the way objects are handled. After the training stage on these datasets, the detection models must locate and distinguish between weapons and different common objects present in the background or handled similarly.

- OD-WeaponDetection: Knife Detection (2 078 images, 1 class) [(available on DatasetNinja)](https://datasetninja.com/od-weapon-detection-knife-detection)
- OD-WeaponDetection: Pistol Detection (3 000 images, 1 class) [(available on DatasetNinja)](https://datasetninja.com/od-weapon-detection-pistol-detection)
- OD-WeaponDetection: Sohas Detection (5 859 images, 6 classes) (current)