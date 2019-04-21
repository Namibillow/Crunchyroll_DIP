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
│
├── README.md
│
├── .gitignore
│
└── utils.py - helper functions
│
└── buiold_datasets.py - split videos n create training dataset

BUGS(Both low priority as easy to work around):
│
└── When running dan.py as part of main process 2 all the files if run on Mac will not have     a place to go and will be put atop of crunchy roll folder (non important as quick to        work around)
│
└── When running build_dataset the resulting files will not go inside of /train but instead     create themselves in their parent videos folder
