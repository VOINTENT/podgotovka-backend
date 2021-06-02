. ./../../assets/local/local.env
source venv/bin/activate
clear
flake8 --ignore=E501,W293,W503 src
uvicorn app:app --reload