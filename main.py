import PriceTracker as pt
import time
# Insert the Amazon Link and header (User-Agent) to Track
# For more info lookup the README
urls = []
with open("data.txt","r") as f:
    for line in f.readlines():
        urls.append(line.rstrip("\n"))
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
price = 11000.0 # Set the threshold
my_email = "ayushbasak0210@gmail.com"
my_password = "sitfbzbcpzkhrsqi"
recievers_email = ""
for url in urls:
        price = float(url.split(" ")[1])
        data = {"URL":url,\
                "Header":header,\
                "PriceThreshold":price,\
                "Email":my_email,\
                "Password":my_password,\
                "Reciever":recievers_email}


        tracker = pt.tracker(data)
        tracker.checkPrice()