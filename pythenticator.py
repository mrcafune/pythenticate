import pyotp
import time
import sys
import os

    
while 1 == 1:
    os.system('clear')
    print("User Account: Sample@test.com\n")
    totp = pyotp.TOTP('INSERT KEY HERE')
    print("OTP code is currently:")
    print(totp.now())
    print(" ")


    for remaining in range(30, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining until new code...".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
