from flask_socketio import SocketIO


socketio = SocketIO()

def configure(app):
    app.socketio = socketio.init_app(app)
