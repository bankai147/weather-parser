import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad status codes
        return r.text
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

htmldata = getdata("https://weather.com/en-IN/weather/today/l/7f86adbbc3cd638c13c6882bf3e7d25a987671c362efae2932b3a46012a0593a")

path = "C:\\Users\\user\\Desktop\\ded_inside.jpg"  # Note the escaped backslashes

if htmldata:
    soup = BeautifulSoup(htmldata, 'html.parser')
    print(soup.prettify())
    n.show_toast("Weather update", "Weather report", icon_path=path, duration=10)
else:
    n.show_toast("Error", "Failed to fetch data", duration=10)