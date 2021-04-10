from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect

class SessionAuth(MiddlewareMixin):
    def process_request(self,request):
        paths = request.path.split('/')
        white_list = ['','signin','signup','sign_in','sign_up','admin']
        if paths[1] in white_list:
            return None
        else:
            is_login = request.session.get('is_login')
            if is_login == True:
                return None
            else:
                return redirect('signin')

    def process_response(self,request,response):
        return response
