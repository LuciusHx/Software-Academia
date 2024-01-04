

class Academia:
    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.equipamentos = []
        self.treinos = []


# -------------- CLIENTES ----------------

     
    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def remove_cliente(self, cliente):
        self.clientes.remove(cliente)

    # listar clientes
    def __str__(self):
        for clientes in self.clientes:
            return f'{clientes}'


# --------------- TREINOS ---------------------

    def add_treino(self, treino):
        self.treinos.append(treino)

    # listar horários de treinos disponíveis
    @property
    def listar_horarios(self, total):
        total = len(self.treinos)
        if total == 0:
            print('Há horários disponíveis.')
        else:
            print('não há horários disponíveis.')
        


# --------------- FUNCIONARIOS --------------
