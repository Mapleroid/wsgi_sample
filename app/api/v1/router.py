import wsgi

class APIManager(object):
    def __init__(self):
        pass

    def test_action(self,req):
        return {
            "test" : "OK"
        }

class API(wsgi.Router):
    def __init__(self,mapper):
        manager = APIManager()

        mapper.connect('/test',
                         controller=wsgi.Resource(manager),
                         action='test_action',
                         conditions={'method': ['GET']},
                         body_expect=False)

        super(API, self).__init__(mapper)
