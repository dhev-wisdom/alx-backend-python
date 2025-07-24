import os
import time
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied

class RequestTimerMiddleware:
    """Middleware that logs the time taken by each request"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        print(f"Request took {duration:.2f} seconds time to process")

        return response
    

class RequestLoggingMiddleware:
    """
    Middleware that logs each user’s requests to a file,
    including the timestamp, user and the request path
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file_path = os.path.join(settings.BASE_DIR, "requests.logs")

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        print(log_message)
        print("Request header: ", request.headers)
        try:
            with open(self.log_file_path, 'a') as f:
                f.write(log_message + "\n")
        except Exception as e:
            print(f"Error: {e}\nCoundn't log request information to {self.log_file_path}")
        

        return response
    
class RestrictAccessByTimeMiddleware:
    """
    Middleware  that check the current server time
    and deny access by returning an error 403 Forbidden
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        current_server_time = timezone.now()
        current_hour = timezone.localtime(current_server_time).hour
        if (request.path.startswith('/api/conversations/') or 
        request.path.startswith('/api/messages/')):
            if 18 <= current_hour < 21:
                return response
            else:
                raise PermissionDenied("You are accessing this chat outside of allowed time")
        return response