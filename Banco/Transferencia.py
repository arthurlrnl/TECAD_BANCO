class Transferencia:
    """
    Classe para gerenciar transferências entre contas.
    """
    def __init__(self, remetente, destinatario, valor, senha):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
        self.senha = senha
        self.status = "Pendente"  # Pode ser "Pendente", "Aprovada" ou "Rejeitada"
        self.mensagem = ""  # Explicação detalhada sobre o status

    def validar_transferencia(self):
        """
        Valida os critérios necessários para a transferência.
        """
        # Verificar se a senha do remetente está correta
        if not self.remetente.validar_senha(self.senha):
            self.status = "Rejeitada"
            self.mensagem = "Senha incorreta."
            return False

        # Verificar se o remetente tem saldo suficiente
        if not self.remetente.saldo.debitar(self.valor):
            self.status = "Rejeitada"
            self.mensagem = "Saldo insuficiente para realizar a transferência."
            return False

        return True

    def executar(self):
        """
        Executa a transferência se for válida.
        """
        if self.validar_transferencia():
            # Creditar o valor na conta do destinatário
            self.destinatario.saldo.creditar(self.valor)
            self.status = "Aprovada"
            self.mensagem = "Transferência realizada com sucesso."

            # Registrar transações no histórico de ambas as contas
            self.remetente.saldo._registrar_historico("Transferência enviada", -self.valor)
            self.destinatario.saldo._registrar_historico("Transferência recebida", self.valor)
            return True

        return False

    def detalhes_transferencia(self):
        """
        Retorna um resumo da transferência.
        """
        return {
            "remetente": self.remetente.nome,
            "destinatario": self.destinatario.nome,
            "valor": self.valor,
            "status": self.status,
            "mensagem": self.mensagem
        }
