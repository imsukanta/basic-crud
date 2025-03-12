#!/bin/bash
flask --app flaskr db init
flask --app flaskr db migrate -m "Initial migration"
flask --app flaskr db upgrade
gunicorn -w 4 -b 0.0.0.0:$PORT "flaskr:create_app()"