@echo off
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "datestamp=%YYYY%%MM%%DD%" & set "timestamp=%HH%%Min%%Sec%"
set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
echo datestamp: "%datestamp%"
echo timestamp: "%timestamp%"
echo fullstamp: "%fullstamp%"

mkdir data\dbbackup\%fullstamp%

move core\migrations data\dbbackup\%fullstamp%\migrations\core
move product\migrations data\dbbackup\%fullstamp%\migrations\product
move program\migrations data\dbbackup\%fullstamp%\migrations\program

move data\db.sqlite3 data\dbbackup\%fullstamp%

call migrate.bat
python manage.py create_super_user
python manage.py create_default_configuration