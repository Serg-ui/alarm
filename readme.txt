1) docker compose up (в корне)
2) docker exec -it [имя контейнера где сервер] alembic upgrade head (создаст таблицы в бд)
2) docker exec -it [имя контейнера где сервер] python fakedata.py (заполнит таблицу users)

Доки к апи: http://127.0.0.1:8000/docs