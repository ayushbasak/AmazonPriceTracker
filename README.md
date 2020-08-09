# Amazon Price Tracker  
***  
a price tracker and Email notifier for [Amazon](https://www.amazon.in)  

## Requirements  
- BeautifulSoup
    
## Usage  
Replace the necessary arguments in `main.py` file  
```
url = "" 
header = {"User-Agent":""}
price = 0.0 # Set the threshold
my_email = ""
my_password = ""
recievers_email = ""
duration = 1 # Number of days to Track
```  
Run the script by `py main.py`  

#### How to set Header?  
[Click Here](https://www.google.com/search?client=firefox-b-d&q=my+user+agent)  
Copy and paste your **Your User Agent** in the header dictionary mentioned  

#### Important: 
You have to keep this script running continiously, *obviously*. You can wipe clean an old PC and run the script on it, or run in online (for exanple = [PythonAnywhere](https://www.pythonanywhere.com/))  
  
Code shamelesly stolen from [Dev Ed](https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q)