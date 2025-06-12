from django.shortcuts import render
from django.http import HttpResponse
from .models import hobbies, cryptoFacts
from Crypto.PublicKey import RSA

# Create your views here.
def home(request):
    hobbies_list = hobbies.objects.all()
    crypto_facts_list = cryptoFacts.objects.all()
    return render(request, "home.html", {"hobbies": hobbies_list, "cryptoFacts": crypto_facts_list})

def RSA_public_key(request):
    key = RSA.generate(4096)    # se genera una clave RSA de 4096 bits
    public_key = key.publickey().exportKey().decode()    # decodifica a texto la llave publica
    response = HttpResponse(public_key, content_type='text/plain')    # tipo de contenido texto plano
    response['Content-Disposition'] = 'attachment; filename="public_key_AAFC.txt"'     # nombre del archivo .txt
    return response