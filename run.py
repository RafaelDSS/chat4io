from app import create_app
from app.ext.websocket import socketio

app = create_app();

socketio.run(app);
