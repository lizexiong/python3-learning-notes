@echo off 
set day=%1 
set action=%2 
set device=%3
set date=%4
git add *
git commit -m "%1 %2 %3 %4"
git push origin master