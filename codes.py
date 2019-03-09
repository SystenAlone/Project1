def clear:
    print("\n" * 100)

class conta:
    def __init__ (self):
        #atributos
        self.numero = None
        self.titular = None
        self.senha = None
        self.saldo = 0
        

    #método depositar
    def depositar (self):
        valorDepositado = int(input("Digite o valor a ser depositado: "))
        self.saldo += valorDepositado
        print("\naguarde um instante...") 
        tempo()
        print("Operação realizada com sucesso.")
        self.mostrarSaldo()
        

    def sacar(self):
        #n tá indo, arrumar depois
        
        self.valorSac = int(input("digite o valor a ser sacado: "))
        if self.valorSac <= self.saldo:
            verificar = int(input("digite a sua senha: "))
            if verificar == self.senha:
                print("\naguarde um instante...") 
                tempo()
                print("Saque realizado com sucesso, retire o dinheiro.")
                self.saldo -= self.valorSac
                print("\nSeu saldo é de: R$", self.saldo)
            else:
                print("senha errada! Operação cancelada.")
        else:
            print("\naguarde um instante...") 
            tempo()
            print("Erro de operação, saldo insuficiênte. Verifique seu saldo e tente novamente.")

    #método mostrar saldo
    def mostrarSaldo(self):
        print("\naguarde um instante...") 
        tempo()
        print("Saldo atual: ",self.saldo)

    #método mostrar informações da conta
    def verInfo(self):
        print("\naguarde um instante...") 
        tempo()
        print("Usuário: ", self.titular)
        print("Número bancário: ", self.numero)
        print("\nSeu saldo é de: R$", self.saldo)

    #metodo alterar senha
    def alterarSenha(self):
        print("Deseja trocar a senha? Não se preocupe Sr. ", self.titular, " pois nós o ajuaremos")
        senhaAtual = int(input ("Digite a senha antiga: "))
        if senhaAtual == self.senha:
            novaSenha = int(input("Digite a nova senha: "))
            self.senha = novaSenha
            print("\naguarde um instante...") 
            tempo()
            print("senha alterada com sucesso.")
        else:
            print("\naguarde um instante...") 
            tempo()
            print("Senha incorreta. Assim você nos quebra né amigo")

#classe conta corrente
class corrente (conta):
    def pagarBoleto(self):
        valorBoleto = float(input("Digite o valor do boleto: "))
        if valorBoleto <= self.saldo:
            verificar = int(input("digite a sua senha: "))
            if verificar == self.senha:
                self.saldo -= valorBoleto
                print("Pagamento realizado com sucesso!")
                print("Seu saldo atual é de: R$", self.saldo)
            else:
                print("Erro de operação, tente novamente mais tarde após algum depósito")

class poupanca (conta):
    #não criei um construtor, pois usaremos o contrutor da classe pai

    #método adicionar rendimento (única difença da classe poupanca para a classe
    def adicionarRendimento(self):
        #incrementa o saldo em meio por cento
        self.saldo += self.saldo*0.005
        print ("Rendimento adicionado com sucesso. Mais uns 50 anos e vc vai ser rico.")
        self.mostrarSaldo()
#===============================================================================
#lista de contas, que funcionará como nosso "banco de dados"
contas = []


import time

def tempo():
    time.sleep(3)  
#aquele velho loop que faz o programa rodar...
while True:
    
    #mostra as opções  
    
    print("\nDoug Banking - Nosso lema é 'dinhiro é igual a um bis, por isso eu vou pegar o seu.'")
    print()
    print("1_ Criar nova conta")
    print("2_ Realizar Operações em contas")
    print("3_ Mostrar lista de usuários")
    print("4_ Exit")
    escolha = int(input("Digite a opção desejada:"))
    print("\naguarde um instante...") 
    tempo()
    clear()
    
    # 1 - Criar nova conta
    if escolha == 1:
        #cria uma nova conta corrente
        novaConta = corrente()
        print("Nova conta\n")
        #preenche os astributos da conta
        novaConta.numero = int(input("Número bancário: "))
        novaConta.titular = input("Titular do usuário: ")
        novaConta.senha = int(input("Senha: "))
        contas.append(novaConta)
        print("\naguarde um instante...") 
        tempo()
        clear()

    # 2 - Gerenciar uma conta
    if escolha ==2:
        #Recebe o número da conta desejada
        contaDesejada = int(input("Digite o número da sua conta:"))

        #cria a variável temporária posição
        posicao = None
        #cria a variável temporaria contaMexida
        contaMexida = corrente()

        #procura na lista uma conta com o número informado
        for conta in contas:
            #se a conta foi encontrara
            if conta.numero == contaDesejada:
                #a conta a ser alterada e copiada para a variável temporária
                contaMexida = conta
                #a posição da conta encontrada é salva na variável temporária
                posicao = contas.index(conta)
        #se a conta foi encontrada
        if posicao != None:
            print("Digite o nº da opção desejada: ")
            print("1_ Sacar")
            print("2_ Depositar")
            print("3_ Pagar Boleto")
            print("4_ Ver Informações")
            print("5_ Sair")

            opcao = int(input("Escolha: "))
            clear()
            if opcao == 1:
                print("\naguarde um instante...") 
                tempo()
                contaMexida.sacar()
            if opcao == 2:
                print("\naguarde um instante...") 
                tempo()
                contaMexida.depositar()
            if opcao == 3:
                print("\naguarde um instante...") 
                tempo()
                contaMexida.pagarBoleto()
            if opcao == 4:
                print("\naguarde um instante...") 
                tempo()
                contaMexida.verInfo()
            if opcao == 5:
                print("Alteração finalizada.")
                
            contas.insert(posicao,contaMexida)
        #se a conta não foi encontrada        
        else:
            print("Conta não cadastrada. Caso queira iniciar uma agora mesmo, basta selecionar a poção 1 do nosso menu pricipal, obrigado pela preferência.")
            clear()
    # 3 - Mostrar lista de contas        

    if escolha==3:
        print("\nLISTA DE CONTAS\n")
        #mostra o número de todas as contas que estão na lista de contas
        for conta in contas:
            print("Titular: ", conta.titular)
            print("Número bancário: ",conta.numero)

    # 4 - Sair 
    if escolha==4:
        print("\naguarde um instante...") 
        tempo()
        print("End code, obrigado por utilizar os programas da fsociety")
        exit()
