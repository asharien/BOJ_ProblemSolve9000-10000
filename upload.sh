#!/bin/bash
today=$(date)
echo $today
git config --global user.name asharien
git config --global user.email asharien@naver.com 
git remote add origin https://github.com/asharien/BOJ_ProblemSolve9000-10000.git 
git add .
git status
git commit -m "Upload from Termux $today"
.././autofill.exp
