@echo off
title 🔮 Bot Soulland - Console
cd /d %~dp0

echo ===============================
echo Installing dependencies...
echo ===============================
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies!
    pause
    exit /b
)

if not exist logs (
    mkdir logs
)

echo ===============================
echo Starting Soulland bot...
echo ===============================

start "Soulland Discord Bot" python main.py > logs\bot.log 2>&1

echo ===============================
echo Bot stopped - check logs\bot.log for more info
echo ===============================
close
