from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message="Rest is important to mental health",
            app_icon = "",
            timeout = 5)
        
        time.sleep(20)
            

# pythonw filename.py  to run in background