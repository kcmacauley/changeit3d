# ShapeShifters UW-Madison CS766 Class Project

## Project Website
Please visit our [project website](https://roettges.github.io/shapeshifter_CS766/) for more information about the project and the experiments conducted. 

## Overview
This is repo is a part of the ShapeShifters UW-Madison CS766 Class Project.
This repo contains forked code from the original [changeit3d repo](https://github.com/optas/changeit3d) in addition to code developed specifically for this project. 
Also checkout our [main repository](https://github.com/Auc7us/shapeshifters) that contains all the training, visualisations, and evaluation scripts for our experiments "Strength of Changeit3D to Gaussian Noise on Point Clouds" and "Robustness of ChangeIt3D to varying language instructions"  
This repos contains important modules required to run the scripts on our main repo; please clone them into the same parent directory.

## Installation
Please flow the installation of the original and install the **Chamfer Loss Submodule** [changeit3d repo](https://github.com/optas/changeit3d?tab=readme-ov-file#installation).

**Note:** in order to use the python scripts used in generating the custom vase dataset you will need to install [open3d](https://www.open3d.org/).

Also, install the [pretrained weights](https://github.com/optas/changeit3d?tab=readme-ov-file#pretained-weights-and-networks).

**Note:** you may need to download the entire [dataset](https://github.com/optas/changeit3d?tab=readme-ov-file#shapetalk-dataset--rocket-).

## Run An Example

First you need to install the following dataset folders into `changeit3d/data/seg_shapetalk/point_clouds/`:
 
 - [chair](https://drive.google.com/drive/folders/1CN_2YQcfustc_GMiwDXLRZeKf5D1kMJO?usp=drive_link)
 - [lamp](https://drive.google.com/drive/folders/1BoL0QChCe9chLj4ItfwqV3oE0c3Slr1M?usp=drive_link)
 - [segmented_chair](https://drive.google.com/drive/folders/1qgYMANYQUzQ9sU1uhx0oJ-wxLORY4IUG?usp=drive_link) 
 - [segmented_lamp](https://drive.google.com/drive/folders/13VuJuqg5PNDtGvZg6rIfApH9EAVZ3n2s?usp=drive_link)


In order to reproduce results from the Part Removal experiment please run: 

[looking_inside_c3d_trained_system_seg.ipynb](https://github.com/kcmacauley/changeit3d/blob/main/changeit3d/notebooks/change_it_nets/looking_inside_c3d_trained_system_seg.ipynb)

To compare with the monolithic network results please run: 

[looking_inside_monolithic_trained_system_seg.ipynb](https://github.com/kcmacauley/changeit3d/blob/main/changeit3d/notebooks/change_it_nets/looking_inside_monolithic_trained_system_seg.ipynb)

