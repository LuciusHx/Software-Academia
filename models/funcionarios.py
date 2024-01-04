from models.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade, cargo)
        self.cargo = cargo
