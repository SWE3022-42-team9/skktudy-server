#!/usr/bin

cd ./${1}
uwsgi --http 127.0.0.1:{2} -w app:app --ini app.ini:dev
