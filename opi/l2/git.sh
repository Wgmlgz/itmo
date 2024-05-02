#!/usr/bin/bash
rm -rf git_repo
mkdir git_repo
cd git_repo
git init

git config --local user.name "red"
git config --local user.email red@mail.ru
cp -r ../files/r0/* .
git add .
git commit -m "r0"

git config --local user.name "blue"
git config --local user.email blue@mail.ru
git checkout -b branch2
cp -r ../files/r1/* .
git add .
git commit -m "r1"

git checkout -b branch3
cp -r ../files/r2/* .
git add .
git commit -m "r2"

cp -r ../files/r3/* .
git add .
git commit -m "r3"

git checkout branch2
cp -r ../files/r4/* .
git add .
git commit -m "r4"

git config --local user.name "red"
git config --local user.email red@mail.ru
git checkout main
cp -r ../files/r5/* .
git add .
git commit -m "r5"

git config --local user.name "blue"
git config --local user.email blue@mail.ru
git checkout branch3
cp -r ../files/r6/* .
git add .
git commit -m "r6"

git checkout branch2
cp -r ../files/r7/* .
git add .
git commit -m "r7"

cp -r ../files/r8/* .
git add .
git commit -m "r8"

git config --local user.name "red"
git config --local user.email red@mail.ru
git checkout main
cp -r ../files/r9/* .
git add .
git commit -m "r9"
git merge branch2 --commit --no-edit


cp -r ../files/r10/* .
git add .
git commit -m "r10"

git config --local user.name "blue"
git config --local user.email blue@mail.ru
git checkout branch3
cp -r ../files/r11/* .
git add .
git commit -m "r11"

cp -r ../files/r12/* .
git add .
git commit -m "r12"

cp -r ../files/r13/* .
git add .
git commit -m "r13"

git config --local user.name "red"
git config --local user.email red@mail.ru
git checkout main
cp -r ../files/r14/* .
git add .
git commit -m "r14"
git merge branch3 --commit --no-edit

git log --graph --all --decorate --oneline --date-order
