class Saldo:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

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

    def exibir_saldo(self):
        return f"Saldo atual: R$ {self._saldo:.2f}"
