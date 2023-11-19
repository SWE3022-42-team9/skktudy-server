#!/usr/bin

uwsgi --http 127.0.0.1:{1} -w app:app --ini app.ini:dev
