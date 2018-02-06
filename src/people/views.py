from django.shortcuts import render
from .models import Contact

def index(request):
  contacts = Contact.objects.all()
  return render(
    request, 'people/index.html', {'contacts': contacts}
  )