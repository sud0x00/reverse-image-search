@echo off

echo Image name is %~1
python imgup.py %~1 >> output.txt

for /f "delims=" %%x in (output.txt) do set value=%%x
echo %value%
python yandex.py %value%
python tineye.py %value%
python bing.py %value%
python google.py %~1
