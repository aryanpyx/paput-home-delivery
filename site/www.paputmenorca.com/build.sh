#!/bin/bash
set -e

echo "Running build steps..."
python3 replace.py

echo "Creating dist directory..."
mkdir -p dist

echo "Copying site files to dist..."
# Use rsync to copy files, excluding the scripts and dist directory
rsync -a --exclude='dist' --exclude='build.bat' --exclude='build.sh' --exclude='replace.py' ./ dist/

echo "Build complete! Ready for Netlify."
