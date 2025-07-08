from prettytable import PrettyTable
import random

class VooView:
    @staticmethod
    def mostrar_voos(voos):
        table = PrettyTable()
        table.field_names = ["Número", "Origem", "Destino", "Partida", "Chegada", "Preço (R$)", "Assentos Livres"]
        
        for voo in voos:
            table.add_row([
                voo.numero,
                voo.origem,
                voo.destino,
                voo.horario_partida,
                voo.horario_chegada,
                f"{voo.preco:.2f}",
                len(voo.get_assentos_livres())
            ])
        
        print("\nLista de Voos Disponíveis:")
        print(table)
    
    @staticmethod
    def mostrar_detalhes_voo(voo):
        print("\nDetalhes do Voo:")
        print(f"Número: {voo.numero}")
        print(f"Origem: {voo.origem} -> Destino: {voo.destino}")
        print(f"Horário: Partida {voo.horario_partida} - Chegada {voo.horario_chegada}")
        print(f"Preço: R$ {voo.preco:.2f}")
        print(f"Assentos disponíveis: {len(voo.get_assentos_livres())}/250")
    
    @staticmethod
    def mostrar_tripulacao(tripulacao):
        print("\nTripulação do Voo:")
        print(f"Comandante: {tripulacao['COMANDANTE'].nome}")
        print(f"Copiloto: {tripulacao['COPILOTO'].nome}")
        print(f"Comissário: {tripulacao['COMISSARIO'].nome}")
        print("\nAeromoças:")
        for aeromoca in tripulacao['AEROMOCAS']:
            print(f"- {aeromoca.nome}")
    
    @staticmethod
    def mostrar_assentos_ocupados(voo, quantidade=10):
        assentos_ocupados = voo.get_assentos_ocupados()
        if not assentos_ocupados:
            print("\nNenhum assento ocupado neste voo.")
            return
        

        sample_size = min(quantidade, len(assentos_ocupados))
        assentos_amostra = random.sample(list(assentos_ocupados.items()), sample_size)
        
        table = PrettyTable()
        table.field_names = ["Assento", "Nome do Passageiro", "CPF"]
        
        for assento, cliente in assentos_amostra:
            table.add_row([assento, cliente.nome, cliente.cpf])
        
        print(f"\nAmostra de {sample_size} assentos ocupados (de {len(assentos_ocupados)}):")
        print(table)