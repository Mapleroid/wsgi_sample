import wsgi

class APIManager(object):
    def __init__(self):
        pass

    def test_action(self):
        pass

class API(wsgi.Router):
    def __init__(self,mapper):
        manager = APIManager()

        manager.connect('/test',
                         controller=wsgi.Resource(manager),
                         action='test_action',
                         conditions={'method': ['POST']},
                         body_expect=False)

        super(API, self).__init__(mapper)
