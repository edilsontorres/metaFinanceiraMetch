from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

@csrf_exempt
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
    numero = f'R${n:_.2f}'
    resultado = numero.replace('.', ',').replace('_', '.')
    return resultado

def formatarResultado(resultado):
    resultadoObtido = resultado // 12
    resto = resultado % 12
    
    if(resultado > 12 and resto):
        if(resultadoObtido == 1 and resto <= 1):
            return f'{round(resultadoObtido)} ano e {(resto)} mês'
        
        if(resultadoObtido > 1 and resto <= 1):
            return f'{round(resultadoObtido)} anos e {(resto)} mês'
        
        if(resultadoObtido == 1 and resto > 1):
            return f'{round(resultadoObtido)} ano e {(resto)} meses'
        
        return f'{round(resultadoObtido)} anos e {(resto)} meses'
    
    elif(resultado == 1):
        return f'{resultado} mês'
    
    else:
        return f'{resultado} meses'
    