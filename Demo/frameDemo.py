import sys,cv2,os,subprocess,random,time

#Tkinter work credit: https://stackoverflow.com/questions/47316266/can-i-display-image-in-full-screen-mode-with-pil/47317411
if sys.version_info[0] == 2:
    import Tkinter
    tkinter = Tkinter 
else:
    import tkinter
from PIL import Image, ImageTk

def showPIL(pilImage):
    root = tkinter.Toplevel()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    imgWidth *= 10
    imgHeight *= 10
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    print("pre-update")
    root.update_idletasks()
    root.update()
    time.sleep(0.5)
    canvas.delete("all")
    print("post-update")
#end Tkinter photo viewer
#########################

# connect to camera
#   cv2.CAP_DSHOW && .destroyAllWindows() erases
#   async callback error 
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.destroyAllWindows()

global keepOrig
keepOrig = False # global var determines if program keeps original copy of photos

def negate(count):
    # negate image
    subprocess.call(f'convert {count}.png -negate {count}.png', shell=True)

def gamma(count):
    # increase gamma of image
    subprocess.call(f'convert {count}.png -gamma 5 {count}.png', shell=True)

def flip(count):
    # flip image in vertical direction
    subprocess.call(f'convert {count}.png -flip {count}.png', shell=True)

def rotational_blur(count):
    # applies a rotational blur effect
    subprocess.call(f'convert {count}.png -rotational-blur 5 {count}.png', shell=True)

def segment_5k(count):
    # segment image default val: 5000
    subprocess.call(f'convert {count}.png -segment 5000 {count}.png', shell=True)

def sketch(count):
    # sketch image default val: 1 (for speed)
    subprocess.call(f'convert {count}.png -sketch 1 {count}.png', shell=True)

def sort_pixels(count):
    # sort pixels by intensity
    subprocess.call(f'convert {count}.png -sort-pixels {count}.png', shell=True)

def spread(count):
    # spread pixels default val: 4
    subprocess.call(f'convert {count}.png -spread 4 {count}.png', shell=True)

def sigmoid(count):
    # creates sigmoidal contrast default val: 25%
    subprocess.call(f'convert {count}.png -sigmoidal-contrast 25 {count}.png', shell=True)

def edge(count):
    # create edge default val: 5
    subprocess.call(f'convert {count}.png -edge 5 {count}.png', shell=True)


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

def main():
    count = 0
    killCount = 0
    while True:
        ret, frame = camera.read() # read a frame

        # write image to current directory
        cv2.imwrite("%d.png" % count, frame)
        
        # apply effect
        pilImage = Image.open("0.png")
        showPIL(pilImage)
        applyEffect(count, 0)

        # show image to screen
        pilImage = Image.open("0.png")
        showPIL(pilImage)

        print("post main")
        killCount += 1
        print(killCount)
        if killCount == 30:
            subprocess.Popen(["py", "frameDemo.py"])
            sys.exit()
        cv2.waitKey(30)

main()
