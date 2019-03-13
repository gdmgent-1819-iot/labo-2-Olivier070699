from sense_hat import SenseHat
import requests
import json
import sys
import os

sense = SenseHat()

# Gets gender, name & age from api
def addProfile():
    profile = requests.get('https://randomuser.me/api/').json()

	global gender
	global name

    gender = profile['results'][0]['gender'];
    name = profile['results'][0]['name']['first'];
    
    showProfile();


# Shows gender, name & age
def showProfile():
    sense.show_message(gender);
    sense.show_message(name);


data = {}
data['people'] = []


# Add to like
def addToLike():
	
	data['people'].append({
	'gender': gender,
	'name': name,
	'choice': 'like'
	})
	
	with open(data.json, 'a') as outfile:
		json.dump(data, outfile)
	addProfile()
	
	
# Add to dislike
def addToDislike():
	
	data['people'].append({
	'gender': gender,
	'name': name,
	'choice': 'dislike'
	})
	with open(data.json, 'a') as outfile:
		json.dump(data, outfile)	
	addProfile()	


# Joystick control
sense.stick.direction_left = addToLike()
sense.stick.direction_right = addToDislike() 


	
# Load first profile
addProfile();
