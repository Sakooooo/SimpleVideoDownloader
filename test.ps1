python .\src\main.py
Write-Output "Tested No Args"

Start-Sleep -Seconds 3
# youtube test
python .\src\main.py https://www.youtube.com/watch?v=aqz-KE-bpKQ
Write-Output "Testing Youtube Download"

if (!(Test-Path -path .\tests\youtube\Video.mp4)){
    Write-Output "ERROR: Video not found!"
  }
else{
    Write-Output "INFO: Video Found! Playing."
    Write-Output "Make sure you have mpv installed!"
    Start-Sleep -Seconds 3
    mpv .\tests\youtube\Video.mp4 
  }

Start-Sleep -Seconds 5

# TODO make tiktok test
# TODO:: HOLY SHIT I HATE POWERSHELL




