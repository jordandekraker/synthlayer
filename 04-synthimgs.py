# gen-synthimgs
# must be python3.8 with some specific library versions
# /export03/data/opt/hippunfold-dev/miniconda3/envs/py38/bin/python

import sys
import os
sys.path.append('/host/cassio/export03/data/opt/hippunfold-dev/model-synthseg_v0.3/SynthSeg')
from SynthSeg.brain_generator import BrainGenerator
from ext.lab2im import utils
import numpy as np

# new labeling scheme that keeps only bg, csf, gm, wm, blood
# note labels 1-4 are gm layers, 5-6 are dg layers
remap_FS = {0:0,
    2:13, #wm
    4:0, #ventricle
    5:0, #ventricle
    7:13, #cerebellar wm
    8:14, #cerebellar gm
    10:14, #thalamus
    11:14, #caudate
    12:14, #putamen
    13:14, #pallidum
    16:14, #brain stem
    17:13, #hippocampus. we will treat this as a unique label to replicate the alveus
    18:14, #amygdala
    24:0, #ventricle
    28:14, #ventralDC
    31:17, # choroid plexus
    77:13, # wm hypointensity
    41:13, #wm
    43:0, #ventricle
    44:0, #ventricle
    46:13, #cerebellar wm
    47:14, #cerebellar gm
    49:14, #thalamus
    50:14, #caudate
    51:14, #putamen
    52:14, #pallidum
    53:13, #hippocampus. we will treat this as a unique label to replicate the alveus
    54:14, #amygdala
    60:14, #ventralDC
    63:17, # choroid plexus
    77:13, # wm hypointensity
    1000:15, # neocortex
    101:16} #blood
remap_HU = {#1-4 gm layers
    #5-6 dg layers
    2:7, #SRLM
    7:8, #cyst
    5:9, #HATA
    6:10, #ind.gris
    9:11, #dgsrc
    10:12} #dgsink


path_label_map = 'labelmaps'
generation_labels = np.unique([list(remap_FS.values()) + list(remap_HU.values()) + [1,2,3,4,5,6]])
n_neutral_labels = len(generation_labels)-1
generation_classes = np.array([0] + [1]*4 + [2]*2 + list(range(3,len(generation_labels)-4))) # group hipp, dg, all others separate
generation_classes[generation_labels==25] = 1 # neocortical and hippocampal grey matter
generation_classes[-2:] = generation_classes[-2:]-1 # adjust subsequent

print(generation_labels)
print(generation_classes)

brain_generator = BrainGenerator(labels_dir=path_label_map,
                                 generation_labels=generation_labels,
                                 n_neutral_labels=n_neutral_labels,
                                 generation_classes=generation_classes,
                                 randomise_res=True,
                                 max_res_iso=1,
                                 max_res_aniso=2)

os.makedirs('/host/bb-compxg-01/export03/data/jordand/model-synthseg_v0.3/nnunet_raw/Dataset001_multihist7/imagesTr', exist_ok=True)
os.makedirs('/host/bb-compxg-01/export03/data/jordand/model-synthseg_v0.3/nnunet_raw/Dataset001_multihist7/labelsTr', exist_ok=True)
for n in range(10000):
    # generate new image and corresponding labels
    im, lab = brain_generator.generate_brain()
    # save output image and label map
    utils.save_volume(im, brain_generator.aff, brain_generator.header,
                      f'/host/bb-compxg-01/export03/data/jordand/model-synthseg_v0.3/nnunet_raw/Dataset001_multihist7/imagesTr/mh_{n:03d}_0000.nii.gz')
    utils.save_volume(lab, brain_generator.aff, brain_generator.header,
                      f'/host/bb-compxg-01/export03/data/jordand/model-synthseg_v0.3/nnunet_raw/Dataset001_multihist7/labelsTr/mh_{n:03d}.nii.gz')
