import time
import pyautogui
from sys import platform

#change the path in the first argument to the path of your source file
source = open('/home/you/that folder/that sub-folder/that file.py', 'r')
#add the string #------ beneath each block of text you want to separate
blocks = source.read().split('#------')
#total length of video. loop below will divide this by the number of blocks
videoLength = .25
#if it's scrolling too much, decrease this number. too little, increase it.
scrollFactor = 100

for i in range(len(blocks)):
    time.sleep(videoLength*60/len(blocks))
    pyautogui.scroll(-len(blocks[i])//scrollFactor)
    destination = open('/home/you/destination file.py', 'a')
    destination.write(blocks[i])
    destination.close()

#the following is a little alarm I put in to alert me to when the program is finished
#you will need to install sox if you want to play it on linux (via apt) or macOS (via port)

duration = .5  # second
f = 349.23/2  # Hz
g = 392.00/2
a = 440/2

x = 0

if platform == 'win32':
    import winsound
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)

else:
    import os
    while x < 2:
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, f))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, g))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, a))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, g))
        x += 1

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (3, f))

#hope you enjoyed it!
