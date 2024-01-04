from models.funcionarios import Funcionario
from models.clientes import Cliente
from models.academia import Academia


# 1- basico
# 2- premium
# 3- familia
aluno = Cliente('Lucius', 10, 3)
print(f'{aluno._nome}')


aluno.mostrar_planos()

g1 = Academia()
g1.add_cliente('Lucius')
