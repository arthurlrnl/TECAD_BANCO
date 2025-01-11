from DataManager import DataManager
from Usuario import Aluno, Servidor
from Transferencia import Transferencia
from Extrato import Extrato
from Emprestimo import EmprestimoEstudantil, EmprestimoPessoal
import re
from datetime import datetime

class SistemaBancario:
    def __init__(self):
        self.data_manager = DataManager()
        self.usuarios = self.data_manager.carregar_dados()
        self.usuario_logado = None

    def criar_conta(self, tipo, dados_usuario):
        cpf = dados_usuario.get("cpf", "").strip()
        data_nascimento = dados_usuario.get("data_nascimento", "").strip()
        senha = dados_usuario.get("senha", "").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido. Insira exatamente 11 números.")
        try:
            data_nasc_obj = datetime.strptime(data_nascimento, "%d/%m/%Y")
            if data_nasc_obj > datetime.now():
                raise ValueError("Data de nascimento inválida. Não pode estar no futuro.")
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato DD/MM/AAAA.")
        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r"[A-Z]", senha):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r"\d", senha):
            raise ValueError("A senha deve conter pelo menos um número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
            raise ValueError("A senha deve conter pelo menos um caractere especial (!@#$%^&*(), etc.).")
        if any(u.cpf == cpf for u in self.usuarios):
            raise ValueError("CPF já cadastrado.")

        if tipo == "Aluno":
            usuario = Aluno(**dados_usuario)
        elif tipo == "Professor":
            usuario = Servidor(**dados_usuario)
        else:
            raise ValueError("Tipo de usuário inválido.")

        self.usuarios.append(usuario)
        self.data_manager.salvar_dados(self.usuarios)
        return usuario

    def fazer_login(self, cpf, senha):
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)
        if not usuario or not usuario.validar_senha(senha):
            raise ValueError("CPF ou senha inválidos.")
        self.usuario_logado = usuario
        return usuario

    def realizar_transferencia(self, cpf_destinatario, valor, senha):
        if not self.usuario_logado:
            raise ValueError("Nenhum usuário logado.")

        destinatario = next((u for u in self.usuarios if u.cpf == cpf_destinatario), None)
        if not destinatario:
            raise ValueError("Destinatário não encontrado.")

        transferencia = Transferencia(self.usuario_logado, destinatario, valor, senha)
        if not transferencia.executar():
            raise ValueError(transferencia.mensagem)

        self.data_manager.salvar_dados(self.usuarios)
        return transferencia

    def solicitar_emprestimo(self, tipo, valor, numero_parcelas):
        if not self.usuario_logado:
            raise ValueError("Nenhum usuário logado.")

        saldo = self.usuario_logado.saldo

        if tipo == "Estudantil":
            emprestimo = EmprestimoEstudantil(valor, numero_parcelas)
        elif tipo == "Pessoal":
            emprestimo = EmprestimoPessoal(valor, numero_parcelas)
        else:
            raise ValueError("Tipo de empréstimo inválido.")

        if emprestimo.validar_emprestimo(saldo):
            emprestimo.registrar_emprestimo(saldo)
            self.data_manager.salvar_dados(self.usuarios)
            return emprestimo
        else:
            raise ValueError("Empréstimo não aprovado. Verifique as condições.")

    def exibir_saldo(self):
        if not self.usuario_logado:
            raise ValueError("Nenhum usuário logado.")
        return self.usuario_logado.saldo.exibir_saldo()

    def exibir_extrato(self, filtro=None):
        if not self.usuario_logado:
            raise ValueError("Nenhum usuário logado.")
        extrato = self.usuario_logado.saldo.exibir_historico()
        return extrato

    def gerenciar_carteirinha(self, operacao, valor=None):
        if not self.usuario_logado:
            raise ValueError("Nenhum usuário logado.")
        carteirinha = self.usuario_logado.carteirinha

        if operacao == "adicionar_saldo" and valor is not None:
            carteirinha.adicionar_saldo(valor)
        elif operacao == "liberar_catraca":
            return carteirinha.liberar_catraca()
        else:
            raise ValueError("Operação inválida para a carteirinha.")
