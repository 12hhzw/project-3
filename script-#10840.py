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
    out = d(text="2").click()
    if not out:
        print("Success: press 2")
    wait()
    d.app_stop("com.ichi2.anki")
    out = d(text="AnkiDroid").longclick()
    if not out:
        print("Success: press app")
    wait()
    out = d(text="开始学习").click()
    if not out:
        print("Success: press 开始学习")
    wait()
        while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
