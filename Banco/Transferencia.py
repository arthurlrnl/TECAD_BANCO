class Transferencia:
    def __init__(self, remetente, destinatario, valor, senha):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
        self.senha = senha
        self.status = "Pendente" 

    def validar_transferencia(self):
        """
        Valida os critérios necessários para a transferência.
        """
     
        if not self.remetente.validar_senha(self.senha):
            self.status = "Rejeitada: senha incorreta"
            return False

        if not self.remetente.saldo.subtrair_saldo(self.valor):
            self.status = "Rejeitada: saldo insuficiente"
            return False

        return True

    def executar(self):
        """
        Executa a transferência se for válida.
        """
        if self.validar_transferencia():
            self.destinatario.saldo.adicionar_saldo(self.valor)
            self.status = "Aprovada"
            self.remetente.extrato.adicionar_transacao("Transferência enviada", -self.valor)
            self.destinatario.extrato.adicionar_transacao("Transferência recebida", self.valor)
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
            "status": self.status
        }
