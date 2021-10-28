import json
import pandas
import glob
import os

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


df = pandas.DataFrame()

for json_file_name in glob.glob('json_files/*.json'): 
	#json_file_name = "json_files/tmdb550.json"
	f = open(json_file_name)
	json_data = json.load(f)
	f.close()



	production_countries = [item['iso_3166_1']for item in json_data['production_countries']]
	production_countries = ";".join(production_countries)


	genres = [item['name'] for item in json_data['genres']]

	#[{'iso_3166_1': 'DE', 'name': 'Germany'}, {'iso_3166_1': 'US', 'name': 'United States of America'}]

	df = df.append({
		'title': json_data['title'],
		'id' : json_data['id'],
		'imdb_id': json_data['imdb_id'],
		'budget': json_data['budget'],
		'revenue': json_data['revenue'],
		'genres': genres, 
		'release_date': json_data['release_date'],
		'vote_average': json_data['vote_average'],
		'production_countries': production_countries 
		}, ignore_index = True)


df.to_csv("parsed_files/tmdb_dataset.csv")

	#what do you expect at this point will be the output 
	#print(json_data["title"])
	#print(json_data)
	#print(json_data['adult'])
	#print(json_data['backdrop_path'])
	#print(json_data['genres'][0]['name'])
	#print(json_data['production_companies'][2]['name'])
