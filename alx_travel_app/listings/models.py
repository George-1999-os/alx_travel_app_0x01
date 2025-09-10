# listings/models.py
from django.db import models

class DummyModel(models.Model):
    name = models.CharField(max_length=100)

# listings/views.py
from django.http import HttpResponse

def dummy_view(request):
    return HttpResponse("Hello")
