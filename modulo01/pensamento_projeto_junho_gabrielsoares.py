'''
Um Bloco de Comentarios. 
Para explicar o que o código faz, ou para deixar anotações para o programador.
>>projeto açaiteria:

>PO (Como dono do negocio: Quero um sistema de vendas para minha açaiteria, 
para que eu possa controlar as vendas e os produtos.)

>QA (Como cliente: Quero um sistema de vendas para minha açaiteria,
para que eu possa comprar meus produtos favoritos de forma rápida e fácil.)

>Tech (Como programador: Quero um sistema de vendas para minha açaiteria,
para que eu possa desenvolver um software eficiente e funcional para o negócio.)

>Dev (Como programador: Quero um sistema de vendas para minha açaiteria,
para que eu possa implementar as funcionalidades necessárias para 
atender as necessidades do negócio e dos clientes.)

>UX (Como designer de experiência do usuário: Quero um sistema de 
vendas para minha açaiteria,para que eu possa criar uma 
interface intuitiva e agradável para os usuários, 
garantindo uma experiência de compra satisfatória.)

>IA (Como analista de dados: Quero um sistema de vendas para minha 
açaiteria, para que eu possa coletar e analisar os dados de vendas, 
ajudando a identificar padrões de consumo e otimizar as 
estratégias de marketing e estoque.)


Ciclo de vida do projeto:
1. Planejamento: Definir os requisitos do sistema, identificar as necessidades do negócio e dos clientes, 
e criar um plano de desenvolvimento.
2. Análise: Analisar os requisitos e criar um modelo de dados e um design de sistema.
3. Desenvolvimento: Escrever o código para implementar as funcionalidades do sistema.
4. Testes: Testar o sistema para garantir que ele funcione corretamente e atenda aos requisitos.
5. Implantação: Implantar o sistema em um ambiente de produção e garantir que ele esteja funcionando 
corretamente.
6. Manutenção: Realizar manutenção contínua para corrigir bugs, adicionar novas funcionalidades e garantir 
que o sistema continue atendendo às necessidades do negócio e dos clientes.

>>Criar um aplicativo, sistema em CLI - Command Line Interface, ou seja, um sistema que funcione no terminal, sem interface gráfica.
>>Complementar e implementar o app / sistema em GUI - Graphical User Interface, ou seja, um sistema com interface gráfica, 
para que os usuários possam interagir de forma mais intuitiva e agradável.

'''
# Inicializando as variáveis para o Produto 1 (vazio)
p1_nome = "T-Cross"
p1_estoque = 27
p1_preco = 100.000
p1_marca = "Volkswagen"
p1_cores = "Azul, vermelho, preto cinza e branco"

# Inicializando as variáveis para o Produto 2 (vazio)
p2_nome = "Argo"
p2_estoque = 13
p2_preco = 60.000
p2_marca = "Fiat"
p2_cores = "preto, branco, cinza e amarelo"

# Inicializando as variáveis para o Produto 3 (vazio)
p3_nome = "Onix"
p3_estoque = 19
p3_preco = 86.000
p3_marca = "Chevrolet"
p3_cores = "amarelo, verde, preto e cinza"

# Inicializando as variáveis para o Produto 4 (vazio)
p4_nome = "HB20"
p4_estoque = 23
p4_preco = 95.000
p4_marca = "Hyundai"
p4_cores = "azul, branco, preto e cinza"

# Inicializando as variáveis para o Produto 5 (vazio)
p5_nome = "Corolla"
p5_estoque = 29
p5_preco = 170.000
p5_marca = "Toyota"
p5_cores = "amarelo, verde, preto e cinza"

# Isso é um comentário de linha única.

while True: 
    print('-' * 48 + '\n')
    print('Bem-vindo ao Sistema de vendas - açaiteria!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar venda')
    print('0 - Sair')
    print('\n--------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')
    # faça a lógica para cadastrar o produto aqui, 
    ## e somente a inseção dos dados usando input e os tipos de dados.
        if p1_nome == "":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_marca = input('Digite a marca do produto: ')    
            p1_cores = input('Digite as cores disponiveis do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')           
        elif p2_nome == "":
                p2_nome = input('Digite o nome do produto: ')
                p2_estoque = int(input('Digite a quantidade em estoque: '))
                p2_preco = float(input('Digite o preço do produto: '))
                p2_marca = input('Digite a marca do produto: ')    
                p2_cores = input('Digite as cores disponiveis do produto: ')
                print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
        elif p3_nome == "":
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_marca = input('Digite a validade do produto: ')    
            p3_cores = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')

        elif p4_nome == "":
                p4_nome = input('Digite o nome do produto: ')
                p4_estoque = int(input('Digite a quantidade em estoque: '))
                p4_preco = float(input('Digite o preço do produto: '))
                p4_marca = input('Digite a marca do produto: ')    
                p4_cores = input('Digite as cores disponiveis do produto: ')
                print(f'\n🎉 Produto "{p4_nome}" cadastrado na vaga 2!')

        elif p5_nome == "":
                p5_nome = input('Digite o nome do produto: ')
                p5_estoque = int(input('Digite a quantidade em estoque: '))
                p5_preco = float(input('Digite o preço do produto: '))
                p5_marca = input('Digite a marca do produto: ')    
                p5_cores = input('Digite as cores disponiveis do produto: ')
                print(f'\n🎉 Produto "{p5_nome}" cadastrado na vaga 2!')
            
        else:
            print('❌ Sistema cheio! Limite de 5 produtos atingido.')

    elif opcao == '2':
        print('Listando produtos...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":

            print('Nenhum produto cadastrado no sistema ainda.')

        else:
            # Mostra o Produto 1 se ele existir
            if p1_nome != "":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")

                print(f"Marca: {p1_marca} | Cores: {p1_cores}")

                print('🔥' * 30)
                
            # Mostra o Produto 2 se ele existir
            if p2_nome != "":

                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")

                print(f"Marca: {p2_marca} | Cores: {p2_cores}")

                print('🔥' * 30)
                
            # Mostra o Produto 3 se ele existir
            if p3_nome != "":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Marca: {p3_marca} | Cores: {p3_cores}")

                print('🔥' * 30)

    elif opcao == '3':
        print('Realizando venda...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print(f'Não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('🔥 Erro: Produto não encontrado!')

    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')