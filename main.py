from dan import *
from nami import *
from tony import *

import argparse


if __name__ == "__main__":
<<<<<<< HEAD
    RecordVideo('Tony0', './Dataset/PT/')
    #openCam()
    hello()
=======
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True,
                        help="name of the person you are recording")

    args = vars(parser.parse_args())

    RecordVideo(args['name'], './Dataset/PN/')
    # openCam()
>>>>>>> 73691c596a6b8a1060774c0866999f5eddc0e5dd
