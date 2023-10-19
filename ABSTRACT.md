Authors introduce **OD-WeaponDetection: Knife Detection** dataset, a collection of 2078 images designed for object detection, specifically focused on the presence of at least one *knife*. These images were sourced from the internet, including frames extracted from YouTube videos and surveillance footage. The dataset encompasses a wide variety of cold steel weapons, differing in types, shapes, colors, sizes, and materials. It accounts for knives positioned at various distances from the camera, some partially occluded by hands, and objects that mimic the handling of knives. The dataset offers a diverse range of indoor and outdoor scenarios, and additional details about this image dataset and experiment results can be found in the related publication. The OD-WeaponDetection: Knife Detection dataset is a part of **Weapon Detection Open Data**.

## More about Weapon Detection Open Data

The weapon datasets available here are specifically tailored for the development of intelligent video surveillance automatic systems.

An automatic weapon detection system can provide the early detection of potentially violent situations that is of paramount importance for citizens security. One way to prevent these situations is by detecting the presence of dangerous objects such as handguns and knives in surveillance videos. Deep Learning techniques based on Convolutional Neural Networks can be trained to detect this type of object.

The weapon detection task can be performed by different approaches of combining a region proposal technique with a classifier, or integrating both into one model. However, any deep learning model requires to learn a quality image dataset and an annotation according to the classification or detection tasks.

Weapon detection Open Data provides quality image datasets built for training Deep Learning models under the development of an automatic weapon detection system. Weapons datasets for image classification and object detection tasks are described and can be downloaded below. The public datasets are organized depending on the included objects in the dataset images and the target task. 

## Weapon Detection Open Data structure

### Classification

The datasets included in this section have been designed for the classification task based on CNN deep learning models. After the training stage on these datasets, the classification models must distinguish between weapons and different common objects present in the background or handled similarly.

- OD-WeaponDetection: Knife Classification (10 039 images, 100 classes) ([(available on DatasetNinja)]())
- OD-WeaponDetection: Pistol Classification (9 857 images, 102 classes) ([(available on DatasetNinja)]())
- - OD-WeaponDetection: Sohas Classification (9 544 images, 6 classes) ([(available on DatasetNinja)]())

### Detection

The datasets included in this section have been designed for the object detection task based on Deep Learning architectures with a CNN backbone. The selected images contain weapons and objects but also consider an enriched context of different background objects as well as the way objects are handled. After the training stage on these datasets, the detection models must locate and distinguish between weapons and different common objects present in the background or handled similarly.

- OD-WeaponDetection: Knife Detection (2 078 images, 1 class) ([(available on DatasetNinja)]())
- OD-WeaponDetection: Pistol Detection (3 000 images, 1 class) ([(available on DatasetNinja)]())
- - OD-WeaponDetection: Sohas Detection (5 859 images, 6 classes) ([(available on DatasetNinja)]())
