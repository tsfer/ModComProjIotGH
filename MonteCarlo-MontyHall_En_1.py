import random
def jogo_sempre_troca ():
    portas=[1,2,3]
    porta_carro=random.choice(portas)
    primeira_escolha=random.choice(portas)

    if primeira_escolha == porta_carro:
        return 0

    if primeira_escolha != porta_carro:
        retirar_porta=[1,2,3]

        retirar_porta.remove(porta_carro)
        retirar_porta.remove(primeira_escolha)

        portas.remove(retirar_porta[0])
        portas.remove(primeira_escolha)

        segunda_escolha=portas[0]

    if segunda_escolha == porta_carro:
        return 1
    else:
        return 0

def jogo_nunca_troca ():
    portas=[1,2,3]
    porta_carro=random.choice(portas)
    primeira_escolha=random.choice(portas)

    if primeira_escolha == porta_carro:
        return 1
    else:
        return 0

# Calcular os resultados

vitorias_sempre_troca= 0
vitorias_nunca_troca=0

rodadas=1000000
n_rodadas=rodadas

while n_rodadas>0:
    vitorias_nunca_troca=vitorias_nunca_troca+jogo_nunca_troca()
    vitorias_sempre_troca=vitorias_sempre_troca+jogo_sempre_troca()
    n_rodadas=n_rodadas-1

# Saida

p_vitorias_nunca_troca = (vitorias_nunca_troca*100)/rodadas
p_vitorias_sempre_troca= (vitorias_sempre_troca*100)/rodadas

print('Quando não troca a probabilidade de ganhar é de : ',p_vitorias_nunca_troca , '%')
print('Quando troca a probabilidade de ganhar é de : ', p_vitorias_sempre_troca, '%')