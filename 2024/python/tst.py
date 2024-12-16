import time
for i in range(10):
    time.sleep(1)
    print('{:02d}'.format(10-i), end="\r")