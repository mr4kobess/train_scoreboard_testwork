# Табло поездов
===
***

Данный проект использует стек: Python  3.9, Django 4.0.4, DRF 3.13.1

В проекте главная страница выводит табло рейсов с указанием
* Номера поезда
* Города отправления
* Города прибытия
* Даты и времени отправления
* Даты и времени прибытия
* Статуса рейса

В проекте доступны REST API для работы рейсами

Документация по API генерируется автоматически и доступна по адресу
```http://localhost:8000/swagger-api/``` или ```http://localhost:8000/redoc-api/```


***
## Развертивание в ручном режиме

1. Для запуска проекта необходимо проверить, установлен ли Python3.9 на сервер <br/>
```$ python -v```<br/>
2. Если Python не установлен, то установить <br/>
```$ sudo apt install python3.9```
3. Установить Git<br/>
```$ sudo apt-get install git```
4. Cкачать код проекта с github<br/>
```$ git clone https://github.com/mr4kobess/train_scoreboard_testwork.git```
5. Перейти в папку с проектом, создать виртуальное окружение и активировать его<br/>
```$ cd project_dir```<br/>
```$ python3 -m venv venv```<br/>
```$ source ./venv/bin/activate```
6. Установить зависимости проекта<br/>
```$ pip install -r req.txt```
7. Установить supevisor<br/>
```$ sudo apt install supervisor```
8. Создать скрипт запуска gunicorn<br/>
```$ vim /home/www/code/project/bin/start_gunicorn.sh```<br/>
С кодом:<br/> 
```
    #!/bin/bash
    source /home/www/code/project/venv/bin/activate
    exec gunicorn  -c "/home/www/code/project/gunicorn_config.py" project.wsgi
```
9. Установить права на выполнение<br/>
10. Создать конфигурационный файл<br/>
```$ vim project/supervisor.testserver.conf```
```
C содержимым:
[program:www_gunicorn]
	command=/home/www/code/project/bin/start_gunicorn.sh
	user=www
	process_name=%(program_name)s
	numprocs=1
	autostart=true
	autorestart=true
	redirect_stderr=true
```
11. Установить Gunicorn<br/>
```$ pip install gunicorn```
12. Создать конфигурационный файл Gunicorn
```
С содержимым:
    command = '/home/www/code/project/venv/bin/gunicorn'
    pythonpath = '/home/www/code/project/project'
    bind = '127.0.0.1:8001'
    workers = 3
    user = 'www'
    limit_request_fields = 32000
    limit_request_field_size = 0
    raw_env = 'DJANGO_SETTINGS_MODULE=project.settings'
```
14. Установить Nginx
` $ sudo apt-get install nginx`
15. Запустить supervisor<br/>
` $ sudo systemctl start supervisor`
16. Образец конфигурационного файла для Nginx лежит в дериктории **_deploy_**

