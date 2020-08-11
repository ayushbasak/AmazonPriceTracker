# Amazon Price Tracker
***
a price tracker and Email notifier for [Amazon](https://www.amazon.in)

## Requirements
- BeautifulSoup
- requests
   
## Usage

- Add your tracking url (Either Amazon or Flipkart) to `data.txt` in the given form:
<E-commerce Product URL><SPACE><Threshold Price>
You can insert any number of links in every *newline* in `data.txt`

- Replace the necessary arguments in `main.py` file.
```
header = {"User-Agent":""}
price = 0.0 # Set the threshold
my_email = ""
my_password = ""
recievers_email = ""
```
Run the script in your terminal `py main.py`. (for one time use or schedule your script)

#### How to set Header?
[Click Here](https://www.google.com/search?client=firefox-b-d&q=my+user+agent)
Copy and paste **Your User Agent** in the header dictionary mentioned above.

#### Important:
##### Schedule your script:
- On a [Windows Machine](https://www.youtube.com/watch?v=n2Cr_YRQk7o)  
- On a [Linux/Mac Machine](https://www.youtube.com/watch?v=QZJ1drMQz1A)


Code shamelessly stolen from [Dev Ed](https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q)