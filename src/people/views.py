from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def index(request):
    contacts = Contact.objects.all()
    return render(
        request, 'people/index.html', {'contacts': contacts}
    )


def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(
        request, 'people/new_contact.html', {'form': form}
    )
