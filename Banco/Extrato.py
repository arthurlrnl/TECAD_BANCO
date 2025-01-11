class Extrato:
    def __init__(self):
        self.transacoes = [] 
    def adicionar_transacao(self, descricao, valor):
        self.transacoes.append({"descricao": descricao, "valor": valor})

    def exibir_extrato(self, saldo_atual):
        print("\n=== Extrato da Conta ===")
        for transacao in self.transacoes:
            tipo = "Crédito" if transacao["valor"] > 0 else "Débito"
            print(f"{tipo}: {transacao['descricao']} - R$ {abs(transacao['valor']):.2f}")
        print(f"Saldo Atual: R$ {saldo_atual:.2f}")
        print("=======================\n")

    def exportar_extrato(self, caminho_arquivo, saldo_atual):
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write("=== Extrato da Conta ===\n")
                for transacao in self.transacoes:
                    tipo = "Crédito" if transacao["valor"] > 0 else "Débito"
                    arquivo.write(f"{tipo}: {transacao['descricao']} - R$ {abs(transacao['valor']):.2f}\n")
                arquivo.write(f"Saldo Atual: R$ {saldo_atual:.2f}\n")
                arquivo.write("=======================\n")
            print(f"Extrato exportado para {caminho_arquivo}")
        except IOError as e:
            print(f"Erro ao exportar o extrato: {e}")
