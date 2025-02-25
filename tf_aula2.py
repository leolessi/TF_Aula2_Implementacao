produtos = {}
continuar = 0

while continuar != 4:
    print("\n1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar")
    print("4 - Sair\n")
    continuar = int(input("Digite a opção desejada: "))
    if continuar == 1:
        nome = input("Digite o nome do produto: ")
        preco = int(input("Digite o preco: "))
        quantidade = int(input("Digite a quantidade: "))
        produtos[nome] = (preco, quantidade)
    elif continuar == 2:
        nome = input("Digite o nome que deseja excluir: ")
        if nome in produtos:
            del produtos[nome]
        else:
            print("Produto não encontrado.\n")
    elif continuar == 3:
        for nome, (preco, quantidade) in produtos.items():
            print(f"Produto: {nome}, Preço: {preco}, Quantidade: {quantidade}")
    elif continuar == 4:
        print("Saindo...")
    else:
        print("Opção inválida")
