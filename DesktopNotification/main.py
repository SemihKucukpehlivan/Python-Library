from plyer import notification
import time

if __name__ =="__main__":
    notification.notify(
        title = "Heading Here",
        message = "Description Here",

        #displaying time
        timeout=2
    )
    time.sleep(7)