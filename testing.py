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
    "databaseURL":""
  }

# initialize firebase
firebase=pyrebase.initialize_app(config)

# set up authentication manager
auth=firebase.auth()

class UserWidget(UserControl):
    def __init__(self,title:str):
        self.title=title
        super().__init__()
    def build(self):
        self._title=Container(
            alignment=alignment.center,
            content=Text(
                self.title,
                size=15,
                text_align="center",
                weight="bold",
                color="black",
            ),
        )
        
        return Column(
            horizontal_alignment='center',
            controls=[
                Container(padding=10),
                self._title,
            ],
        )

def main(page: ft.Page):
    page.title = "LinguaMitra - Sign Up"
    page.window.width = 375
    page.window.height = 812
    page.window.resizable=False
    page.update()
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    
    def _main_column_():
        return Container(
            width=280,height
        )
    
if __name__=="__main__":
    flet.app(target=main)