. ./../../assets/local/test.env
source venv/bin/activate
clear
flake8 --ignore=E501,W293,W503 src
pytest -vs tests