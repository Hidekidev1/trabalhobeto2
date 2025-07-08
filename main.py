from controllers import sistema_reserva
from views import (
    mostrar_voos,
    mostrar_detalhes_voo,
    mostrar_tripulacao,
    mostrar_assentos_ocupados
)

def main():
    sistema = sistema_reserva()
    
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
            mostrar_voos(voos)
        
        elif opcao == "2":
            try:
                numero = int(input("Digite o número do voo (3 dígitos): "))
                voo = sistema.get_voo(numero)
                if voo:
                    mostrar_detalhes_voo(voo)
                else:
                    print("Voo não encontrado!")
            except ValueError:
                print("Número inválido!")
        
        elif opcao == "3":
            try:
                numero = int(input("Digite o número do voo (3 dígitos): "))
                voo = sistema.get_voo(numero)
                if voo:
                    mostrar_tripulacao(voo.tripulacao)
                else:
                    print("Voo não encontrado!")
            except ValueError:
                print("Número inválido!")
        
        elif opcao == "4":
            try:
                numero = int(input("Digite o número do voo (3 dígitos): "))
                voo = sistema.get_voo(numero)
                if voo:
                    mostrar_assentos_ocupados(voo)
                else:
                    print("Voo não encontrado!")
            except ValueError:
                print("Número inválido!")
        
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()