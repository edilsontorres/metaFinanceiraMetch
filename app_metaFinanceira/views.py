from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calcular(request):
    n1 = int(request.POST.get('meta',0))
    n2 = int(request.POST.get('valorMensal',0))
    resultado = n1 / n2
    return render(request, 'home.html', {'resultado': resultado})
    