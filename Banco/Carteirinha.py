class Carteirinha:
    """
    Classe para gerenciar o saldo da carteirinha do RU.
    Permite adicionar saldo, liberar catraca e consultar histórico.
    """
    PRECO_PADRAO = 5.6  # Preço para alunos não FUMPistas
    PRECOS_FUMP = {
        "I": 0.0,  # Gratuito para FUMPistas Nível I
        "II": 1.0,  # R$ 1,00 para FUMPistas Nível II
        "III": 1.0,  # R$ 1,00 para FUMPistas Nível III
        "IV": 2.0   # R$ 2,00 para FUMPistas Nível IV
    }
    PRECO_PROFESSOR = 13.0  # Preço fixo para professores

    def __init__(self, tipo_usuario, nivel_fump=None):
        self._saldo_carteirinha = 0.0
        self._historico = []
        self._tipo_usuario = tipo_usuario
        self._nivel_fump = nivel_fump
        self._custo_refeicao = self.definir_custo_refeicao()

    @property
    def saldo_carteirinha(self):
        return self._saldo_carteirinha

    @property
    def custo_refeicao(self):
        return self._custo_refeicao

    def definir_custo_refeicao(self):
        """
        Define o custo da refeição com base no tipo de usuário e nível FUMP.
        """
        if self._tipo_usuario == "Professor":
            return self.PRECO_PROFESSOR
        elif self._tipo_usuario == "Aluno":
            return self.PRECOS_FUMP.get(self._nivel_fump, self.PRECO_PADRAO)
        return 20.0  # Valor padrão caso o tipo de usuário não seja reconhecido

    def adicionar_saldo(self, valor):
        """
        Adiciona saldo à carteirinha.
        """
        if valor <= 0:
            raise ValueError("O valor a ser adicionado deve ser maior que zero.")
        self._saldo_carteirinha += valor
        self._registrar_historico("Crédito", valor)

    def liberar_catraca(self):
        """
        Libera a catraca do RU, descontando o custo da refeição.
        """
        if self._saldo_carteirinha >= self._custo_refeicao:
            self._saldo_carteirinha -= self._custo_refeicao
            self._registrar_historico("Débito: Refeição no RU", -self._custo_refeicao)
            return "Catraca liberada. Aproveite sua refeição!"
        else:
            return "Saldo insuficiente na carteirinha para liberar a catraca."

    def _registrar_historico(self, descricao, valor):
        """
        Registra uma movimentação no histórico.
        """
        self._historico.append({"descricao": descricao, "valor": valor})

    def exibir_historico(self):
        """
        Retorna o histórico de movimentações da carteirinha como uma string.
        """
        historico = [
            f"{'Crédito' if mov['valor'] > 0 else 'Débito'}: {mov['descricao']} - R$ {abs(mov['valor']):.2f}"
            for mov in self._historico
        ]
        return "\n".join(["=== Histórico da Carteirinha ==="] + historico + ["=============================="])
