export $(cat .env.development | xargs)
python entrypoint.py