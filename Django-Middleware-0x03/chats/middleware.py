import os
import time
from datetime import datetime
from django.conf import settings

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
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        print(log_message)
        try:
            with open(self.log_file_path, 'a') as f:
                f.write(log_message + "\n")
        except Exception as e:
            print(f"Error: {e}\nCoundn't log request information to {self.log_file_path}")
        
        response = self.get_response(request)

        return response