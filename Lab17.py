import flask
import render_template
from flask import Flask

# create an instance of Flask
app = Flask(__name__)

# route decorator binds a function to a URL
@app.route('/')
def hello():
   return 'Hello world'

@app.route('HaiderNFS')
def t_test():
    return render_template('my_template_1.html')

