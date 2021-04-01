for /f "tokens=*" %%a in ('dir ".pytest_cache" /b /ad /s') do rd "%%a" /q/s
for /f "tokens=*" %%b in ('dir "__pycache__" /b /ad /s') do rd "%%b" /q/s