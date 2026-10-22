class EmployeeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.user, request.path)
        resp = self.get_response(request)
        return resp