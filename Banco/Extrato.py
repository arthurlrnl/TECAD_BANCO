from datetime import datetime

class Extrato:
    """
    Classe para gerenciar o extrato de uma conta bancária.
    Armazena e organiza as transações realizadas.
    """
    def __init__(self):
        self._transacoes = []  # Lista de transações: {"data", "descricao", "valor"}

    def adicionar_transacao(self, descricao, valor):
        """
        Adiciona uma transação ao extrato.
        """
        transacao = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "descricao": descricao,
            "valor": valor
        }
        self._transacoes.append(transacao)
        print(f"Transação registrada: {descricao} - R$ {valor:.2f}")

    def exibir_extrato(self, saldo_atual=None, filtro=None):
        """
        Exibe o extrato das transações.
        Opcionalmente, filtra por tipo ou intervalo de datas.
        """
        print("\n=== Extrato da Conta ===")
        for transacao in self._filtrar_transacoes(filtro):
            tipo = "Crédito" if transacao["valor"] > 0 else "Débito"
            print(f"{transacao['data']} - {tipo}: {transacao['descricao']} - R$ {abs(transacao['valor']):.2f}")
        if saldo_atual is not None:
            print(f"Saldo Atual: R$ {saldo_atual:.2f}")
        print("=======================\n")

    def exportar_extrato(self, caminho_arquivo, saldo_atual=None, filtro=None, formato="txt"):
        """
        Exporta o extrato para um arquivo.
        Suporta formatos 'txt' e 'json'.
        """
        try:
            if formato == "txt":
                with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                    arquivo.write("=== Extrato da Conta ===\n")
                    for transacao in self._filtrar_transacoes(filtro):
                        tipo = "Crédito" if transacao["valor"] > 0 else "Débito"
                        arquivo.write(f"{transacao['data']} - {tipo}: {transacao['descricao']} - R$ {abs(transacao['valor']):.2f}\n")
                    if saldo_atual is not None:
                        arquivo.write(f"Saldo Atual: R$ {saldo_atual:.2f}\n")
                    arquivo.write("=======================\n")
            elif formato == "json":
                import json
                with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                    dados = {
                        "transacoes": self._filtrar_transacoes(filtro),
                        "saldo_atual": saldo_atual
                    }
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            print(f"Extrato exportado para {caminho_arquivo}")
        except IOError as e:
            print(f"Erro ao exportar o extrato: {e}")

    def _filtrar_transacoes(self, filtro):
        """
        Filtra transações com base em um critério.
        """
        if filtro is None:
            return self._transacoes
        # Exemplo de filtro por data ou tipo
        if "tipo" in filtro:
            tipo = filtro["tipo"]
            return [t for t in self._transacoes if (t["valor"] > 0 and tipo == "Crédito") or (t["valor"] < 0 and tipo == "Débito")]
        if "data_inicio" in filtro and "data_fim" in filtro:
            data_inicio = datetime.strptime(filtro["data_inicio"], "%d/%m/%Y")
            data_fim = datetime.strptime(filtro["data_fim"], "%d/%m/%Y")
            return [t for t in self._transacoes if data_inicio <= datetime.strptime(t["data"], "%d/%m/%Y %H:%M:%S") <= data_fim]
        return self._transacoes
