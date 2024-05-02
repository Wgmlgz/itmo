#!/usr/bin/bash
rm -rf svn_repo
mkdir svn_repo
cd svn_repo

# Create SVN repository
svnadmin create repo
URL="file://$(pwd)/repo"

# Create project structure with trunk and branches
svn mkdir -m "Initialize structure" $URL/trunk $URL/branches --username red

# Checkout the trunk for initial work
svn checkout $URL/trunk workdir
cd workdir

# User red initial commit
cp -r ../../files/r0/* .
svn add *
svn commit -m "r0" --username red

# Create and switch to branch2 by blue
svn copy $URL/trunk $URL/branches/branch2 -m "Creating branch2" --username blue
svn switch $URL/branches/branch2

# User blue r1 commit
cp -r ../../files/r1/* .
svn rm *
svn add *
svn commit -m "r1" --username blue

# Switch to new branch3 for r2 commit by blue
svn copy $URL/trunk $URL/branches/branch3 -m "Creating branch3" --username blue
svn switch $URL/branches/branch3

# User blue r2 commit
cp -r ../../files/r2/* .
svn rm *
svn add *
svn commit -m "r2" --username blue

# User blue r3 commit
cp -r ../../files/r3/* .
svn rm *
svn add *
svn commit -m "r3" --username blue

# Switch back to branch2 for r4 by blue
svn switch $URL/branches/branch2

# User blue r4 commit
cp -r ../../files/r4/* .
svn rm *
svn add *
svn commit -m "r4" --username blue

# Switch to trunk for r5 commit by red
svn switch $URL/trunk

# User red r5 commit
cp -r ../../files/r5/* .
svn rm *
svn add *
svn commit -m "r5" --username red

# Further commits by blue in branch3
svn switch $URL/branches/branch3
cp -r ../../files/r6/* .
svn rm *
svn add *
svn commit -m "r6" --username blue

# More commits by blue in branch2
svn switch $URL/branches/branch2
cp -r ../../files/r7/* .
svn rm *
svn add *
svn commit -m "r7" --username blue

cp -r ../../files/r8/* .
svn rm *
svn add *
svn commit -m "r8" --username blue

# User red commits r9 in trunk
svn switch $URL/trunk
cp -r ../../files/r9/* .
svn rm *
svn add *
svn commit -m "r9" --username red

# Merge branch2 into trunk
svn switch $URL/trunk
svn merge $URL/branches/branch2 --accept theirs-conflict
svn commit -m "Merge branch2 into trunk" --username red

# User red r10 commit
cp -r ../../files/r10/* .
svn rm *
svn add *
svn commit -m "r10" --username red

# User blue commits r11, r12, r13 in branch3
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

# Final merge from branch3 to trunk
svn switch $URL/trunk
svn merge $URL/branches/branch3 --accept theirs-conflict
svn commit -m "Merge branch3 into trunk" --username red

# Last commit r14 by red
cp -r ../../files/r14/* .
svn rm *
svn add *
svn commit -m "r14" --username red
