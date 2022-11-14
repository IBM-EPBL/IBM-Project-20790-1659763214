import requests #importing a library
#replace the url and it should be in ""
a="https://api.openweathermap.org/data/2.5/weather?q=Chennai,%20IN&appid=bc453a0b339cb9ee1ad10d2dd64d0bc0"
r=requests.get(url=a)

print(r)
