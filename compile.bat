If exist obf (rd obf /s /q)
copy src\a.py input\
python Intensio-Obfuscator\intensio\intensio_obfuscator.py --input input --output obf -rth
copy src\autoreportes.py obf\
cd obf
REM pyinstaller --icon=..\src\dmm.ico --noconsole main.py
REM pyinstaller --icon=..\src\dmm.ico autoreportes.py
pyinstaller autoreportes.py
cd dist\autoreportes
copy ..\..\..\src\*.col .
autoreportes.exe 
cd ..\..\..
