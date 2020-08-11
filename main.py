import PriceTracker as pt
import time
# Insert the Amazon Link and header (User-Agent) to Track
# For more info lookup the README
url = "https://www.flipkart.com/redmi-8-ruby-red-64-gb/p/itm6981a578c4d90?pid=MOBFKPYDCVSCZBYR&lid=LSTMOBFKPYDCVSCZBYR7PKM5A&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=5ca7b5a2-8489-41d3-93c8-75154267db67.MOBFKPYDCVSCZBYR.SEARCH&ppt=sp&ppn=sp&ssid=ujt2q6x784f7591c1597166432509&qH=eb4af0bf07c16429" 
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
price = 11000.0 # Set the threshold
my_email = "ayushbasak0210@gmail.com"
my_password = "sitfbzbcpzkhrsqi"
recievers_email = ""

data = {"URL":url,\
        "Header":header,\
        "PriceThreshold":price,\
        "Email":my_email,\
        "Password":my_password,\
        "Reciever":recievers_email}


tracker = pt.tracker(data)
tracker.checkPrice()