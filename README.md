This repo will train a NN for highly detailed hippocampal segmentation to be used in hippunfold.

A few of its key innivations are:
- start with only ground-truth histology data
- generate synthetic MRI-like images
- label layers separately (x4 in hipp, x2 in dentate) for easier topological separability in hippunfold
- augment histology labelmaps by superimposing them on MRI backgrounds
- augment histology labelmaps using morphometric operations to make them more in-vivo like
- augment histology labelmaps to simulate sickness (e.g. thinning, malrotation, excess cysts)
- generate many MRI-like images of arbitrary contrast to make the NN contrast-agnostic

Here is an example of an initial result generated using nnunetv2:
![image](https://github.com/user-attachments/assets/448599fd-075f-4c08-981d-13ec2abe7798)

TODOs:
- hippocampal grey matter still extends superior to the actual hippocampus. Will likely need to add additional CSF to the background since these often have hippocampus directly abutting white matter on the superior side
- it may be helpful to add alveus+fimbira labels, which are generally useful but may also alleviate the issue above
- if the NN is still not performing well, we may still need template shape injection in hippunfold to avoid topological breaks. We should create a new tempalte shape from these samples (and ideally with all the same labels for simplicity)
- checkout out torchio & 3DINO as alternatives to snynthseg's BrainGenerator & nnunet
- "synthsick" for things like major athrophy, malrotation, enlarged ventricles & cysts, hypo/hyperintensities, loss of SRLM definition, etc
