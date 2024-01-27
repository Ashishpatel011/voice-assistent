import requests as r

url='https://official-joke-api.appspot.com/random_joke'
json_data=r.get(url).json()
arr=["",""]
arr[0]=json_data['setup']
arr[1]=json_data['punchline']
def joke():
    return arr
# x=joke()
# print(x)
