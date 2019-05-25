# target
i just want to offer some interface for my friends,
then then can get some data easily through 'tony'.
such as then can get json-data from www.leisu.com,
just send a simple get request without complicated environment.
i will write all my progress while building the project.

if you have any questions ,send email to:
15261066994tel@gmail.com

powered by guanrongjia at 2018/04/30
all rights reserved

# use：
1.python2.7

2.django1.11.8

# progress
## django
windows:  
1、pip install Django==1.11.8

2、in cmd console : django-admin startproject tony, 
then a empy django project in the folder named tony will be created 

*ps:   if you got error : django-admin.py不是内部或外部命令，也不是可运行的程序或批处理文件
add django bin in system path: in my pc, is  "C:\Python27\Lib\site-packages\django\bin"*

3、 python manage.py startapp friday

-----------

##  uwsgi
#### test
touch test_uwsgi.py
```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
```

    
uwsgi --plugin python --http :8001 --wsgi-file test_uwsgi.py

#### uwsgi config file

``` 
[uwsgi]
# 项目目录
chdir = /usr/program/gitdata/tony
# 指定项目的application
module=tony.wsgi:application
# 进程个数       
# workers=5
pidfile=/tmp/project-master.pid
# 启用主进程
master = true
# 启用线程
enable-threads=true
processes = 2
# 指定socket
socket =localhost:8888 
# 自动移除unix Socket和pid文件当服务停止的时候
vacuum = true  
# 序列化接受的内容，如果可能的话
thunder-lock=true
# 最大缓冲区，如果设置得太小，请求的数据超过buffer-size的话，网站会起不来
buffer-size = 65536 
# uwsgi默认日志 + 程序print输出
logto = /tmp/uwsgi.log
# 打印时间
logdate = true
```

----
start: uwsgi --ini /etc/nginx/uwsgi.ini  &

stop: uwsgi --stop /tmp/project-master.pid

reload: uwsgi --reload /tmp/project-master.pid

*uwsgi 中文文档: https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/Logging.html*

*uwsgi en doc: https://uwsgi-docs.readthedocs.io/en/latest/Management.html*

----

## nginx
/etc/nginx/nginx.conf
``` 
user root;
worker_processes 8;
http{
	include /etc/nginx/mime.types;
	default_type application/octet-stream;
	server {
		listen 80;
		server_name guanrongjia.top; 
		charset utf-8;
		client_max_body_size 75M;
		location /media {
			alias /virtualenv/mezzanine/mezzsite/static/media;
		}
		location /static {
			alias /virtualenv/mezzanine/mezzsite/static;
		}
		location / {
			uwsgi_pass localhost:8888;
			include /etc/nginx/uwsgi_params;
		}
	}
}
events {
	worker_connections 1024;
}
``` 

service nginx start
service nginx restart
service nginx stop