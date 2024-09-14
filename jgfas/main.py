repositorio = [
    {'Codigo': 1,
     'Autor': 'dostoievisk',
     'Titulo': 'subsolo',
     'Preco': 100,
     'Disponivel': True
     }
]

codigo = 1

while True:
    print('----BEM VINDO, SEU BAITOLA-----')
    print('1 - Cadastrar livro')
    print('2 - Listar livros')
    print('3 - Editar livros')
    print('4 - Remover livros')
    print('5 - SAIR')
    opcao = input('Selecione uma opção: ')
    if opcao == '1':
        titulo = input('Informe o titulo do livro: ')
        autor = input('Informe o autor do livro: ')
        preco= float(input('Informe o preço do livro: '))
        codigo += 1
        livro = {
            'Codigo': codigo,
            'Autor':autor,
            'Titulo':titulo,
            'Preco' : preco,
            'Disponivel' : True   
        }
        print('Livro cadastrado com sucesso')
        print(repositorio)
    elif opcao == '2':
        for livro in repositorio:
            print(f"Codigo: {livro['Codigo']}")
            print(f"Titulo: {livro['Titulo']}")
            print(f"Autor: {livro['Autor']}")
            print(f"Preco: {livro['Preco']}")
            print(f"Disponivel: {livro['Disponivel']}")
            print('-'*50)
    elif opcao == '3':
        codigo = int(input('informe o codigo do livro: '))
        for livro in repositorio:
            if livro ['Codigo'] == codigo:
                livro['Titulo'] = input('Digite o titulo: ')
                livro['Autor'] = input('Digite o nome do autor: ')
                livro['Preco'] = input('Digite o preço: ')
                print('Dados alterados com sucesso!')
                break   
    elif opcao == '4':
         codigo = int(input('informe o codigo do livro: '))
         for livro in repositorio:
             if livro['Codigo'] == codigo:
                 repositorio.remove(livro)
                 print('Livro removido com sucesso!')
                 break
         else:
             print('Livro nao encontrado')
    elif opcao == '5':
        print("------FIM------")
        break