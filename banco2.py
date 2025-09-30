import os

LIMITE_SAQUES = 3

saldo = 0
saque_max = 500
saques_num = 0
extrato = ""
conta_num = 0
users = []
contas = []

def criar_user():
	cpf = input("Digite o CPF do usuário: ")
	for user in users:
		if user["cpf"] == cpf:
			print("Este CPF já está cadastrado. Tente novamente.")
			return False
	nome = input("Digite o nome do usuário: ")
	nasc = input("Digite a data de nascimento do usuário: ")
	addr = input("Digite o endereço do usuário: ")
	users.append({
		"cpf": cpf,
		"nome": nome,
		"nasc": nasc,
		"addr": addr,
	})
	print("Usuário criado com sucesso.")

def criar_conta():
	global conta_num
	cpf = input("Digite o CPF do usuário: ")
	for user in users:
		if user["cpf"] == cpf:
			conta_num += 1
			contas.append({
				"numero": conta_num,
				"agencia": '0001',
				"cpf": cpf,
			})
			print("Conta criada com sucesso.")
			return True
	print("CPF não registrado. Tente novamente.")

def deposito(val):
	global saldo, extrato
	if val > 0:
		saldo += val
		if extrato: extrato += "\n"
		extrato += f"Depósito: R$ {val:.2f}"
		return True
	print("Valor inválido. Tente novamente")
	return False

def saque(*, val):
	global LIMITE_SAQUES
	global saldo, extrato, saque_max, saques_num
	if saques_num >= LIMITE_SAQUES:
		print("Número máximo de saques excedido.")
	elif val > saldo:
		print("Você não tem saldo suficiente.")
	elif val > saque_max:
		print("O valor do saque excede o limite.")
	elif val <= 0:
		print("O valor informado é inválido.")
	else:
		saldo -= val
		saques_num += 1
		if extrato: extrato += "\n"
		extrato += f"Saque: R$ {val:.2f}"
		return True
	return False

def exibir_extrato(saldo, *, extrato):
	if extrato:
		print(extrato)
	else:
		print("Não foram realizadas movimentações.")
	print(f"Saldo: R$ {saldo:.2f}")

while True:
	os.system('cls' if os.name == 'nt' else 'clear')

	print("0. Sair")
	print("1. Depósito")
	print("2. Saque")
	print("3. Extrato")
	print("4. Criar usuário")
	print("5. Criar conta")

	opcao = input("Digite uma opção: ")

	if opcao == "0":
		break

	elif opcao == "1":
		val = float(input("Valor do depósito: "))
		deposito(val)

	elif opcao == "2":
		val = float(input("Valor do saque: "))
		saque(val=val)

	elif opcao == "3":
		exibir_extrato(saldo, extrato=extrato)

	elif opcao == "4":
		criar_user()

	elif opcao == "5":
		criar_conta()

	else:
		print("Operação inválida.")
	
	input("Pressione qualquer tecla para continuar.")
