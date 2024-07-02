@echo off

rem Run PyInstaller to create the executable
pyinstaller --noconsole --onefile -w QDodger.py

echo Build completed.

