release: python3 manage.py migrate
web: daphne portfolio.asgi:application --port $PORT --bind 0.0.0.0 -v2