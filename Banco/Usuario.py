import re
import random

class Usuario:
    usuarios = []
    numeros_conta_corrente_gerados = set()

    def __init__(self, nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.senha = senha
        self.numero_conta_corrente = numero_conta_corrente

    @staticmethod
    def criar_usuario():
        print("Bem-vindo ao cadastro de usuário! Preencha os dados abaixo.")

        while True:
            nome = input("Nome completo: ").strip()
            if nome:
                break
            print("O nome não pode estar vazio.")

        while True:
            cpf = input("CPF (somente números): ").strip()
            if len(cpf) == 11 and cpf.isdigit() and not Usuario.cpf_existente(cpf):
                break
            print("CPF inválido ou já existente. Por favor, tente novamente.")

        while True:
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
            if Usuario.validar_data_nascimento(data_nascimento):
                break
            print("Data de nascimento inválida. Use o formato DD/MM/AAAA.")

        while True:
            endereco = input("Endereço completo: ").strip()
            if endereco:
                break
            print("O endereço não pode estar vazio.")

        print("\nA senha deve atender aos seguintes requisitos:")
        print("- Ter entre 8 e 30 caracteres.")
        print("- Conter pelo menos uma letra maiúscula.")
        print("- Conter pelo menos um número.")
        print("- Conter pelo menos um caractere especial.")

        while True:
            senha = input("Crie uma senha: ").strip()
            if Usuario.senha_valida(senha):
                break

        numero_conta_corrente = Usuario.gerar_numero_conta_corrente()

        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente)
        Usuario.usuarios.append(novo_usuario)
        print(f"\nUsuário criado com sucesso! Número da conta: {numero_conta_corrente}")

    @staticmethod
    def cpf_existente(cpf):
        return any(usuario.cpf == cpf for usuario in Usuario.usuarios)

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
    def validar_data_nascimento(data):
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", data):
            return False
        dia, mes, ano = map(int, data.split('/'))
        if not (1 <= mes <= 12):
            return False
        if dia < 1 or (mes == 2 and (dia > 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else dia > 28)) or (dia > 30 and mes in [4, 6, 9, 11]) or dia > 31:
            return False
        return True
