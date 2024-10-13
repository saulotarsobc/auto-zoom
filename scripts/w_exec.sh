#! bash
rm -rf build dist main.spec
pyinstaller --onefile -w --add-data "image.png;." --name "Auto Zoom" main.py