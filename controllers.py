from .models import Voo, Cliente, Tripulante
from .data import gerar_clientes, gerar_tripulantes, criar_voos
import random

class SistemaReserva:
    def __init__(self):
        self.voos = []
        self.clientes = gerar_clientes()
        self.tripulantes = gerar_tripulantes()
        self.criar_voos_iniciais()
        self.popular_voos()
    
    def criar_voos_iniciais(self):
        self.voos = criar_voos()
    
    def popular_voos(self):
        comandantes = [t for t in self.tripulantes if t.cargo == "COMANDANTE"]
        copilotos = [t for t in self.tripulantes if t.cargo == "COPILOTO"]
        comissarios = [t for t in self.tripulantes if t.cargo == "COMISSARIO"]
        aeromocas = [t for t in self.tripulantes if t.cargo == "AEROMOCA"]
        
        for voo in self.voos:
            
            voo.adicionar_tripulante(random.choice(comandantes))
            voo.adicionar_tripulante(random.choice(copilotos))
            voo.adicionar_tripulante(random.choice(comissarios))
            for _ in range(2):
                voo.adicionar_tripulante(random.choice(aeromocas))
            
    
            assentos_livres = list(voo.get_assentos_livres().keys())
            assentos_reservar = random.sample(assentos_livres, min(50, len(assentos_livres)))
            
            for assento in assentos_reservar:
                cliente = random.choice(self.clientes)
                voo.reservar_assento(assento, cliente)
    
    def listar_voos(self):
        return self.voos
    
    def get_voo_por_numero(self, numero):
        for voo in self.voos:
            if voo.numero == numero:
                return voo
        return None
    
    def reservar_voo(self, numero_voo, assento, cliente):
        voo = self.get_voo_por_numero(numero_voo)
        if not voo:
            raise ValueError("Voo não encontrado")
        voo.reservar_assento(assento, cliente)
        return True
    
    def get_tripulacao_voo(self, numero_voo):
        voo = self.get_voo_por_numero(numero_voo)
        if not voo:
            raise ValueError("Voo não encontrado")
        return voo.tripulacao
    
    def get_assentos_ocupados(self, numero_voo):
        voo = self.get_voo_por_numero(numero_voo)
        if not voo:
            raise ValueError("Voo não encontrado")
        return voo.get_assentos_ocupados()
    
    def get_assentos_livres(self, numero_voo):
        voo = self.get_voo_por_numero(numero_voo)
        if not voo:
            raise ValueError("Voo não encontrado")
        return voo.get_assentos_livres()