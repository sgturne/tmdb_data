import urllib.request
import os 
import json
import time 

f = open("api_key", "r")

api_key= f.read()
f.close()
#this will work the same as if directly had the api key inserted into document. so you can hide api key, which is like your password from anyone who may read your code.

response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/latest?api_key="+ api_key)
json_response = json.load(response)
movie_end = int(json_response['id'])

movie_start= movie_end - 10 
#movie_start = 0



if not os.path.exists("json_files"):
	os.mkdir("json_files")

for movie_id in range(movie_start, movie_end):


	response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/"+ str(movie_id) + "?api_key="+ api_key)


	json_response = json.load(response)

	f = open("json_files/tmdb" + str(movie_id) + ".json", "w")
	f.write(json.dumps(json_response))
	f.close()
	time.sleep(40)

