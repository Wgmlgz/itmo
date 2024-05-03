#!/usr/bin/bash
rm -rf svn_repo
mkdir svn_repo
cd svn_repo

# Create SVN repository
svnadmin create repo
URL="file://$(pwd)/repo"

svn mkdir -m "Initialize structure" $URL/trunk $URL/branches --username red

svn checkout $URL/trunk workdir
cd workdir

cp -r ../../files/r0/* .
svn add *
svn commit -m "r0" --username red

svn copy $URL/trunk $URL/branches/branch2 -m "Creating branch2" --username blue
svn switch $URL/branches/branch2

cp -r ../../files/r1/* .
svn rm *
svn add *
svn commit -m "r1" --username blue

svn copy $URL/trunk $URL/branches/branch3 -m "Creating branch3" --username blue
svn switch $URL/branches/branch3

cp -r ../../files/r2/* .
svn rm *
svn add *
svn commit -m "r2" --username blue

cp -r ../../files/r3/* .
svn rm *
svn add *
svn commit -m "r3" --username blue

svn switch $URL/branches/branch2

cp -r ../../files/r4/* .
svn rm *
svn add *
svn commit -m "r4" --username blue

svn switch $URL/trunk

cp -r ../../files/r5/* .
svn rm *
svn add *
svn commit -m "r5" --username red

svn switch $URL/branches/branch3
cp -r ../../files/r6/* .
svn rm *
svn add *
svn commit -m "r6" --username blue

svn switch $URL/branches/branch2
cp -r ../../files/r7/* .
svn rm *
svn add *
svn commit -m "r7" --username blue

cp -r ../../files/r8/* .
svn rm *
svn add *
svn commit -m "r8" --username blue

svn switch $URL/trunk
cp -r ../../files/r9/* .
svn rm *
svn add *
svn commit -m "r9" --username red

svn merge $URL/branches/branch2 --accept theirs-conflict
svn commit -m "Merge branch2 into trunk" --username red

cp -r ../../files/r10/* .
svn rm *
svn add *
svn commit -m "r10" --username red

svn switch $URL/branches/branch3
cp -r ../../files/r11/* .
svn rm *
svn add *
svn commit -m "r11" --username blue

cp -r ../../files/r12/* .
svn rm *
svn add *
svn commit -m "r12" --username blue

cp -r ../../files/r13/* .
svn rm *
svn add *
svn commit -m "r13" --username blue

svn switch $URL/trunk
svn merge $URL/branches/branch3 --accept theirs-conflict
svn commit -m "Merge branch3 into trunk" --username red

cp -r ../../files/r14/* .
svn rm *
svn add *
svn commit -m "r14" --username red
