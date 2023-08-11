# criar funções para cada opção
# 1. função saque: apenas argumentos nomeados, parâmetros: saldo, valor, extrato, limite, numero_saques, limite_saques; retornar saldo e extrato


# 3. extrato ambos args, args pos sado, ars nom extrato

# 4. criar usuário: usauários armazenados em uma lista, possui: nome, data_de_nascimento, CPF, endereco: {logradouro, nro, bairro, cidade/est}
# cada cpf deve ser cadatrado uma única vez e apenas números

# 5. criar conta: nº da agencia 0001


def opcoes():
    menu = '''
    ========= OPCOES =========

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

    ==========================  
    Opcao selecionada => '''

    return input(menu)

#função deposito

def deposito(saldo, valor, extrato, /):
          
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f'Valor depositado: R${saldo:.2f}.\n'
        print('Depósito realizado com sucesso')
        return valor, extrato
      
    else: 
        print('Houve uma falha no sistema, tente novamente mais tarde.')
    

# 1. função saque: apenas argumentos nomeados, parâmetros: saldo, valor, extrato, limite, numero_saques, limite_saques; retornar saldo e extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    return saldo, extrato

saldo = 0
SAQUE_MAXIMO = 500
qtd_saques = 0
LIMITE_SAQUES = 3
extrato = ''
deposito = 0

while True:
    opcao = opcoes()

    if opcao == '1':
        valor_depositado = float(input('Informe a quantia que deseja depositar: \n'))
        
        saldo, extrato = deposito(saldo, valor_depositado, extrato)
      
    elif opcao == '2':

        valor_sacado = float(input('Qual a quantia que deseja sacar? '))

       
    
    elif opcao == '3':
        print('\n *** EXTRATO ***')
        print(extrato)
        print(f'''Seu saldo é R${saldo:.2f}.
        ''')
        # Você ainda pode fazer {qtd_saques} saques esse mês.

    elif opcao == '0':
        print('Até mais ver!')
        break
    
    else: 
        print('Digite uma opção válida')