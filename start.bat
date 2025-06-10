@echo off
cd /d %~dp0

echo ===============================
echo 🔧 ติดตั้ง dependencies...
echo ===============================
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ เกิดข้อผิดพลาดในการติดตั้ง packages!
    pause
    exit /b
)

echo ===============================
echo 🚀 กำลังเริ่มรันบอท...
echo ===============================
python bot.py

echo ===============================
echo ✅ สิ้นสุดการทำงานของบอท
pause
