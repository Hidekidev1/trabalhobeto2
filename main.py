from voos.controllers import SistemaReserva
from voos.views import VooView
import random

def main():
    sistema = SistemaReserva()
    
    while True:
        print("\nSistema de Reserva de Voos")
        print("1. Listar todos os voos")
        print("2. Ver detalhes de um voo")
        print("3. Ver tripulação de um voo")
        print("4. Ver assentos ocupados de um voo")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            voos = sistema.listar_voos()
            VooView.mostrar_voos(voos)
        
        elif opcao == "2":
            numero_voo = int(input("Digite o número do voo (3 dígitos): "))
            voo = sistema.get_voo_por_numero(numero_voo)
            if voo:
                VooView.mostrar_detalhes_voo(voo)
            else:
                print("Voo não encontrado!")
        
        elif opcao == "3":
            numero_voo = int(input("Digite o número do voo (3 dígitos): "))
            tripulacao = sistema.get_tripulacao_voo(numero_voo)
            if tripulacao:
                VooView.mostrar_tripulacao(tripulacao)
            else:
                print("Voo não encontrado!")
        
        elif opcao == "4":
            numero_voo = int(input("Digite o número do voo (3 dígitos): "))
            voo = sistema.get_voo_por_numero(numero_voo)
            if voo:
                VooView.mostrar_assentos_ocupados(voo)
            else:
                print("Voo não encontrado!")
        
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()