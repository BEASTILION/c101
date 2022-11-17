import time 

def GetTime(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        sec = int(seconds%60)
        timer = f'{mins}mins:{sec}secs'
        print(timer)
        seconds -=1
    print('time up')

seconds = input("Write Seconds ::: ")
GetTime(int(seconds))