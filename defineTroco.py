import math

def calculaTroco(valor,pagamento):


    valorFloat = float(valor)
    pagamentoFloat = float(pagamento)
    troco = []


    devendoCompleto = pagamentoFloat - valorFloat


    print(f"O valor total a ser entregue de troco é: {devendoCompleto}")


    indice = str(devendoCompleto).find(".")


    if indice != -1:#confere se tem ponto
        
        centavos = int(str(devendoCompleto)[indice + 1:])# Mantém apenas a parte da string após o ponto
        devendo = int(str(devendoCompleto)[:indice])# Mantém apenas a parte da string até o ponto

    else:
        devendo = devendoCompleto

    if len(str(centavos)) == 1:#se o centavo estiver com 1 digito só ele adiciona o zero do lado
        centavos = centavos * 10
    else:
        centavos = math.ceil(centavos / 5) * 5#arredonda o numero para o proximo numero terminado em 5 ou 0, sempre pra cima

    print(devendo)
    print(centavos)


    while devendo > 0:
        if devendo >= 100:
            troco.append('cedulas/nota100.jpeg')
            devendo = devendo - 100
        elif devendo >= 50:
            troco.append('cedulas/nota50.jpeg')
            devendo = devendo - 50
        elif devendo >= 20:
            troco.append('cedulas/nota20.jpeg')
            devendo = devendo - 20
        elif devendo >= 10:
            troco.append('cedulas/nota10.jpeg')
            devendo = devendo - 10
        elif devendo >= 5:
            troco.append('cedulas/nota5.jpeg')
            devendo = devendo - 5
        elif devendo >= 2:
            troco.append('cedulas/nota2.jpeg')
            devendo = devendo - 2
        elif devendo >= 1:
            troco.append('moedas/1real.png')
            devendo = devendo - 1
        
        #print(f"O caixa ainda deve {devendo}")

    while centavos > 0:
        if centavos >= 50:
            troco.append('moedas/50cents.png')
            centavos = centavos - 50
        elif centavos >= 25:
            troco.append('moedas/25cents.png')
            centavos = centavos - 25
        elif centavos >= 10:
            troco.append('moedas/10cents.png')
            centavos = centavos - 10
        elif centavos >= 5:
            troco.append('moedas/5cents.png')
            centavos = centavos - 5
        
        #print(f"O caixa ainda deve {centavos}")



    return(troco)

