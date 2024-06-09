[app]
# (str) Title of your application
title = SampleApp
# (str) Package name
package.name = sampleapk
# (str) Package domain (needed for android/ios packaging)
package.domain = org.novfensec
# (str) Source code where the main.py live
source.dir = .
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,txt,atlas
# (list) List of inclusions using pattern matching
source.include_patterns = images/*.png
# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec
# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv
# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg
# (str) Application versioning (method 1)
version = 0.1
# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py
# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,kivymd==0.104.2,pillow==8.3.1
# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/nfsIcon/images.png
presplash.filename = %(source.dir)s/images/images.png

# (str) Icon of the application
icon.filename = %(source.dir)s/nfsIcon/favicon.png
icon.filename = %(source.dir)s/images/favicon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait
# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY
#
# OSX Specific
#
#
# author = © Copyright Novfensec Inc.
# change the major version of python used by the app
osx.python_version = 3
# Kivy version to use
osx.kivy_version = 2.1.0
#
# Android specific
#
