from Usuario import Usuario
from Saldo import Saldo
from Transferencia import Transferencia
from Emprestimo import Emprestimo
from Extrato import Extrato
from Carteirinha import Carteirinha

class SistemaBancario:
    def __init__(self):
        self.usuarios = []  # Lista de usuários cadastrados
        self.usuario_logado = None

    def executar_aplicativo(self):
        while True:
            print("\n=== Bem-vindo ao Banco UFMG ===")
            print("1. Criar conta")
            print("2. Fazer login")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_conta()
            elif opcao == "2":
                self.fazer_login()
            elif opcao == "0":
                print("Obrigado por usar o Banco UFMG. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def criar_conta(self):
        Usuario.criar_usuario()

    def fazer_login(self):
        cpf = input("Digite o CPF: ")
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)

        if not usuario:
            print("CPF não encontrado.")
            return

        for _ in range(3):
            senha = input("Digite a senha: ")
            if usuario.senha == senha:
                self.usuario_logado = usuario
                print(f"Login realizado com sucesso! Bem-vindo(a), {usuario.nome}.")
                self.menu_usuario()
                return
            else:
                print("Senha incorreta. Tente novamente.")

        print("Número máximo de tentativas excedido.")

    def menu_usuario(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1. Exibir saldo")
            print("2. Realizar transferência")
            print("3. Exibir extrato")
            print("4. Depósito")
            print("5. Carteirinha")
            print("6. Crédito (Empréstimo)")
            print("0. Logout")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.exibir_saldo()
            elif opcao == "2":
                self.realizar_transferencia()
            elif opcao == "3":
                self.exibir_extrato()
            elif opcao == "4":
                self.realizar_deposito()
            elif opcao == "5":
                self.gerenciar_carteirinha()
            elif opcao == "6":
                self.solicitar_emprestimo()
            elif opcao == "0":
                print("Logout realizado. Voltando ao menu principal.")
                self.usuario_logado = None
                break
            else:
                print("Opção inválida. Tente novamente.")

    def exibir_saldo(self):
        print(self.usuario_logado.saldo.exibir_saldo())

    def realizar_transferencia(self):
        numero_conta_destino = input("Digite o número da conta destino: ")
        Transferencia.realizar_transferencia(self.usuario_logado, self.usuarios, numero_conta_destino)

    def exibir_extrato(self):
        self.usuario_logado.extrato.exibir_extrato(self.usuario_logado.saldo.saldo)

    def realizar_deposito(self):
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            self.usuario_logado.saldo.adicionar_saldo(valor)
            self.usuario_logado.extrato.adicionar_transacao("Depósito", valor)
            print("Depósito realizado com sucesso!")
        except ValueError:
            print("Erro: Informe um valor válido.")

    def gerenciar_carteirinha(self):
        while True:
            print("\n=== Carteirinha ===")
            print("1. Adicionar saldo na carteirinha")
            print("2. Liberar catraca do RU")
            print("0. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    valor = float(input("Informe o valor a ser adicionado: R$ "))
                    self.usuario_logado.carteirinha.adicionar_saldo(valor)
                except ValueError:
                    print("Erro: Informe um valor válido.")
            elif opcao == "2":
                self.usuario_logado.carteirinha.liberar_catraca()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def solicitar_emprestimo(self):
        Emprestimo.solicitar_emprestimo(self.usuario_logado.renda, self.usuario_logado.saldo)
