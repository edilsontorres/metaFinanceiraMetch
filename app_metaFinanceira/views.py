from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calcular(request):
    n1 = request.POST.get('meta')
    meta = formatarEntradas(n1)

    n2 = request.POST.get('valorMensal')
    valorMensal = formatarEntradas(n2)

    resultado = int(meta / valorMensal)

    return render(request, 'home.html', {'resultado': formatarResultado(resultado), 'meta': formatarSaidas(meta),
                                          'valorMensal': formatarSaidas(valorMensal)})


def formatarEntradas(n):
    numero = str(n)
    resultadoFormatado = float(numero.replace('R$', '').replace('.','').replace(',','.'))
    return resultadoFormatado

def formatarSaidas(n):
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