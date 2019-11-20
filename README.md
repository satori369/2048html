##2048html版本

```
v1.0 单机版
v2.0 可以多人并发操作

uwsgi部署 uwsgi.ini
[uwsgi]
socket=127.0.0.1:8000
#http=127.0.0.1:8000
chdir=/home/tarena/aid1907/ht2048
wsgi-file=ht2048/wsgi.py
process=4
threads=2
pidfile=uwsgi.pid
daemonize=uwsgi.log
master=true


nginx 配置 
# 在server节点下添加新的location项，指向uwsgi的ip与端口。
server {
    ...
    location / {
        uwsgi_pass 127.0.0.1:8000;  # 重定向到127.0.0.1的8000端口
        include /etc/nginx/uwsgi_params; # 将所有的参数转到uwsgi下
    }
    ...
}


nginx 配置静态文件路径
    # 先确认settings.py配置好路由
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# file : /etc/nginx/sites-available/default
# 新添加location /static 路由配置，重定向到指定的绝对路径
server {
    ...
    location /static {
        # root static文件夹所在的绝对路径,如:
         ; # 重定向/static请求的路径，这里改为你项目的文件夹
    }
    ...
}

nginx配置静态文件无效时
    vim /etc/nginx/nginx.conf
    ### 修改
    user  root;  ## 这里默认是nginx，改为root。
    worker_processes  8;  


重启uwsgi
sudo uwsgi --stop uwsgi.pid
sudo uwsgi --ini 项目文件夹/uwsgi.ini
操作nginx
sudo /etc/init.d/nginx restart
sudo /etc/init.d/nginx start|stop|restart|status



远程连接到云
	ssh root@47.106.98.251
	输入root密码
  
上传文件到云服务器
	sudo scp ht2048.tar.gz root@47.106.98.251:/root/
	上传出错时看到这个,删掉/root/.ssh/known_hosts路径下的存储的记录信息
		(报错内容)Add correct host key in /root/.ssh/known_hosts to get rid of this message.



```





```

```