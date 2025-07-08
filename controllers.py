import random
from models import voo, cliente, tripulante  

def gerar_clientes(n=100):
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Lucia", "Marcos", "Julia", "Fernando", "Patricia"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Almeida", "Carvalho", "Gomes"]
    
    clientes = []
    for i in range(n):
        nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        cpf = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
        email = f"{nome.lower().replace(' ', '.')}@email.com"
        clientes.append(cliente(nome, cpf, email))
    return clientes

def gerar_tripulantes():
    tripulantes = [
        tripulante("Carlos Alberto", "111.111.111-11", "comandante"),
        tripulante("Roberto Nascimento", "222.222.222-22", "comandante"),
        tripulante("Marcos Silva", "333.333.333-33", "copiloto"),
        tripulante("Ana Paula", "444.444.444-44", "copiloto"),
        tripulante("Ricardo Oliveira", "555.555.555-55", "comissario"),
        tripulante("Fernanda Souza", "666.666.666-66", "comissario"),
    ]
    
    aeromocas = ["Juliana", "Patricia", "Camila", "Amanda", "Beatriz", "Carolina"]
    for i, nome in enumerate(aeromocas):
        tripulantes.append(tripulante(nome, f"777.{i+100}.{i+100}-{i+10}", "aeromoca"))
    
    return tripulantes

def criar_voos():
    origens = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador"]
    destinos = ["Recife", "Fortaleza", "Manaus", "Porto Alegre", "Curitiba"]
    precos = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
    
    voos = []
    for i in range(10):
        numero = 100 + i
        origem = random.choice(origens)
        destino = random.choice([d for d in destinos if d != origem])
        preco = random.choice(precos)
        voos.append(voo(
            numero=numero,
            origem=origem,
            destino=destino,
            horario_partida=f"{random.randint(6, 23)}:{random.randint(0, 59):02d}",
            horario_chegada=f"{random.randint(6, 23)}:{random.randint(0, 59):02d}",
            preco=preco
        ))
    return voos

class sistema_reserva:
    def __init__(self):
        self.voos = []
        self.clientes = gerar_clientes()
        self.tripulantes = gerar_tripulantes()
        self.inicializar()
    
    def inicializar(self):
        self.voos = criar_voos()
        self.distribuir_tripulantes()
        self.reservar_assentos_aleatorios()
    
    def distribuir_tripulantes(self):
        comandantes = [t for t in self.tripulantes if t.cargo == "comandante"]
        copilotos = [t for t in self.tripulantes if t.cargo == "copiloto"]
        comissarios = [t for t in self.tripulantes if t.cargo == "comissario"]
        aeromocas = [t for t in self.tripulantes if t.cargo == "aeromoca"]
        
        for voo in self.voos:
            voo.adicionar_tripulante(random.choice(comandantes))
            voo.adicionar_tripulante(random.choice(copilotos))
            voo.adicionar_tripulante(random.choice(comissarios))
            for _ in range(2):
                voo.adicionar_tripulante(random.choice(aeromocas))
    
    def reservar_assentos_aleatorios(self):
        for voo in self.voos:
            assentos_livres = list(voo.get_assentos_livres().keys())
            assentos_reservar = random.sample(assentos_livres, min(50, len(assentos_livres)))
            
            for assento in assentos_reservar:
                cliente = random.choice(self.clientes)
                voo.reservar_assento(assento, cliente)
    
    def listar_voos(self):
        return self.voos
    
    def get_voo(self, numero):
        for v in self.voos:
            if v.numero == numero:
                return v
        return None