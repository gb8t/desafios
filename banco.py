import os

LIMITE_SAQUES = 3

saldo = 0

saque_max = 500
saques_num = 0

extrato = ""

while True:
	os.system('cls' if os.name == 'nt' else 'clear')

	print("0. Sair")
	print("1. Depósito")
	print("2. Saque")
	print("3. Extrato")

	opcao = input("Digite uma opção: ")

	if opcao == "0":
		break

	elif opcao == "1":
		val = float(input("Valor do depósito: "))
		if val > 0:
			saldo += val
			if extrato: extrato += "\n"
			extrato += f"Depósito: R$ {val:.2f}"
		else:
			print("Valor inválido. Tente novamente")

	elif opcao == "2":
		val = float(input("Valor do saque: "))

		if saques_num >= LIMITE_SAQUES:
			print("Número máximo de saques excedido.")
		elif val > saldo:
			print("Você não tem saldo suficiente.")
		elif val > saque_max:
			print("O valor do saque excede o limite.")
		elif val > 0:
			saldo -= val
			if extrato: extrato += "\n"
			extrato += f"Saque: R$ {val:.2f}"
			saques_num += 1
		else:
			print("O valor informado é inválido.")

	elif opcao == "3":
		if extrato:
			print(extrato)
		else:
			print("Não foram realizadas movimentações.")
		print(f"Saldo: R$ {saldo:.2f}")

	else:
		print("Operação inválida.")
	
	input("Pressione qualquer tecla para continuar.")
