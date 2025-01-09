contante_bonus = 1000
nome_usuario = input("Informe o nome: ")
salario_usuario = float(input("Informe o salário: "))
bonus_usuario = float(input("Digite o valor do seu bônus: "))

bonificacao = contante_bonus + salario_usuario * bonus_usuario

print(f"A bonificação do {nome_usuario} é de : {bonificacao}")