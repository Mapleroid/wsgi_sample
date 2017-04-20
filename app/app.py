from paste.deploy import loadapp 

def initialize_application():
	config = "/home/crack/wsgi_sample/etc/app-paste.ini"
	app_name = "app-wsgi"
	wsgi_app = loadapp("config:%s" % config, app_name)
	return wsgi_app
