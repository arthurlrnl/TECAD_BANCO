from saldo import Saldo
from transferencia import Transferencia
from extrato import Extrato

class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, saldo_inicial=0):
        if numero_conta in self.contas:
            print("Erro: Conta já existente.")
        else:
            self.contas[numero_conta] = {
                "saldo": Saldo(saldo_inicial),
                "extrato": Extrato()
            }
            print(f"Conta {numero_conta} criada com sucesso!")

    def realizar_transferencia(self, origem, destino, valor):
        if origem not in self.contas or destino not in self.contas:
            print("Erro: Uma ou mais contas não existem.")
            return

        transferencia = Transferencia(self.contas[origem]["saldo"], self.contas[destino]["saldo"], valor)
        if transferencia.executar():
            self.contas[origem]["extrato"].adicionar_transacao(f"Transferência para {destino}", -valor)
            self.contas[destino]["extrato"].adicionar_transacao(f"Transferência de {origem}", valor)
            print("Transferência realizada com sucesso!")
        else:
            print("Erro: Saldo insuficiente.")

    def exibir_saldo(self, numero_conta):
        if numero_conta in self.contas:
            print(self.contas[numero_conta]["saldo"].exibir_saldo())
        else:
            print("Erro: Conta não encontrada.")

    def exibir_extrato(self, numero_conta):
        if numero_conta in self.contas:
            print(self.contas[numero_conta]["extrato"].exibir_extrato())
        else:
            print("Erro: Conta não encontrada.")
