from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calcular(request):
    meta = float(request.POST.get('meta',0))
    valorMensal = float(request.POST.get('valorMensal',0))
    resultado = int(meta / valorMensal)

    return render(request, 'home.html', {'resultado': formatarResultado(resultado), 'meta': formatarEntradas(meta),
                                          'valorMensal': formatarEntradas(valorMensal)})

def formatarEntradas(n):
    numero = f'{n:_.2f}'
    resultado = numero.replace('.', ',').replace('_', '.')
    return resultado

def formatarResultado(resultado):
    if(resultado > 12):
        r = resultado / 12
        resposta = f'{round(r)} Anos'
        return resposta

    if(resultado == 12):
        return  f'1 Ano'

    else:
        resposta = f'{resultado} Meses'
        return resposta
    