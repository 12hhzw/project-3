# bug reproduction script for bug #6145 of ankidroid
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    d.app_start("com.ichi2.anki")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.ichi2.anki":
            break
        time.sleep(2)
    wait()

   

    out = d(text="Custom study session").longclick()
    if not out:
        print("Success: longpress Custom study session")
    wait()
    
    out = d(text="Empty").click()
    if not out:
        print("Success: press settings")
    wait()
    
    out = d(text="Custom study session").click()
    if not out:
        print("Success: press Custom study session")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()
    
    out = d(text="Options").click()
    if not out:
        print("Success: press Options")
    wait()
    
    
    out = d(text="Define custom steps").click()
    if not out:
        print("Success: press Define custom steps")
    wait()
    
    out = d(text="Reschedule").click()
    if not out:
        print("Success: press Reschedule")
    wait()
    
    out = d(description="转到上一层级").click()
    if not out:
        print("Success: press navigation")
    wait()
    
     out = d(description="Undo").click()
    if not out:
        print("Success: press Undo")
    wait()
    
    
    

    out = d(text="Empty cards").click()
    if not out:
        print("Success: press Empty cards")
    wait()

  

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
