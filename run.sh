#!/bin/sh

export FLASK_ENV=development
export FLASK_APP=app.py

flask run -p 8004 --host=0.0.0.0
