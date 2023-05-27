print('''
Bruno Telles e Andrew Costa
Bem-vindo à lanchonete do Brunin!
Por favor, faça seu pedido:
**************Cardápio************************''')

# Tabela de produtos da lanchonete
produtos = {
    100: {'descricao': 'Cachorro-Quente', 'valor': 9.00},
    101: {'descricao': 'Cachorro-Quente Duplo', 'valor': 11.00},
    102: {'descricao': 'X-Egg', 'valor': 12.00},
    103: {'descricao': 'X-Salada', 'valor': 13.00},
    104: {'descricao': 'X-Bacon', 'valor': 14.00},
    105: {'descricao': 'X-Tudo', 'valor': 17.00},
    200: {'descricao': 'Refrigerante Lata', 'valor': 5.00},
    201: {'descricao': 'Chá Gelado', 'valor': 4.00}
}

# Função para exibir tabela para os clientes
def exibir_tabela():
    print("| Código | Descrição             | Valor(R$) |")
    for codigo, produto in produtos.items():
        print("|{:^8}| {:<21} | {:^9.2f} |".format(codigo, produto['descricao'], produto['valor']))

# Variáveis de controle
total = 0.0
pedido = []
tabela_exibida = False  # Variável de controle para verificar se a tabela já foi exibida

# Loop para realizar os pedidos
while True:
    if not tabela_exibida:  # Verifica se a tabela ainda não foi exibida
        exibir_tabela()
        tabela_exibida = True  # Atualiza a variável de controle

    # Entrada do código do produto para o pedido
    codigo = int(input("Digite o código do produto desejado: "))
    
    # Confere se o código é válido e adiciona o produto ao pedido
    if codigo in produtos:
        pedido.append(produtos[codigo]['descricao'])
        total += produtos[codigo]['valor']
        print("Você escolheu um: {}, no valor de R$ {:.2f} ".format(produtos[codigo]['descricao'], produtos[codigo]['valor']))
        quantidade = int(input("Digite a quantidade que deseja: "))
        total *= quantidade
    
    elif codigo == 0:
        break
    else:
        print("Opção inválida. Por favor, digite um código válido.")
        continue

    # Pergunta se o cliente deseja pedir mais alguma coisa
    print('Você pediu {} de {}'.format(quantidade,produtos[codigo]['descricao'])) 
    continuar = input("Deseja pedir mais alguma coisa? (s/n): ")
    if continuar.lower() == 'n':
        break

# Fechar o pedido
print("\nPedido:")
for item in pedido:
    print(item)
print(f"\nTotal a pagar: R$ {total:.2f}")
print("Brunin Agradece seu pedido !! Volte sempre!")
