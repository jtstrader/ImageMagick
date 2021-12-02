import cv2,os,subprocess,random

# home directory
directory = r'C:\Users\IST301\Desktop\IMPG'

print(f"Starting dir: {directory}")

# connect to camera
#   cv2.CAP_DSHOW && .destroyAllWindows() erases
#   async callback error 
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.destroyAllWindows()

def negate(count):
    # negate image
    subprocess.call(f'convert {count}.png -negate ./Converted/{count}_n.png', shell=True)

def gamma(count):
    # increase gamma of image
    subprocess.call(f'convert {count}.png -gamma 5 ./Converted/{count}_g.png', shell=True)

def flip(count):
    # flip image in vertical direction
    subprocess.call(f'convert {count}.png -flip ./Converted/{count}_f.png', shell=True)

def rotational_blur(count):
    # applies a rotational blur effect
    subprocess.call(f'convert {count}.png -rotational-blur 5 ./Converted/{count}_rb.png', shell=True)

def segment_5k(count):
    # segment image default val: 5000
    subprocess.call(f'convert {count}.png -segment 5000 ./Converted/{count}_s5k.png', shell=True)

def sketch(count):
    # sketch image default val: 1 (for speed)
    subprocess.call(f'convert {count}.png -sketch 1 ./Converted/{count}_sk.png', shell=True)

def sort_pixels(count):
    # sort pixels by intensity
    subprocess.call(f'convert {count}.png -sort-pixels ./Converted/{count}_srt.png', shell=True)

def spread(count):
    # spread pixels default val: 4
    subprocess.call(f'convert {count}.png -spread 4 ./Converted/{count}_sprd.png', shell=True)

def sigmoid(count):
    # creates sigmoidal contrast default val: 25%
    subprocess.call(f'convert {count}.png -sigmoidal-contrast 25 ./Converted/{count}_sig.png', shell=True)

def edge(count):
    # create edge default val: 5
    subprocess.call(f'convert {count}.png -edge 5 ./Converted/{count}.png', shell=True)

# select random affect to apply to image
def applyEffect(count, z):
    choose = random.randint(1,10)
    if z > 0:
        choose = z # overwrite count for testing purposes
    if choose == 1:
        negate(count)
    elif choose == 2:
        gamma(count)
    elif choose == 3:
        flip(count)
    elif choose == 4:
        rotational_blur(count)
    elif choose == 5:
        segment_5k(count)
    elif choose == 6:
        sketch(count)
    elif choose == 7:
        sort_pixels(count)
    elif choose == 8:
        spread(count)
    elif choose == 9:
        sigmoid(count)
    elif choose == 10:
        edge(count)
    else:
        print("Option not available")

def devMode():
    z = 0
    # continue until user requests exit (-1)
    while z != -1:
        ret, frame = camera.read() # read in image
        print("Input option you want to test. Input -1 to exit: ")
        z = int(input())
        if z != -1:
            cv2.imwrite("test.png", frame)
            applyEffect("test", z)

def main():
    print("How many photos do you want?")
    photoCount = input()

    # dev mode
    if photoCount == "-1":
        devMode()
        return

    # grab photoCount photos
    count = 0
    for i in range(int(photoCount)):
        ret, frame = camera.read() # read a frame

        # write image to current directory
        cv2.imwrite("%d.png" % count, frame)

        # apply effect
        applyEffect(count, 0)
        count += 1

        cv2.waitKey(1000) # wait 1 second

main()
