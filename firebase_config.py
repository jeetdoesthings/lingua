# url: https://console.firebase.google.com/

#modules
import pyrebase
import flet
from flet import *
import datetime
from functools import partial


config = {
    "apiKey": "AIzaSyC166K4TUz3J50KZUGQ_gmBWM3qgm6njXA",
    "authDomain": "flet-firebase-eecc7.firebaseapp.com",
    "projectId": "flet-firebase-eecc7",
    "storageBucket": "flet-firebase-eecc7.firebasestorage.app",
    "messagingSenderId": "775524762611",
    "appId": "1:775524762611:web:5c88425b0c517c40ff8886",
    # set database to None
    "databaseURL":"https://flet-firebase-eecc7-default-rtdb.firebaseio.com"
  }

# initialize firebase
firebase=pyrebase.initialize_app(config)

# set up authentication manager
auth=firebase.auth()