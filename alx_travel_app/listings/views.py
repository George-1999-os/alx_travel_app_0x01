from django.http import JsonResponse
from django.views import View

class ListingsView(View):
    def get(self, request, *args, **kwargs):
        data = {
            "message": "Welcome to the Listings endpoint"
        }
        return JsonResponse(data)
