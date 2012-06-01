#!/usr/bin/env sh
# This should be run from the $SPLUNK_HOME/etc/apps/oidemo directory.

# Save for later
CURRENT_PWD=`pwd`

# Cleanup
rm $CURRENT_PWD/vmwareeventgen.spl

# Create a build directory that we can use
BUILD_DIR=.build/vmwareeventgen
BUILD_DIR_PARENT=.build
mkdir -p $BUILD_DIR

cp -R * $BUILD_DIR
cd $BUILD_DIR_PARENT
tar cfz $CURRENT_PWD/vmwareeventgen.spl vmwareeventgen --exclude "SA-Eventgen/eventgen.spl" --exclude "vmwareeventgen/.*"
cd $CURRENT_PWD
rm -rf $BUILD_DIR

echo "Build Complete"
