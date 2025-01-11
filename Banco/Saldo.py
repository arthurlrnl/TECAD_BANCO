class Saldo:
    def __init__(self, numero_conta):
        self._saldo = 0
        self._limite_credito = 0
        self._usar_limite_credito = False
        self.numero_conta = numero_conta  # Identificador único do usuário

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        raise AttributeError("Use os métodos adicionar_saldo ou subtrair_saldo para modificar o saldo.")

    def ativar_limite_credito(self, limite):
        if limite <= 0:
            raise ValueError("O limite de crédito deve ser maior que zero.")
        self._limite_credito = limite
        self._usar_limite_credito = True
        print(f"Limite de crédito ativado: R$ {limite:.2f}")

    def desativar_limite_credito(self):
        self._usar_limite_credito = False
        self._limite_credito = 0
        print("Limite de crédito desativado.")

    def adicionar_saldo(self, valor):
        if valor <= 0:
            raise ValueError("O valor a ser adicionado deve ser maior que zero.")
        self._saldo += valor
        print(f"R$ {valor:.2f} adicionados ao saldo.")

    def subtrair_saldo(self, valor):
        if valor <= 0:
            raise ValueError("O valor a ser subtraído deve ser maior que zero.")

        if self._saldo >= valor:
            self._saldo -= valor
            print(f"R$ {valor:.2f} subtraídos do saldo.")
            return True

        if self._usar_limite_credito and (self._saldo - valor) >= -self._limite_credito:
            self._saldo -= valor
            print(f"R$ {valor:.2f} subtraídos usando o limite de crédito.")
            return True

        print("Saldo insuficiente e limite de crédito indisponível.")
        return False

    def deposito(self, valor):
        print("Realizando depósito...")
        self.adicionar_saldo(valor)

    def transferencia(self, destino, valor):
        print("Realizando transferência...")
        if self.subtrair_saldo(valor):
            destino.adicionar_saldo(valor)
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso para a conta {destino.numero_conta}.")
            return True

        print("Transferência não realizada devido a saldo insuficiente.")
        return False
