# https://cx-freeze.readthedocs.io/en/latest/distutils.html
# Make sure cx_Freeze is installed - 'pip install cx_Freeze'
# Run 'python setup.py build' to create a compiled directory
# OR run 'python setup.py bdist_msi' to create a single msi installer file
import sys
from cx_Freeze import setup, Executable
includes = []
# Include your files and folders
includefiles = ['GUI/','images/','scripts/','config.yaml']
# Exclude unnecessary packages
excludes = ['cx_Freeze','setuptools','tkinter']
# Dependencies are automatically detected, but some modules need help.
# packages = ['kivy','kivymd', 'ffpyplayer','gtts']    
base = None
shortcutName = None
shortcutDir = None
if sys.platform == "win32":
    base = "Win32GUI"
    shortcutName='RAPIID'
    shortcutDir="DesktopFolder"
setup(
    name = 'RAPIID',
    version = '1.0',
    description = 'Rapid Angled Pinned Insect Imaging Device',
    author = 'A.M.T. Harmer',
    author_email = 'harmera@landcareresearch.co.nz',
    options = {'build_exe': {
        'includes': includes,
        'excludes': excludes,
        # 'packages': packages,
        'include_files': includefiles}
        }, 
    executables = [Executable('rapiid.py', 
    base = base, # "Console", base, # None
    icon='images/RAPIID_icon.ico', 
    shortcutName = shortcutName, 
    shortcutDir = shortcutDir)]
)