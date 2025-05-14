# running with nnUNet_v2

# conda activate nnunet

export nnUNet_results=trained_models
export nnUNet_raw=nnunet_raw
export nnUNet_preprocessed=preprocessed
mkdir -p $nnUNet_results
mkdir -p $nnUNet_raw
mkdir -p $nnUNet_preprocessed

# write json file (nano nnUNet_raw/Dataset001_multihist7/dataset.json)
# { 
#  "channel_names": { 
#    "0": "anymodality"
#  }, 
#  "labels": {  
#    "background": 0,
#     "hlayer1": 1,
#    "hlayer2": 2,
#    "hlayer3": 3,
#    "hlayer4": 4,
#    "dglayer1": 5,
#    "dglayer2": 6,
#    "srlm": 7,
#    "cyst": 8,
#    "hata": 9,
#    "ind.gris.": 10,
#    "dgsrc": 11,
#    "dgsink": 12,
#    "wm": 13,
#    "gm": 14,
#    "neocort": 15,
#    "blood": 16,
#    "choroid": 17
#  }, 
#  "numTraining": 10000, 
#  "file_ending": ".nii.gz",
#  "overwrite_image_reader_writer": "SimpleITKIO"  
#  }

# get ready to train
# nnUNetv2_convert_old_nnUNet_dataset nnunet_raw/Dataset001_multihist7
nnUNetv2_plan_and_preprocess -d 001 -c 3d_fullres --verify_dataset_integrity

# train
CUDA_VISIBLE_DEVICES=0 nnUNetv2_train 001 3d_fullres 0 & 
CUDA_VISIBLE_DEVICES=1 nnUNetv2_train 001 3d_fullres 1 & 
CUDA_VISIBLE_DEVICES=2 nnUNetv2_train 001 3d_fullres 2 & 
CUDA_VISIBLE_DEVICES=3 nnUNetv2_train 001 3d_fullres 3 & 
CUDA_VISIBLE_DEVICES=4 nnUNetv2_train 001 3d_fullres 4 & 
wait

tar -cvf $nnUNet_results/nnunetv2_synthlayer.tar $nnUNet_results/Dataset001_multihist7