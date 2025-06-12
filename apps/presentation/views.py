from django.shortcuts import render
from django.http import HttpResponse
from .models import hobbies, cryptoFacts
from Crypto.PublicKey import RSA

# Create your views here.
def home(request):
    hobbies_list = hobbies.objects.all()
    crypto_facts_list = cryptoFacts.objects.all()
    return render(request, "home.html", {"hobbies": hobbies_list, "cryptoFacts": crypto_facts_list})