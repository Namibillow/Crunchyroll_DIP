'''
    Need to create sequences for both '.' and '_'

    def createDot(directory)
    def createDash(directory)
        where the directory passed is the one containing 4 frames 
        for the creation (labeled closed.jpg, open.jpg, opcl.jpg, clop) of the Dot and Dash.
***** Please make sure theyre taken from consecutive frames so as to not have much movement from face ******

    def create nums(directory)
        where the create dot and dash are in
    Numbers in morse code:
        '0':'-----',        '1':'.----',         '2':'..---',
        '3':'...--',        '4':'....-',         '5':'.....',
        '6':'-....',        '7':'--...',         '8':'---..',
        '9':'----.', 
    
    If we ever get to it alphabet in morse code:
        'A':'.-',           'B':'-...',          'C':'-.-.',
        'D':'-..',          'E':'.',             'F':'..-.',
        'G':'--.',          'H':'....',          'I':'..',
        'J':'.---',         'K':'-.-',           'L':'.-..',
        'M':'--',           'N':'-.',            'O':'---',
        'P':'.--.',         'Q':'--.-',          'R':'.-.',
        'S':'...',          'T':'-',             'U':'..-', 
        'V':'...-',         'W':'.--',           'X':'-..-', 
        'Y':'-.--',         'Z':'--..',
'''
import cv2 
import os
import sys


# Create the Dot transmutation calls
def createDot(openF, closeF, opclF, clopF):
    # Get all the information to be able to concat images into video
    height, width, layers = openF.shape
    # Message if succesful
    message = 'called createDot'
    # Create vid to be returned
    try:
        dotVid = cv2.VideoWriter('dot.mp4v', -1, 1, (width, height))
        # Concat frames into vid
        dotVid.write(openF)
        dotVid.write(opclF)
        dotVid.write(closeF)
        dotVid.write(clopF)
        dotVid.write(openF)
        # Print if successful
        print(message)
        # Close everything
        cv2.destroyAllWindows()
        dotVid.release()
        # return the video
        return None
    except:
        print("Oops!",sys.exc_info()[0],"occured.")

# Create the Dash transmutation
def createDash(openF, closeF, opclF, clopF):
    # Get all the information to be able to concat images into video
    height, width, layers = openF.shape
    message = 'called createDash'
    try:
        dashVid = cv2.VideoWriter('dash.mp4v', -1, 1, (width, height))
        # Concat frames into vid
        dashVid.write(openF)
        dashVid.write(opclF)
        dashVid.write(closeF)
        dashVid.write(closeF)
        dashVid.write(closeF)
        dashVid.write(clopF)
        dashVid.write(openF)
        # Print if successful
        print(message)
        # Close everything
        cv2.destroyAllWindows()
        dashVid.release()
        # return the video
        return None
    except:
        print("Oops!",sys.exc_info()[0],"occured.")

# Create all the transmutations of 0-9 from new directory created from createDot/createDash
# Doesnt get called until both createDot and CreateDash are finished
def createNums(directory):
    # only do something if checkDir passes
    if checkDir(directory):
        # Store in variables to later recall
        openF  = cv2.imread('open.jpg')
        closeF = cv2.imread('close.jpg')
        opclF  = cv2.imread('opcl.jpg')
        clopF  = cv2.imread('clop.jpg')
        # Call createDot and createDash to create them from ^
        createDot(openF, closeF, opclF, clopF)
        createDash(openF, closeF, opclF, clopF)
        # Create all the numbers if ^ was succesful
        print('videos createsd')

# Checks to make sure all the files are included in the passed directory
def checkDir(directory):
    # Move to cur directory
    if not os.path.exists(directory):
        print('Path doesnt exist')
        return False
    print(directory)
    os.chdir(directory);
    cwd = os.getcwd()
    print(cwd);
    # Store values to check
    openExist = os.path.exists('open.jpg')
    closeExist = os.path.exists('close.jpg')
    opclExist = os.path.exists('opcl.jpg')
    clopExist = os.path.exists('clop.jpg') 
    # Check if they exist
    if openExist and closeExist and opclExist and clopExist:
        print('All the files exist')
        return True
    elif not openExist and closeExist and opclExist and clopExist:
        print('Missing open.jpg')
        return False
    elif openExist and not closeExist and opclExist and clopExist:
        print('Missing close.jpg')
        return False
    elif openExist and closeExist and not opclExist and clopExist:
        print('Missing opcl.jpg')
        return False
    elif openExist and closeExist and opclExist and not clopExist:
        print('Missing clop.jpg')
        return False
    # If multiple dont exist
    else:
        print('Missing multiple files')
        return False


