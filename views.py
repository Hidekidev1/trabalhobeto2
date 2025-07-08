import random
from models import voo  

def mostrar_voos(voos):
    print("\nLista de Voos Disponíveis:")
    print("-" * 80)
    print(f"{'Número':<10}{'Origem':<20}{'Destino':<20}{'Partida':<10}{'Chegada':<10}{'Preço':<10}{'Assentos Livres'}")
    print("-" * 80)
    
    for v in voos:
        print(f"{v.numero:<10}{v.origem:<20}{v.destino:<20}{v.horario_partida:<10}{v.horario_chegada:<10}R$ {v.preco:<8}{len(v.get_assentos_livres())}")

def mostrar_detalhes_voo(voo):
    print("\nDetalhes do Voo:")
    print(f"Número: {voo.numero}")
    print(f"Rota: {voo.origem} → {voo.destino}")
    print(f"Horário: {voo.horario_partida} - {voo.horario_chegada}")
    print(f"Preço: R$ {voo.preco:.2f}")
    print(f"Assentos disponíveis: {len(voo.get_assentos_livres())}/250")

def mostrar_tripulacao(tripulacao):
    print("\nTripulação do Voo:")
    print(f"Comandante: {tripulacao['comandante'].nome}")
    print(f"Copiloto: {tripulacao['copiloto'].nome}")
    print(f"Comissário: {tripulacao['comissario'].nome}")
    print("\nAeromoças:")
    for a in tripulacao['aeromocas']:
        print(f"- {a.nome}")

def mostrar_assentos_ocupados(voo, quantidade=10):
    assentos = voo.get_assentos_ocupados()
    if not assentos:
        print("\nNenhum assento ocupado neste voo.")
        return
    
    sample = random.sample(list(assentos.items()), min(quantidade, len(assentos)))
    
    print(f"\nAmostra de {len(sample)} assentos ocupados (de {len(assentos)}):")
    print("-" * 60)
    print(f"{'Assento':<10}{'Passageiro':<30}{'CPF'}")
    print("-" * 60)
    for assento, cliente in sample:
        print(f"{assento:<10}{cliente.nome:<30}{cliente.cpf}")