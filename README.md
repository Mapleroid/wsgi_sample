# wsgi_sample

一个简单的使用paste-deploy、webob、wsgi.py实现wsgi接口和URL分发的样例程序.

## 依赖（在ubuntu上）
apahce2

libapache2-mod-wsgi

python-pip

routes

webob

paste

pastedeploy

## 安装
sudo apt-get install apache2 libapache2-mod-wsgi python-pip

sudo pip install routes webob paste pastedeploy

将etc目录下的app_wsgi.conf 文件复制到/etc/apache2/sites-available，并编辑文件：

将APP_PORT替换为要运行的tcp端口

将APP_BIN_PATH 替换为wsgi_sample/app的完全路径.

然后在/etc/apache2/sites-enabled下建立app_wsgi.conf文件的符号链接：

sudo ln -s /etc/apache2/sites-available/app_wsgi.conf /etc/apache2/sites-enabled

重启apache：
sudo service apache2 restart

在浏览器中访问ip:port/v1/test可以看到返回的结果

## 调试
查看/var/log/apache2目录下的error.log日志文件，定位错误信息
