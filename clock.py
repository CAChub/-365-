import time

minutes = int(input("Enter the number of minutes to focus: "))
seconds = minutes * 60
while seconds:
    mins, secs = divmod(seconds, 600)
    timer = '{:2d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds = 1

print("跑起来啊")
