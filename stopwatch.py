# a simple stopwatch program
import time

print('Press enter to begin. Afterwards press enter to click the stopwatch.')
print('Press Ctrl-c to quit')
input() ## press enter to  begin 
print('Started')
startTime  = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time()  - startTime)
        print('Lap #%s: %s (%s)' %(lapNum, totalTime,lapTime),end ='')
        lapNum +=1 
        lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:
    ## handling the  Ctrl-C exception to keep the error message from displaying
    print('\nDone')

