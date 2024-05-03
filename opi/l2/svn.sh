#!/usr/bin/bash
rm -rf svn_repo
mkdir svn_repo
cd svn_repo

# Create SVN repository
svnadmin create repo
URL="file://$(pwd)/repo"

cd repo
svn mkdir -m "project structure" $URL/trunk $URL/branches
cd ..
svn checkout $URL/trunk/ wd
cd wd


cp -r ../../files/r0/* .
svn add f0
svn commit -m "r0" --username red

svn copy $URL/trunk $URL/branches/branch2 -m "Creating branch2" --username blue
svn switch $URL/branches/branch2

cp -r ../../files/r1/* .
svn add f1
svn commit -m "r1" --username blue

svn copy $URL/trunk $URL/branches/branch3 -m "Creating branch3" --username blue
svn switch $URL/branches/branch3

cp -r ../../files/r2/* .
svn add f2
svn commit -m "r2" --username blue

cp -r ../../files/r3/* .
svn add f3
svn commit -m "r3" --username blue

svn switch $URL/branches/branch2

cp -r ../../files/r4/* .
svn add f4
svn commit -m "r4" --username blue

svn switch $URL/trunk

cp -r ../../files/r5/* .
svn add f5
svn commit -m "r5" --username red

svn switch $URL/branches/branch3
cp -r ../../files/r6/* .
svn add f6
svn commit -m "r6" --username blue

svn switch $URL/branches/branch2
cp -r ../../files/r7/* .
svn add f7
svn commit -m "r7" --username blue

cp -r ../../files/r8/* .
svn add f8
svn commit -m "r8" --username blue

svn switch $URL/trunk
cp -r ../../files/r9/* .
svn add f9
svn commit -m "r9" --username red

svn switch $URL/trunk
svn update
svn merge $URL/branches/branch2 --accept theirs-conflict
svn commit -m "Merge branch2 into trunk" --username red

cp -r ../../files/r10/* .
svn add f10
svn commit -m "r10" --username red

svn switch $URL/branches/branch3
cp -r ../../files/r11/* .
svn add f11
svn commit -m "r11" --username blue

cp -r ../../files/r12/* .
svn add f12
svn commit -m "r12" --username blue

cp -r ../../files/r13/* .
svn add f13
svn commit -m "r13" --username blue

svn switch $URL/trunk
svn merge $URL/branches/branch3 --accept theirs-conflict
svn commit -m "Merge branch3 into trunk" --username red

cp -r ../../files/r14/* .
svn add f14
svn commit -m "r14" --username red
