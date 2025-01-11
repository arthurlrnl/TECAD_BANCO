class Saldo:
    """
    Classe para gerenciar o saldo de uma conta bancária.
    Inclui operações de crédito, débito e controle de limite.
    """
    def __init__(self, numero_conta):
        self._saldo = 0.0
        self._limite_credito = 0.0
        self._usar_limite_credito = False
        self.numero_conta = numero_conta
        self._historico = []

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite_credito(self):
        return self._limite_credito

    @property
    def usar_limite_credito(self):
        return self._usar_limite_credito

    def ativar_limite_credito(self, limite):
        """
        Ativa o limite de crédito para a conta.
        """
        if limite <= 0:
            raise ValueError("O limite de crédito deve ser maior que zero.")
        self._limite_credito = limite
        self._usar_limite_credito = True
        self._registrar_historico("Limite de crédito ativado", limite)
        print(f"Limite de crédito ativado: R$ {limite:.2f}")

    def desativar_limite_credito(self):
        """
        Desativa o limite de crédito da conta.
        """
        self._usar_limite_credito = False
        self._limite_credito = 0
        self._registrar_historico("Limite de crédito desativado", 0)
        print("Limite de crédito desativado.")

    def creditar(self, valor):
        """
        Adiciona saldo à conta.
        """
        if valor <= 0:
            raise ValueError("O valor a ser creditado deve ser maior que zero.")
        self._saldo += valor
        self._registrar_historico("Crédito", valor)
        print(f"R$ {valor:.2f} creditados no saldo.")

    def debitar(self, valor):
        """
        Subtrai saldo da conta. Usa o limite de crédito se necessário.
        """
        if valor <= 0:
            raise ValueError("O valor a ser debitado deve ser maior que zero.")

        if self._saldo >= valor:
            self._saldo -= valor
            self._registrar_historico("Débito", -valor)
            print(f"R$ {valor:.2f} debitados do saldo.")
            return True

        if self._usar_limite_credito and (self._saldo - valor) >= -self._limite_credito:
            self._saldo -= valor
            self._registrar_historico("Débito com limite", -valor)
            print(f"R$ {valor:.2f} debitados usando o limite de crédito.")
            return True

        print("Saldo insuficiente e limite de crédito indisponível.")
        return False

    def _registrar_historico(self, descricao, valor):
        """
        Registra uma movimentação no histórico.
        """
        self._historico.append({"descricao": descricao, "valor": valor})

    def exibir_historico(self):
        """
        Exibe o histórico de movimentações.
        """
        print("\n=== Histórico de Movimentações ===")
        for mov in self._historico:
            print(f"{mov['descricao']}: R$ {mov['valor']:.2f}")
        print("==============================\n")

    def exibir_saldo(self):
        """
        Retorna uma representação legível do saldo e do limite.
        """
        status_limite = "ativo" if self._usar_limite_credito else "desativado"
        return (f"Saldo atual: R$ {self._saldo:.2f}\n"
                f"Limite de crédito: R$ {self._limite_credito:.2f} ({status_limite})")
