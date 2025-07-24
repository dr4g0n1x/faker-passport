@echo off
echo Cleaning old directories...
if exist faker rmdir /s /q faker
if exist tests\providers rmdir /s /q tests\providers

echo Installing package...
pip install -e .

echo Running simple test...
python run_simple_test.py

echo.
echo Running unit tests...
python -m unittest tests.test_passport_provider -v
