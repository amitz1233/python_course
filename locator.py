import  requests

url=input("please enter a valid url:")
response=requests.get('http://' +url)
print(response.text)