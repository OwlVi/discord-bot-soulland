@echo off
cd /d %~dp0

python -m pip install -r requirements.txt

echo 🚀 กำลังเริ่มรันบอท...
python discordlink.py
pause