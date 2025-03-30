# This middleware is used for testing purposes only.
# FAKE IP Middleware to simulate a request from a specific IP address


class FakeIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.META["REMOTE_ADDR"] = "152.56.70.150"  # Fake IP
        return self.get_response(request)
