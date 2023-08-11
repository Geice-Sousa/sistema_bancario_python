# função lista usuário
def lista_usuarios(contas):
    for conta in contas:
        print(f'''\n Agência: {conta['agencia']} \n Conta Corrente: {conta['numero_conta']} \n Titular: {conta['usuario']['nome']}''')

# função verifica cpf
def verifica_usuario(cpf, usuarios):
    if cpf in usuarios:
        return True
    else:
        return usuarios.append(cpf)
    # 11min 

# função cria usuário
def criar_usuario(usuarios):
    cpf = int(input('CPF (apenas nº): '))
    
    usuario = verifica_usuario(cpf, usuarios)
    if usuario:
        print('Este usuário já foi cadastrado, basta fazer o login')
        print('Caso ainda deseje se cadastrar, informe outro CPF.')
        return

    nome = input('Nome e sobrenome: ')
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
    endereco = input('Endereço residencial: ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('*Usuário cadastrado com sucesso!*')

# criar conta: nº da agencia 0001
def cria_conta(agencia, numero_conta, usuarios):
    cpf = int(input('CPF (apenas nº): '))
    usuario = verifica_usuario(cpf, usuarios)
    
    if usuario:
        print('*Conta criada com sucesso!*')
        return {"agencia": agencia, "conta": numero_conta, "usuario": usuario}
    
    print("\n *Usuário não encontrado! Para criar uma conta, primeiro você precisa criar um usuário!* \n")

def opcoes():
    menu = '''
    ========= OPCOES =========

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar usuário
        [5] Criar nova conta
        [6] Lista de contas
        [0] Sair

    ==========================  
    Opcao selecionada => '''

    return input(menu)

# função deposito
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato = ''
        extrato += f'Valor depositado: R${saldo:.2f}.\n'
        print('Depósito realizado com sucesso')
    
    else: 
        print('Houve uma falha no sistema, tente novamente mais tarde.')
    
    return valor, extrato
    
# função saque
def saque(*, saldo, valor, extrato, limite_valor, numero_saques, limite_saques):
    if valor > limite_valor:
        print(f'O saque máximo é {limite_valor}')
            
    elif numero_saques >= limite_saques:
        print(f'Você já excedeu o limite de saques mensal.')  

    elif valor < limite_valor and valor <= saldo and valor > 0 :
        saldo -= valor
        extrato += f'Saque efetuado: R${valor:.2f}.\n'
        numero_saques += 1
        print(f'Seu saque no valor de R${valor:.2f}, foi realizado com sucesso.\n')

    else:
        print(f'Valor solicitado indisponível, seu saldo é R${saldo:.2f}.\n')
    
    return saldo, extrato

# funçao extrato 
def exibe_extrato(saldo, /, *, extrato):
    print(f'**** EXTRATO ****')
    print(extrato)
    print(f'Seu saldo é R${saldo:.2f}')

def main():
    SAQUE_MAXIMO = 500
    LIMITE_SAQUES = 3
    AGENCIA: '0001'
    saldo = 0
    qtd_saques = 0
    extrato = 'Nenhuma operação realizada'
    usuarios = []
    contas = []

    while True:
        opcao = opcoes()

        if opcao == '1':
            valor_depositado = float(input('Informe a quantia que deseja depositar: \n'))
            
            saldo, extrato = deposito(saldo, valor_depositado, extrato)
        
        elif opcao == '2':
            valor_sacado = float(input('Qual a quantia que deseja sacar? '))

            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor_sacado, 
                extrato=extrato, 
                limite_valor=SAQUE_MAXIMO, 
                numero_saques=qtd_saques, 
                limite_saques=LIMITE_SAQUES 
            )       
        
        elif opcao == '3':
            print(exibe_extrato(saldo, extrato=extrato))

        elif opcao == '4': 
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = 2023 + len(contas) + 1
            conta = cria_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == '6':
            print(lista_usuarios(contas))

        elif opcao == '0':
            print('Até mais ver!')
            break
        
        else: 
            print('Digite uma opção válida')

main()