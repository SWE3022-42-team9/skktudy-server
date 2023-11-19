#!/usr/bin

cd ./deploy
uwsgi --http 127.0.0.1:6000 -w app:app --ini app.ini:deploy
