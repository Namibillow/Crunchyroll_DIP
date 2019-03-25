from dan import *
from nami import *
from tony import *

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True,
                        help="name of the person you are recording")

    args = vars(parser.parse_args())

    RecordVideo(args['name'], './Dataset/PT/')
    # openCam()
