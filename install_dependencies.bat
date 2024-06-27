@echo off
:: Ensure script is run as administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrative privileges. Please run as administrator.
    pause
    exit /b
)

:: Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo Python is not installed. Please install Python and add it to the PATH.
    pause
    exit /b
)

:: Install Python packages
echo Installing Python packages...
python -m pip install google-generativeai PyQt5==5.15.6 google pyqtgraph
if %errorLevel% neq 0 (
    echo Failed to install Python packages.
    pause
    exit /b
)

:: Check if PowerShell is available
powershell -Command "exit 0" >nul 2>&1
if %errorLevel% neq 0 (
    echo PowerShell is not available. Please install PowerShell.
    pause
    exit /b
)

:: Run PowerShell commands to download and install Google Cloud SDK
echo Downloading Google Cloud SDK...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe', '%TEMP%\GoogleCloudSDKInstaller.exe')"
if %errorLevel% neq 0 (
    echo Failed to download Google Cloud SDK.
    pause
    exit /b
)

echo Installing Google Cloud SDK...
powershell -Command "Start-Process '%TEMP%\GoogleCloudSDKInstaller.exe' -Wait"
if %errorLevel% neq 0 (
    echo Failed to install Google Cloud SDK.
    pause
    exit /b
)

:: Prompt user to login to Google Cloud SDK with timeout
echo Please log in to Google Cloud SDK...
start "" "cmd.exe" /C "gcloud auth login && exit"
timeout /t 200
taskkill /im gcloud.exe /f >nul 2>&1
taskkill /im conhost.exe /f >nul 2>&1

:: Check if gcloud login was successful
gcloud auth list >nul 2>&1
if %errorLevel% neq 0 (
    echo Google Cloud SDK login failed or was canceled.
    pause
    exit /b
)

echo Installation and setup complete.
pause
