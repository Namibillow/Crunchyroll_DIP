Crunchyroll_DIP

# file structure
DIP/
│
├── train.py - main script to start training
│
├── test.py - evaluation of trained model
│
├── Datasets / - default directory for storing input data
│   │── train/
│   └── test/
│
│
├── model / - models, losses, and metrics
│   ├── data_loaders.py - specifies how the data should be fed to the network
│   └── net.py - specifies the neural network architecture, the loss function and evaluation metrics
│
├── build_dataset - scripts for generating the datasets
│   │── nami.py
│   └── tony.py
│   └── dan.py
│
├── requirements.txt
├── README.md
├── .gitignore

To run this
