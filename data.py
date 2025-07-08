from random import randint, choice
from .models import Voo, Cliente, Tripulante

def gerar_clientes(n=100):
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Lucia", "Marcos", "Julia", "Fernando", "Patricia"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Almeida", "Carvalho", "Gomes"]
    
    clientes = []
    for i in range(n):
        nome = f"{choice(nomes)} {choice(sobrenomes)}"
        cpf = f"{randint(100, 999)}.{randint(100, 999)}.{randint(100, 999)}-{randint(10, 99)}"
        email = f"{nome.lower().replace(' ', '.')}@email.com"
        clientes.append(Cliente(nome, cpf, email))
    return clientes

def gerar_tripulantes():
    tripulantes = [
        Tripulante("Carlos Alberto", "111.111.111-11", "COMANDANTE"),
        Tripulante("Roberto Nascimento", "222.222.222-22", "COMANDANTE"),
        Tripulante("Marcos Silva", "333.333.333-33", "COPILOTO"),
        Tripulante("Ana Paula", "444.444.444-44", "COPILOTO"),
        Tripulante("Ricardo Oliveira", "555.555.555-55", "COMISSARIO"),
        Tripulante("Fernanda Souza", "666.666.666-66", "COMISSARIO"),
    ]
    
    aeromocas = ["Juliana", "Patricia", "Camila", "Amanda", "Beatriz", "Carolina"]
    for i, nome in enumerate(aeromocas):
        tripulantes.append(Tripulante(nome, f"777.{i+100}.{i+100}-{i+10}", "AEROMOCA"))
    
    return tripulantes

def criar_voos():
    origens = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador"]
    destinos = ["Recife", "Fortaleza", "Manaus", "Porto Alegre", "Curitiba"]
    precos = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
    
    voos = []
    for i in range(10):
        numero = 100 + i
        origem = choice(origens)
        destino = choice([d for d in destinos if d != origem])
        preco = choice(precos)
        voo = Voo(
            numero=numero,
            origem=origem,
            destino=destino,
            horario_partida=f"{randint(6, 23)}:{randint(0, 59):02d}",
            horario_chegada=f"{randint(6, 23)}:{randint(0, 59):02d}",
            preco=preco
        )
        voos.append(voo)
    return voos