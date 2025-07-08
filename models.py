class pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class cliente(pessoa):
    def __init__(self, nome, cpf, email):
        super().__init__(nome, cpf)
        self.email = email

class tripulante(pessoa):
    cargos = {
        'comandante': 'Comandante',
        'copiloto': 'Copiloto',
        'comissario': 'Comissário',
        'aeromoca': 'Aeromoça'
    }
    
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        if cargo not in self.cargos:
            raise ValueError("Cargo inválido")
        self.cargo = cargo

class voo:
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
            'comandante': None,
            'copiloto': None,
            'comissario': None,
            'aeromocas': []
        }
    
    def reservar_assento(self, assento, cliente):
        if assento not in self.assentos:
            raise ValueError("Assento inválido")
        if self.assentos[assento] is not None:
            raise ValueError("Assento já ocupado")
        self.assentos[assento] = cliente
    
    def adicionar_tripulante(self, tripulante):
        if tripulante.cargo == 'comandante':
            if self.tripulacao['comandante'] is not None:
                raise ValueError("Já existe um comandante neste voo")
            self.tripulacao['comandante'] = tripulante
        elif tripulante.cargo == 'copiloto':
            if self.tripulacao['copiloto'] is not None:
                raise ValueError("Já existe um copiloto neste voo")
            self.tripulacao['copiloto'] = tripulante
        elif tripulante.cargo == 'comissario':
            if self.tripulacao['comissario'] is not None:
                raise ValueError("Já existe um comissário neste voo")
            self.tripulacao['comissario'] = tripulante
        elif tripulante.cargo == 'aeromoca':
            if len(self.tripulacao['aeromocas']) >= 4:
                raise ValueError("Limite de aeromoças atingido")
            self.tripulacao['aeromocas'].append(tripulante)
    
    def get_assentos_ocupados(self):
        return {k: v for k, v in self.assentos.items() if v is not None}
    
    def get_assentos_livres(self):
        return {k: v for k, v in self.assentos.items() if v is None}
    
    def __str__(self):
        return f"Voo {self.numero}: {self.origem} -> {self.destino} (R$ {self.preco:.2f})"