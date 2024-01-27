import requests as r
key="c153f2d358604006a01da61ca705ec2b"
api_address='https://newsapi.org/v2/top-headlines?country=us&apikey='+key
json_data =r.get(api_address).json()

ar=[]
def news():
    for i in range(5):
        ar.append('Number '+str(i+1)+':-'+json_data['articles'][i]['title']+' ,')
    return ar

# arr=news()
# print(arr)