@echo off
echo Running build steps...
python replace.py

echo Creating dist directory...
if not exist dist mkdir dist

echo Copying site files to dist...
powershell -Command "Get-ChildItem -Exclude dist, build.bat, replace.py | Copy-Item -Destination dist -Recurse -Force"

echo Build complete! You can now drop the 'dist' folder into Netlify.
