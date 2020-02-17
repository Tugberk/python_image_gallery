@echo off
cd \
cd temp
del index.html
cd images
dir /b >> ../index.html
cd ..
start run.py


