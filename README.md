1. add models module
2. preprocess the data with preprocess_dataset/preprocess_4dr.py, path and model parameters specified within the file
3. demo ``` python train.py dataset=4d_dress_00123_out_8_smpl non_rigid=hashgrid rigid=skinning_field pose_correction=none  option=iter30k  ```

## License
We employ [MIT License](LICENSE) for the 3DGS-Avatar code, which covers
```
configs
dataset
models
utils/dataset_utils.py
extract_smpl_parameters.py
render.py
train.py
```

The rest of the code are modified from [3DGS](https://github.com/graphdeco-inria/gaussian-splatting). 
Please consult their license and cite them.

## Acknowledgement
This project is built on source codes from [3DGS](https://github.com/graphdeco-inria/gaussian-splatting). 
We also use the data preprocessing script and part of the network implementations from [ARAH](https://github.com/taconite/arah-release).
We sincerely thank these authors for their awesome work.

