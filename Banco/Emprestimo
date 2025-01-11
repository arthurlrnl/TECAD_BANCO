from abc import ABC, abstractmethod

class EmprestimoBase(ABC):
    def __init__(self, salario, valor_emprestimo, numero_parcelas):
        self._salario = salario
        self._valor_emprestimo = valor_emprestimo
        self._numero_parcelas = numero_parcelas
        self._valor_parcela = self.calcular_valor_parcela()

    @abstractmethod
    def calcular_valor_parcela(self):
        pass

    def validar_solicitacao(self):
        return self._valor_parcela <= (self._salario / 2)

    def exibir_detalhes(self):
        detalhes = (
            f"Salário: {self._salario}\n"
            f"Valor do Empréstimo: {self._valor_emprestimo}\n"
            f"Número de Parcelas: {self._numero_parcelas}\n"
            f"Valor da Parcela: {self._valor_parcela:.2f}\n"
        )
        return detalhes

    # Getters e Setters para encapsulamento
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    @property
    def valor_emprestimo(self):
        return self._valor_emprestimo

    @valor_emprestimo.setter
    def valor_emprestimo(self, valor):
        self._valor_emprestimo = valor

    @property
    def numero_parcelas(self):
        return self._numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, valor):
        self._numero_parcelas = valor

class EmprestimoPessoal(EmprestimoBase):
    def calcular_valor_parcela(self):
        taxa_juros = 0.05  # Taxa fixa para empréstimos pessoais
        valor_total = self._valor_emprestimo * (1 + taxa_juros)
        return valor_total / self._numero_parcelas

class EmprestimoImobiliario(EmprestimoBase):
    def calcular_valor_parcela(self):
        taxa_juros = 0.03  # Taxa reduzida para empréstimos imobiliários
        valor_total = self._valor_emprestimo * (1 + taxa_juros)
        return valor_total / self._numero_parcelas
