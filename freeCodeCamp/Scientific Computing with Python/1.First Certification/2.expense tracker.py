# Definindo função de add de gastos (gastos, valor, categoria)
def adicionar_despesa(despesas, nome, valor, categoria):
    despesas.append({'nome': nome, 'valor': valor, 'categoria': categoria})                       # Adiciona o valor e a categoria no último índice do dicionário 'despesas'
# Definindo função para imprimir despesas    
def listar_despesas(despesas):
    for despesa in despesas:
        print(f'Despesa: {despesa["nome"]} Valor: {despesa["valor"]} Categoria: {despesa["categoria"]}')
# Definindo função para somar as despesas
def total_despesas(despesas):
    return sum(map(lambda despesa: despesa['valor'], despesas))                     # lambda() é uma função breve e anonima, map(função, lista) opera a função para cada valor da lista, sum() soma
# Definindo função para filtrar despesas
def filtrar_despesas_por_categoria(despesas, categoria):
    return filter(lambda despesa: despesa['categoria'] == categoria, despesas)
    

def main():
    despesas = []
    while True:
        print('\nRastreador de Despesas')
        print('1. Adicionar uma despesa')
        print('2. Listar todas as despesas')
        print('3. Mostrar total de despesas')
        print('4. Filtrar despesas por categoria')
        print('5. Sair')
       
        escolha = input('Digite sua escolha: ')

        if escolha == '1':
            nome = input('Digite a despesa: ')
            valor = float(input('Digite o valor: '))
            categoria = input('Digite a categoria: ')
            adicionar_despesa(despesas, nome, valor, categoria)
        elif escolha == '2':
            if len(despesas) == 0:
                print('\nNão existem despesas registradas.')
            else:
                print('\nTodas as Despesas:')
                listar_despesas(despesas)
        elif escolha == '3':
            print('\nTotal de Despesas: ', total_despesas(despesas))
        elif escolha == '4':
            categoria = input('Digite a categoria para filtrar: ')
            print(f'\nDespesas para {categoria}:')
            despesas_da_categoria = filtrar_despesas_por_categoria(despesas, categoria)
            listar_despesas(despesas_da_categoria)
        elif escolha == '5':
            print('Saindo do programa.')
            break

main()