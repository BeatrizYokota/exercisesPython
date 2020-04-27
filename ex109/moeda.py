def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def metade(preço=0, formato=False):
    resp = preço / 2
    return resp if formato is False else moeda(resp)

def dobro(preço=0, formato=False):
    resp = preço * 2
    return resp if formato is False else moeda(resp)

def aumentar(preço=0, taxa=0, formato=False):
    resp = preço + (preço * taxa/100)
    return resp if formato is False else moeda(resp)

def diminuir(preço=0, taxa=0, formato=False):
    resp = preço + (preço * taxa / 100)
    return resp if formato is False else moeda(resp)
