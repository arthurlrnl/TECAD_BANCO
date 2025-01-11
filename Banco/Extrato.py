from abc import ABC, abstractmethod

class RelatorioFinanceiro(ABC):
    @abstractmethod
    def adicionar_transacao(self, descricao, valor):
        pass

    @abstractmethod
    def exibir_relatorio(self):
        pass

    @abstractmethod
    def exportar_relatorio(self, caminho_arquivo):
        pass

class Extrato(RelatorioFinanceiro):
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, descricao, valor):
        self._transacoes.append({"descricao": descricao, "valor": valor})

    def exibir_relatorio(self):
        relatorio = "Extrato de Transações:\n"
        for transacao in self._transacoes:
            relatorio += f"{transacao['descricao']}: R$ {transacao['valor']:.2f}\n"
        return relatorio

    def exportar_relatorio(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(self.exibir_relatorio())
        except IOError as e:
            print(f"Erro ao exportar o relatório: {e}")
