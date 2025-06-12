@echo off
cd /d %~dp0

echo ===============================
echo install dependencies...
echo ===============================
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ error can't install packages!
    pause
    exit /b
)

echo ===============================
echo starting bot...
echo ===============================
python bot.py

echo ===============================
echo bot stopped
pause
