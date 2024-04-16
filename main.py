from codigo.bytebank import Funcionario

#No terminal python -m venv venv cria um ambiente virtual
#.venv\Scripts\activate ativa-o

vitor = Funcionario("Vitor Bittencoourt", "25/01/2000", 1000)

print(vitor.calcular_bonus())
