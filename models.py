class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, nome, cpf, email):
        super().__init__(nome, cpf)
        self.email = email

class Tripulante(Pessoa):
    CARGO_CHOICES = {
        'COMANDANTE': 'Comandante',
        'COPILOTO': 'Copiloto',
        'COMISSARIO': 'Comissário',
        'AEROMOCA': 'Aeromoça'
    }
    
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        if cargo not in self.CARGO_CHOICES:
            raise ValueError("Cargo inválido")
        self.cargo = cargo

class Voo:
    def __init__(self, numero, origem, destino, horario_partida, horario_chegada, preco):
        if not (100 <= numero <= 999):
            raise ValueError("Número do voo deve ter 3 dígitos")
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.horario_partida = horario_partida
        self.horario_chegada = horario_chegada
        self.preco = preco
        self.assentos = {i: None for i in range(1, 251)}  
        self.tripulacao = {
            'COMANDANTE': None,
            'COPILOTO': None,
            'COMISSARIO': None,
            'AEROMOCAS': []
        }
    
    def reservar_assento(self, assento, cliente):
        if assento not in self.assentos:
            raise ValueError("Assento inválido")
        if self.assentos[assento] is not None:
            raise ValueError("Assento já ocupado")
        self.assentos[assento] = cliente
    
    def adicionar_tripulante(self, tripulante):
        if tripulante.cargo == 'COMANDANTE':
            if self.tripulacao['COMANDANTE'] is not None:
                raise ValueError("Já existe um comandante neste voo")
            self.tripulacao['COMANDANTE'] = tripulante
        elif tripulante.cargo == 'COPILOTO':
            if self.tripulacao['COPILOTO'] is not None:
                raise ValueError("Já existe um copiloto neste voo")
            self.tripulacao['COPILOTO'] = tripulante
        elif tripulante.cargo == 'COMISSARIO':
            if self.tripulacao['COMISSARIO'] is not None:
                raise ValueError("Já existe um comissário neste voo")
            self.tripulacao['COMISSARIO'] = tripulante
        elif tripulante.cargo == 'AEROMOCA':
            if len(self.tripulacao['AEROMOCAS']) >= 4:  
                raise ValueError("Limite de aeromoças atingido")
            self.tripulacao['AEROMOCAS'].append(tripulante)
        else:
            raise ValueError("Cargo inválido")
    
    def get_assentos_ocupados(self):
        return {k: v for k, v in self.assentos.items() if v is not None}
    
    def get_assentos_livres(self):
        return {k: v for k, v in self.assentos.items() if v is None}
    
    def __str__(self):
        return f"Voo {self.numero}: {self.origem} -> {self.destino} (R$ {self.preco:.2f})"