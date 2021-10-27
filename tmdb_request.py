import urllib.request
import os 

 #api_key = "thing_copied_from_site"

f = open("api_key", "r")

api_key= f.read()
f.close()
#this will work the same as if directly had the api key inserted into document. so you can hide api key, which is like your password from anyone who may read your code.

if not os.path.exists("json_files"):
	os.mkdir("json_files")


movie_id = 550

response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/"+ str(movie_id) + "?api_key="+ api_key)

print(response)
