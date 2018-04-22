import time
import pyautogui
from sys import platform

if platform == 'win32':
    import winsound

else:
    import os


sPath = input('Path of source: ')
source = open(sPath, 'r')
dPath = input('Path of destination: ')
destination = open(dPath, 'a')
separator = input('Separator string: ')
blocks = source.read().split(separator)
blockLength = int(input("Seconds per section: "))
warningYN = input("Warn before change? (y/n) ")

if warningYN.lower() == "y":
    warningLength = int(input("Seconds warning before change: "))

scrollFactor = 0
scrollYN = input("Autoscroll? (y/n) ")

if scrollYN.lower() == "y":
    calibrated = "n"
    scrollFactor = input('Okay, let\'s test your scroll. Open your editor to the destination file. If you have done this before and already know your scroll factor, enter it here. Otherwise, just hit ENTER, then click in the editor window of the destination file.') or 100

    while calibrated == "n":
        time.sleep(5)
        for i in range(len(blocks)):
            time.sleep(1)
            pyautogui.scroll(-len(blocks[i])//scrollFactor)
            destination = open(dPath, 'a')
            destination.write(blocks[i])
            destination.close()

        calibrated = input('Did that scroll correctly? (y/n) ')
        if calibrated == 'n':
            scrollFactor = int(input('Ok. That test was with a scroll factor of %d. The lower the number, the greater the scrolling. What number would you like to try now? ' % scrollFactor))

input('Great. We\'re all set. When you\'re ready, just hit ENTER and click inside the editor window of your destination file.')
time.sleep(5)

def warn():
    if platform == 'win32':
        duration = 500  # millisecond
        a = 440  # Hz
        winsound.Beep(freq, duration)
    else:
        duration = .5
        a = 440
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, a))

        

if warningYN.lower() == 'y':
    for i in range(len(blocks)):
        pyautogui.scroll(-len(blocks[i])//scrollFactor)
        destination = open(dPath, 'a')
        destination.write(blocks[i])
        destination.close()
        time.sleep(blockLength - warningLength)
        warn()
        time.sleep(warningLength)

else:
    for i in range(len(blocks)):
        pyautogui.scroll(-len(blocks[i])//scrollFactor)
        destination = open(dPath, 'a')
        destination.write(blocks[i])
        destination.close()
        time.sleep(blockLength)

#the following is a little alarm I put in to alert me to when the program is finished
#you will need to install sox if you want to play it on linux (via apt) or macOS (via port)

if platform == 'win32':
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)

else:
    duration = .5  # second
    f = 349.23/2  # Hz
    g = 392.00/2
    a = 440/2
    x = 0

    while x < 2:
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, f))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, g))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, a))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, g))
        x += 1

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (3, f))

#hope you enjoyed it!
