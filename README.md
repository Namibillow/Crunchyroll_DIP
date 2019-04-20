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



#### WHAT WE NEED TO DO ####
- CREATE DATASETS
    - Split videos to frames
        - Create label txt file
            - eg.: "1 Video/Folder"
        - RESCALE the images
        - 1 video is 5 seconds so captured the frames per sec

    - Feed it into CNN to extract features and then LSTM



Datasets/
Train/
    digit_0/
        video1/
            frame1.jpg (image ratio needs to be 1:2 (112, 224))
            frame2.jpg
            frame3.jpg
            frame4.jpg
            ...
        video2/
        video3/
        ...

    digit_1/
        video1/
        video2/

    digit_2/
    digit_3/
    digit_4/
    digit_5/
    digit_6/
    digit_7/
    digit_8/
    digit_9/
    label.txt/
        - 0 /digit_0
        - 1 /digit_1
        - 2 /digit_2
        - 3 /digit_3
        - 4
        - 5
        - 6
        - 7
        - 8
        - 9


Test/
