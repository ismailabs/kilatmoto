@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
  echo Open http://localhost:8000/ in your browser. Press Ctrl+C to stop.
  py scripts\serve.py
  goto :end
)
where python >nul 2>nul
if %errorlevel% equ 0 (
  echo Open http://localhost:8000/ in your browser. Press Ctrl+C to stop.
  python scripts\serve.py
  goto :end
)
echo Python was not found. Install it from https://www.python.org/downloads/
pause
:end
