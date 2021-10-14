import cv2,subprocess,random,time

# home directory
directory = r'C:\Users\IST301\Desktop\IMPG\ImageMagick\Web'

print(f"Starting dir: {directory}")

# connect to camera
#   cv2.CAP_DSHOW && .destroyAllWindows() erases
#   async callback error 
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.destroyAllWindows()

prev = -1

def negate():
    # negate image
    subprocess.call(f'convert image.png -negate image_n.png', shell=True)
    print("negate")

def gamma():
    # increase gamma of image
    subprocess.call(f'convert image.png -gamma 2 image_n.png', shell=True)
    print("gamma")

def flip():
    # flip image in vertical direction
    subprocess.call(f'convert image.png -flip image_n.png', shell=True)
    print("flip")

def rotational_blur():
    # applies a rotational blur effect
    subprocess.call(f'convert image.png -rotational-blur 5 image_n.png', shell=True)
    print("rotational-blur")

def segment_5k():
    # segment image default val: 5000
    subprocess.call(f'convert image.png -segment 5000 image_n.png', shell=True)
    print("segment 5k")

def sketch():
    # sketch image default val: 1 (for speed)
    subprocess.call(f'convert image.png -sketch 1 image_n.png', shell=True)
    print("sketch")

def sort_pixels():
    # sort pixels by intensity
    subprocess.call(f'convert image.png -sort-pixels image_n.png', shell=True)
    print("sort pixels")

def spread():
    # spread pixels default val: 4
    subprocess.call(f'convert image.png -spread 4 image_n.png', shell=True)
    print("spread")

def sigmoid():
    # creates sigmoidal contrast default val: 25%
    subprocess.call(f'convert image.png -sigmoidal-contrast 25 image_n.png', shell=True)
    print("sigmoid")

def edge():
    # create edge default val: 5
    subprocess.call(f'convert image.png -edge 5 image_n.png', shell=True)
    print("edge")

# select random affect to apply to image
def applyEffect():
    global prev
    choose = random.randint(1, 10)
    while prev == choose:
        choose = random.randint(1,10)
    prev = choose
    if choose == 1:
        negate()
    elif choose == 2:
        gamma()
    elif choose == 3:
        flip()
    elif choose == 4:
        rotational_blur()
    elif choose == 5:
        segment_5k()
    elif choose == 6:
        sketch()
    elif choose == 7:
        sort_pixels()
    elif choose == 8:
        spread()
    elif choose == 9:
        sigmoid()
    elif choose == 10:
        edge()
    # input(f"post edit, choose: {choose}")
    # end of apply effect set image to new image
    # run powershell command to force rename file to set new image
    cmd = rf'Move-Item -Force -Path "C:\Users\IST301\Desktop\IMPG\ImageMagick\Web\image_n.png" -Destination "C:\Users\IST301\Desktop\IMPG\ImageMagick\Web\image_magick.png"'
    subprocess.run(["powershell", "-Command", cmd])
        
def main():
    # grab photo photos
    while True:
        ret, frame = camera.read() # read a frame

        # write image to current directory
        cv2.imwrite("image.png", frame)
        cv2.imshow('IMPG Frame Grab', frame)

        # apply effect
        applyEffect()
        # cv2.waitKey(30) # wait 1 second
        time.sleep(5)
main()

