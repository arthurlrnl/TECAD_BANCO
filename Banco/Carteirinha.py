class Carteirinha:
    def __init__(self):
        self._saldo_carteirinha = 0

    @property
    def saldo_carteirinha(self):
        return self._saldo_carteirinha

    def adicionar_saldo(self, valor):
        if valor <= 0:
            raise ValueError("O valor a ser adicionado deve ser maior que zero.")
        self._saldo_carteirinha += valor
        print(f"R$ {valor:.2f} adicionados à carteirinha. Saldo atual: R$ {self._saldo_carteirinha:.2f}")

    def liberar_catraca(self):
        custo_refeicao = 5.6
        if self._saldo_carteirinha >= custo_refeicao:
            self._saldo_carteirinha -= custo_refeicao
            print("Catraca liberada. Aproveite sua refeição!")
            print(f"Saldo restante na carteirinha: R$ {self._saldo_carteirinha:.2f}")
        else:
            print("Saldo insuficiente na carteirinha para liberar a catraca.")