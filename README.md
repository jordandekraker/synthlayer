This repo will train a NN for highly detailed hippocampal segmentation to be used in hippunfold.

A few of the key innivations are:
- start with only ground-truth histology data
- generate synthetic MRI-like images
- augment histology labelmaps by superimposing them on MRI backgrounds
- augment histology labelmaps using morphometric operations to make them more in-vivo like
- augment histology labelmaps to simulate sickness (e.g. thinning, malrotation, excess cysts)
- generate many MRI-like images of arbitrary contrast to make the NN contrast-agnostic
