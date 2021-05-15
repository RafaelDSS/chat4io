from flask import Blueprint, render_template, g, Response, request
from app.ext.websocket import socketio
from flask_socketio import emit, send


app_home  = Blueprint('home', __name__)

@app_home.route('/')
def home():
    return render_template('index.html', timeid=id)

@socketio.on('message server')
def response(msg):
    socketio.emit('message client', {'msg': msg, 'id': request.sid}, broadcast=True)
    

def configure(app):
    app.register_blueprint(app_home)