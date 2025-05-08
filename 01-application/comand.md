Создан приватный репозиторий на [Docker Hub](https://hub.docker.com/ ).  
На локальной машине выполнена авторизация и подготовка образа для отправки:

```bash
docker login

docker tag echo-server:latest andredocker2003/echo_server:latest

docker push andredocker2003/echo_server:latest

docker run --rm -p 8000:8000 -e AUTHOR="SFLFKF" andredocker2003/echo_server:latest