from flask_login import UserMixin
from app import login_manager
from flask import current_app as app
import os, json


class User(UserMixin):
    def __init__(self, id):
        self.id = id

    # def get_id(self):
    #     return self.username


@login_manager.user_loader
def user_loader(id):
    auth = app.config['AUTH']
    
    return User(id) if id in auth else None  


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')

    auth = app.config['AUTH']

    return User(username) if username in auth else None
