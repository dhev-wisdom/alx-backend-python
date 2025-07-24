import os
import time
from collections import defaultdict
from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied
from .models import MessageRequestLog

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
        # print("Request header: ", request.headers)
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
    
class OffensiveLanguageMiddleware:
    """
    Middleware detects and blocks offensive languages or spam
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)

        if (request.method == 'POST' and
            (request.path.startswith('/api/conversations/') or 
                                     request.path.startswith('/api/messages/'))):
            ip = self.get_client_ip_addr(request)
            now = timezone.now()
            time_since = now - timedelta(seconds=60)

            print(f"time_since: {time_since}")

            recent_logs = MessageRequestLog.objects.filter(ip_address=ip,
                                                           timestamp__gte=time_since)
            
            if recent_logs.count() >= 5:
                raise PermissionDenied("Rate limiting exceeded. You can send max 5 messages in 1 minute")

            print(f"Rate limit check before append: {recent_logs}")

            MessageRequestLog.objects.create(ip_address=ip, timestamp=now)
        return response

    def get_client_ip_addr(self, request):
        """get client ip address"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get("REMOTE_ADDR")
    

class RolepermissionMiddleware:
    """
    Middleware checks users' role before allowing access to certain actions
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        protected_paths = [
            # '/api/messages/',
            # '/api/conversations/messages/', 
            # '/admin/', # append relevant routes
        ]

        if any(request.path.startswith(path) for path in protected_paths):
            user = request.user
            if not user.is_authenticated():
                raise PermissionDenied("User is not Authenticated")
            
            if not hasattr(user, 'role') or user.role not in ['admin', 'moderator']:
                raise PermissionDenied("You do not have permission to access this recource")
            
        return response