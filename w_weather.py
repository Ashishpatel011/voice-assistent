import requests as r
key='6df5771e86fcd7302e7024df221ac938'
api_address='https://api.openweathermap.org/data/2.5/weather?q=gwalior&appid='+key
json_data=r.get(api_address).json()

def temp():
    temprature=round(json_data["main"]["temp"]-273,1)
    return temprature
def des():
    description=json_data['weather'][0]['description']   
    return description


# print(temp())
# print(des())