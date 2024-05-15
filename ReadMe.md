Basic structure for using fastapi

How to run application from root directory in Development
- uvicorn app.main:app --host 127.0.0.1 --port 8000
- uvicorn app.main:app --host 0.0.0.0 --port 5000

How to run application from root directory in Production
- uvicorn app.main:app --host 0.0.0.0 --port 8081 --ssl-keyfile /etc/pki/nginx/private/server.key --ssl-certfile /etc/pki/nginx/server.crt
