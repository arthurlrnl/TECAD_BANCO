import re
from usuario import Usuario, DadosUsuario

class SistemaBancario:
    def __init__(self):
        self.opcao = 0
        self.usuario_logado = None

    @staticmethod
    def exibir_mensagem_boas_vindas():
        print("\n========================================")
        print("        BEM VINDO AO BANCO UFMG        ")
        print("========================================\n")

    def executar_aplicativo(self):
        self.exibir_mensagem_boas_vindas()

        continuar_execucao = True

        while continuar_execucao:
            print("\n\n========================================\n")
            print("Escolha uma opção:\n"
                  "1. Cadastrar novo usuário\n"
                  "2. Fazer login\n"
                  "0. Encerrar o programa")
            self.opcao = int(input("Opção: "))

            if self.opcao == 1:
                Usuario.criar_novo_usuario()
            elif self.opcao == 2:
                self.fazer_login()
            elif self.opcao == 0:
                print("Encerrando o programa. Adeus!")
                continuar_execucao = False
            else:
                print("Opção inválida. Tente novamente.")

    def fazer_login(self):
        cpf = input("Digite o CPF: ")
        usuario = next((u for u in Usuario.usuarios if u.cpf == cpf), None)

        if not usuario:
            print("CPF não encontrado.")
            return

        for _ in range(3):
            senha = input("Digite a senha: ")
            if usuario._senha == senha:
                print("Login realizado com sucesso!")
                self.usuario_logado = usuario
                self.realizar_operacoes_apos_login()
                return
            else:
                print("Senha incorreta. Tente novamente.")

        print("Número máximo de tentativas excedido.")

    def realizar_operacoes_apos_login(self):
        while True:
            print(f"Bem-vindx, {self.usuario_logado.nome}!")
            print(f"CC: {self.usuario_logado.numero_conta_corrente}")
            print(f"Saldo: R$ {self.usuario_logado.saldo}")
            print("========================================")
            print("Escolha uma ação:")
            print("1. Fazer um novo depósito")
            print("2. Fazer uma transferência")
            print("3. Mostrar informações do usuário")
            print("0. Fazer logout e voltar ao menu principal")
            opcao = int(input("Opção: "))

            if opcao == 1:
                self.novo_deposito()
            elif opcao == 2:
                self.nova_transferencia()
            elif opcao == 3:
                self.mostrar_informacoes_usuario()
            elif opcao == 0:
                print("Fazendo logout e voltando ao menu principal.")
                return
            else:
                print("Opção inválida. Tente novamente.")

    def novo_deposito(self):
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            self.usuario_logado._saldo += valor
            self.usuario_logado._extrato.append(f"Depósito: +R$ {valor}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")

    def nova_transferencia(self):
        numero_conta = input("Digite o número da conta para transferência: ")
        destinatario = next((u for u in Usuario.usuarios if u.numero_conta_corrente == numero_conta), None)

        if not destinatario or destinatario == self.usuario_logado:
            print("Conta inválida ou não encontrada.")
            return

        valor = float(input("Informe o valor da transferência: R$ "))
        if valor > 0 and valor <= self.usuario_logado._saldo:
            self.usuario_logado._saldo -= valor
            destinatario._saldo += valor
            self.usuario_logado._extrato.append(f"Transferência: -R$ {valor}")
            destinatario._extrato.append(f"Transferência: +R$ {valor}")
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def mostrar_informacoes_usuario(self):
        print("\nInformações do Usuário:")
        print(self.usuario_logado.exibir_dados())
        print(f"Saldo: R$ {self.usuario_logado.saldo}")
        print("========================================")

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar_aplicativo()
