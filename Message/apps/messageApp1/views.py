from django.shortcuts import render

# Create your views here.
from .models import UserMessage
def get_form(request):
    return render(request, "message_form.html")
