from Extrato import Extrato

class Saldo:
    """
    Classe para gerenciar o saldo de uma conta bancária.
    Inclui operações de crédito, débito e registro no extrato.
    """
    def __init__(self, numero_conta, callback_salvar=None):
        self._saldo = 0.0
        self.numero_conta = numero_conta
        self._historico = []
        self._callback_salvar = callback_salvar
        self._extrato = Extrato() 

    @property
    def saldo(self):
        return self._saldo

    def creditar(self, valor):
        """
        Adiciona saldo à conta.
        """
        if valor <= 0:
            raise ValueError("O valor a ser creditado deve ser maior que zero.")
        self._saldo += valor
        self._registrar_historico("Crédito", valor)
        if self._callback_salvar:
            self._callback_salvar() 
        return f"R$ {valor:.2f} creditados no saldo."

    def debitar(self, valor):
        """
        Subtrai saldo da conta.
        """
        if valor <= 0:
            raise ValueError("O valor a ser debitado deve ser maior que zero.")
        if self._saldo >= valor:
            self._saldo -= valor
            self._registrar_historico("Débito", -valor)
            if self._callback_salvar:
                self._callback_salvar() 
            return f"R$ {valor:.2f} debitados do saldo."

        return "Saldo insuficiente."

    def exibir_saldo(self):
        """
        Retorna uma representação legível do saldo.
        """
        return f"Saldo atual: R$ {self._saldo:.2f}"

    def _registrar_historico(self, descricao, valor):
        """
        Registra uma transação no extrato.
        """
        self._extrato.adicionar_transacao(descricao, valor)

    def exibir_historico(self):
        """
        Retorna o histórico de transações formatado.
        """
        return self._extrato.exibir_extrato(self._saldo)
