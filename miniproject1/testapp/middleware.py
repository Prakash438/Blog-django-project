from django.http import HttpResponse
class ExecutionFlowMiddleware():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('this line is printed from middleware before executing viw function')
        response = self.get_response(request)
        print("This line is printing after executing view function")
        return response

class UnderMaintainanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        return self.get_response(request)

    def process_exception(self,request,exception):
        s = "<h1> Currently we are facing some technical problem please check after some time</h1>"
        s2 = '<h2>Raised excption:{}</h2>'.format(exception)
        s3 = '<h2>Raised excption description:{}</h2>'.format(exception.__class__.__name__)
        return HttpResponse(s+s2+s3)