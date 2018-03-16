from flask import Flask, render_template

apps = Flask(__name__)
apps.config.from_object('config')

from microblog.app import views

