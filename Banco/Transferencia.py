from abc import ABC, abstractmethod

class OperacaoFinanceira(ABC):
    @abstractmethod
    def executar(self):
        pass

class Transferencia(OperacaoFinanceira):
    def __init__(self, conta_origem, conta_destino, valor):
        self._conta_origem = conta_origem
        self._conta_destino = conta_destino
        self._valor = valor

    @property
    def conta_origem(self):
        return self._conta_origem

    @property
    def conta_destino(self):
        return self._conta_destino

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        self._valor = valor

    def executar(self):
        if self._conta_origem.subtrair_valor(self._valor):
            self._conta_destino.adicionar_valor(self._valor)
            return True
        return False

# Exemplo de uso:
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def adicionar_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser adicionado deve ser positivo.")
        self._saldo += valor

    def subtrair_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser subtraído deve ser positivo.")
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

conta1 = Conta(1000)
conta2 = Conta(500)

transferencia = Transferencia(conta1, conta2, 200)
if transferencia.executar():
    print("Transferência realizada com sucesso!")
    print(f"Saldo Conta 1: R$ {conta1.saldo:.2f}")
    print(f"Saldo Conta 2: R$ {conta2.saldo:.2f}")
else:
    print("Transferência falhou!")
