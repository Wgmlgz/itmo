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


cp -r ../../commits/r0/* .
svn add *
svn commit -m "r0" --username red

svn copy $URL/trunk $URL/branches/branch2 -m "Creating branch2" --username blue
svn switch $URL/branches/branch2

cp -r ../../commits/r1/* .
svn add *
svn commit -m "r1" --username blue

svn copy $URL/trunk $URL/branches/branch3 -m "Creating branch3" --username blue
svn switch $URL/branches/branch3

cp -r ../../commits/r2/* .
svn add *
svn commit -m "r2" --username blue

cp -r ../../commits/r3/* .
svn add *
svn commit -m "r3" --username blue

svn switch $URL/branches/branch2

cp -r ../../commits/r4/* .
svn add *
svn commit -m "r4" --username blue

svn switch $URL/trunk

cp -r ../../commits/r5/* .
svn add *
svn commit -m "r5" --username red

svn switch $URL/branches/branch3
cp -r ../../commits/r6/* .
svn add *
svn commit -m "r6" --username blue

svn switch $URL/branches/branch2
cp -r ../../commits/r7/* .
svn add *
svn commit -m "r7" --username blue

cp -r ../../commits/r8/* .
svn add *
svn commit -m "r8" --username blue

svn switch $URL/trunk
cp -r ../../commits/r9/* .
svn add *
svn commit -m "r9" --username red

# svn rm *
svn switch $URL/trunk
svn update
svn merge $URL/branches/branch2  --accept=theirs-full --dry-run
svn commit -m "Merge branch2 into trunk" --username red

cp -r ../../commits/r10/* .
svn add *
svn commit -m "r10" --username red

svn switch $URL/branches/branch3
cp -r ../../commits/r11/* .
svn add *
svn commit -m "r11" --username blue

cp -r ../../commits/r12/* .
svn add *
svn commit -m "r12" --username blue

cp -r ../../commits/r13/* .
svn add *
svn commit -m "r13" --username blue

svn switch $URL/trunk
svn merge $URL/branches/branch3  --accept=theirs-full --dry-run
svn commit -m "Merge branch3 into trunk" --username red

cp -r ../../commits/r14/* .
svn add *
svn commit -m "r14" --username red
