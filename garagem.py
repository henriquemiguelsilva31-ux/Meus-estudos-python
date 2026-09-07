garagem = []
print("Vamos criar sua garagem! (quando for colocar sua resposta dê um espaço depois de escrever, senão a resposta não aparece)")
primeiro_carro=input("digite seu primeiro carro: ")
garagem.append(primeiro_carro)
print("sua garagem tem:", garagem)

while True:
	opcao=input("quer adicionar ou retirar mais algum carro da sua garagem? ").strip().lower()
	
	if opcao=="sim" or opcao=="quero" or opcao=="adicionar":
		novo_carro=input("qual carro a mais você quer adicionar? ")
		garagem.append(novo_carro)
		print(" sua garagem agora tem:", garagem)
	
	elif opcao=="quero tirar" or opcao=="remover" or opcao=="tirar" or opcao=="retirar":
		carro_remover=input("qual carro você quer remover? ")
		garagem.remove(carro_remover)
		print("sua garagem agora tem:", garagem)
	
	elif opcao=="não" or opcao=="nao" or opcao=="sair" or opcao=="fim":
		print(" programa encerrado! Sua garagem agora tem:", garagem)
		break
	else:
		print("Opção inválida! Digite algo como 'adicionar', 'retirar', 'fim'")
		