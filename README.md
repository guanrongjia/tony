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

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
    
uwsgi --plugin python --http :8001 --wsgi-file test_uwsgi.py

#### uwsgi config file
[uwsgi]
chdir = /usr/program/gitdata/tony
module=tony.wsgi:application
pidfile=/tmp/project-master.pid
master = true
processes = 2
socket =localhost:8888 
vacuum = true  #退出时清理环境
buffer-size = 65536  

uwsgi --ini uwsgi.ini

----------

## nginx
/etc/nginx/nginx.conf

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

service nginx start
service nginx restart
service nginx stop