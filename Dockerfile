FROM python:latest AS applications

RUN pip install Flask

COPY web_server.py /app/
COPY resources.py /app/
COPY entrymanager.py /app/

CMD ["python", "/app/web_server.py"]

