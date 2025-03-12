#!/bin/bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
gunicorn -w 4 -b 0.0.0.0:$PORT "flaskr:create_app()"