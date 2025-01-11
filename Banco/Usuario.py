from abc import ABC, abstractmethod
import re
import random

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @abstractmethod
    def exibir_dados(self):
        pass

class DadosUsuario(Pessoa):
    def __init__(self, nome='', senha='', data_nascimento='', endereco='', cpf='', numero_conta_corrente=''):
        super().__init__(nome, cpf)
        self._senha = senha
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._numero_conta_corrente = numero_conta_corrente
        self._saldo = 0
        self._extrato = []

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def endereco(self):
        return self._endereco

    @property
    def numero_conta_corrente(self):
        return self._numero_conta_corrente

    @property
    def saldo(self):
        return self._saldo

    def exibir_dados(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Conta: {self.numero_conta_corrente}"

class Usuario:
    usuarios = []
    numeros_conta_corrente_gerados = set()

    @staticmethod
    def criar_novo_usuario():
        print("\n=========================================================================")
        print("Obrigado por escolher o Banco UFMG, por favor, preencha os dados a seguir:")

        nome = input("Nome completo: ")

        while True:
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            if Usuario.validar_data_nascimento(data_nascimento):
                break

        endereco = input("Endereço Completo: ")

        while True:
            cpf = input("CPF (somente números, no formato XXXXXXXXXXX): ")
            if len(cpf) == 11 and cpf.isdigit() and not Usuario.cpf_existente(cpf):
                break
            print("CPF inválido ou já existente.")

        print("\nRequisitos para senha:\n- Deve ter entre 8 e 30 caracteres.\n- Deve conter pelo menos uma letra maiúscula, um número e um caractere especial.")
        while True:
            senha = input("Senha desejada: ")
            if Usuario.senha_valida(senha):
                break

        numero_conta_corrente = Usuario.gerar_numero_conta_corrente()
        novo_usuario = DadosUsuario(nome, senha, data_nascimento, endereco, cpf, numero_conta_corrente)
        Usuario.usuarios.append(novo_usuario)
        print("\nNovo usuário criado com sucesso!")

    @staticmethod
    def deletar_conta():
        numero_conta = input("Número da conta: ")
        nome_usuario = input("Nome do usuário: ")
        senha_usuario = input("Senha: ")

        usuario = next((u for u in Usuario.usuarios if u.numero_conta_corrente == numero_conta and u.nome == nome_usuario and u._senha == senha_usuario), None)

        if usuario:
            confirmacao = input("Tem certeza que deseja deletar sua conta? (S/N): ").strip().upper()
            if confirmacao == 'S':
                Usuario.usuarios.remove(usuario)
                print("Conta deletada com sucesso.")
            else:
                print("Operação de exclusão cancelada.")
        else:
            print("Dados incorretos ou conta não encontrada.")

    @staticmethod
    def senha_valida(senha):
        if len(senha) < 8 or len(senha) > 30:
            print("A senha deve ter entre 8 e 30 caracteres.")
            return False

        if not any(c.isupper() for c in senha):
            print("A senha deve conter pelo menos uma letra maiúscula.")
            return False

        if not any(c.isdigit() for c in senha):
            print("A senha deve conter pelo menos um número.")
            return False

        if not any(not c.isalnum() for c in senha):
            print("A senha deve conter pelo menos um caractere especial.")
            return False

        return True

    @staticmethod
    def gerar_numero_conta_corrente():
        while True:
            numero_conta = str(random.randint(100000, 999999))
            if numero_conta not in Usuario.numeros_conta_corrente_gerados:
                Usuario.numeros_conta_corrente_gerados.add(numero_conta)
                return numero_conta

    @staticmethod
    def cpf_existente(cpf):
        return any(usuario.cpf == cpf for usuario in Usuario.usuarios)

    @staticmethod
    def validar_data_nascimento(data):
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", data):
            print("Data de nascimento inválida. Use o formato DD/MM/AAAA.")
            return False

        dia, mes, ano = map(int, data.split('/'))
        if not (1 <= mes <= 12):
            print("Mês inválido.")
            return False

        if dia < 1 or (mes == 2 and (dia > 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else dia > 28)) or (dia > 30 and mes in [4, 6, 9, 11]) or dia > 31:
            print("Dia inválido para o mês especificado.")
            return False

        return True

    @staticmethod
    def adicionar_usuario_administrador():
        admin = DadosUsuario("Administrador", "#Senha123", cpf="12345678910")
        Usuario.usuarios.append(admin)
        print("Usuário Administrador criado com sucesso!")
