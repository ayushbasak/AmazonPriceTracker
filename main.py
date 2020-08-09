import PriceTracker as pt
import time
# Insert the Amazon Link and header (User-Agent) to Track
# For more info lookup the README
url = "" 
header = {"User-Agent":""}
price = 0.0 # Set the threshold
my_email = ""
my_password = ""
recievers_email = ""
duration = 1 # Number of days to Track

data = {"URL":url,\
        "Header":header,\
        "PriceThreshold":price,\
        "Email":my_email,\
        "Password":my_password,\
        "Reciever":recievers_email}


tracker = pt.tracker(data)

def track(duration):
    while(duration > 0):
        print(tracker.checkPrice())
        time.sleep(86400)
        duration -= 1