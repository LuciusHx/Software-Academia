from models.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, i):
        super().__init__(nome, idade)
        self.planos = ['basico', 'premium', 'familia']
        if 0 <= i < len(self.planos):
            self.plano_escolhido = self.planos[i]
        else:
            raise ValueError("Índice de plano inválido.")

    def mostrar_planos(self):
        print(f'O Plano escolhido foi o {self.plano_escolhido.capitalize()}')


