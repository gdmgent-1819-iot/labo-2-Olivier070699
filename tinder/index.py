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


# Add to like
def addToLike():
	data = { 
		'gender': 'gender',
		'name': 'name',
		'choice': 'like'
	}
	
	write(data)
	addProfile()
	
	
# Add to dislike
def addToDislike():
	data = { 
		'gender': 'gender',
		'name': 'name',
		'choice': 'dislike'
	}
	
	write(data)
	addProfile()
	
	
# Write to data.json file
def write(data):
	filePathNameWEXT = './data.json'
	with open(filePathNameWEXT, 'w') as fp:
		json.dump(data, fp)
		


# Joystick control
sense.stick.direction_left = addToLike()
sense.stick.direction_right = addToDislike() 


	
# Load first profile
addProfile();
