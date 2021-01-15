from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1>Todos somos capazes de fazer melhor a cada dia</h1>')
