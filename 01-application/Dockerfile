FROM python:3.9-alpine
WORKDIR /app

COPY web.py .

ENV AUTHOR = "Andrei"
ENV PORT = 8000

EXPOSE 8000

CMD [ "python", "web.py" ]