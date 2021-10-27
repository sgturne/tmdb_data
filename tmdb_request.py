
 #api_key = "thing_copied_from_site"

f = open("api_key", "r")

api_key= f.read()
f.close()
#this will work the same as if directly had the api key inserted into document. so you can hide api key, which is like your password from anyone who may read your code.



print(api_key)