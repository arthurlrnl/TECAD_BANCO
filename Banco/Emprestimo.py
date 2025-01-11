from abc import ABC, abstractmethod

class EmprestimoBase(ABC):
    """
    Classe abstrata para definir a interface de empréstimos.
    """
    def __init__(self, valor_emprestimo, numero_parcelas):
        self._valor_emprestimo = valor_emprestimo
        self._numero_parcelas = numero_parcelas
        self._taxa_juros = 0.05  # Juros padrão de 5% por mês

    @property
    def valor_emprestimo(self):
        return self._valor_emprestimo

    @property
    def numero_parcelas(self):
        return self._numero_parcelas

    @property
    def taxa_juros(self):
        return self._taxa_juros

    @abstractmethod
    def calcular_valor_parcela(self):
        """
        Método abstrato para calcular o valor das parcelas.
        Deve ser implementado pelas subclasses.
        """
        pass

    @abstractmethod
    def validar_emprestimo(self, saldo):
        """
        Método abstrato para validar as condições do empréstimo.
        """
        pass

    def registrar_emprestimo(self, saldo):
        """
        Registra o empréstimo adicionando o valor ao saldo.
        """
        saldo.adicionar_saldo(self._valor_emprestimo)
        print(f"Empréstimo registrado: R$ {self._valor_emprestimo:.2f}")

class EmprestimoEstudantil(EmprestimoBase):
    """
    Classe para empréstimos estudantis com condições especiais.
    """
    def __init__(self, valor_emprestimo, numero_parcelas):
        super().__init__(valor_emprestimo, numero_parcelas)
        self._taxa_juros = 0.02  # Taxa reduzida para estudantes

    def calcular_valor_parcela(self):
        valor_total = self._valor_emprestimo * (1 + self._taxa_juros * self._numero_parcelas)
        return valor_total / self._numero_parcelas

    def validar_emprestimo(self, saldo):
        if saldo.saldo < 0:
            print("Empréstimo negado: saldo negativo.")
            return False

        limite_parcela = saldo.saldo * 0.3
        valor_parcela = self.calcular_valor_parcela()

        if valor_parcela > limite_parcela:
            print("Empréstimo negado: parcela excede 30% do saldo disponível.")
            return False

        return True

class EmprestimoPessoal(EmprestimoBase):
    """
    Classe para empréstimos pessoais com condições gerais.
    """
    def calcular_valor_parcela(self):
        valor_total = self._valor_emprestimo * (1 + self._taxa_juros * self._numero_parcelas)
        return valor_total / self._numero_parcelas

    def validar_emprestimo(self, saldo):
        if saldo.saldo < 0:
            print("Empréstimo negado: saldo negativo.")
            return False

        limite_parcela = saldo.saldo * 0.5  # Condições menos restritivas
        valor_parcela = self.calcular_valor_parcela()

        if valor_parcela > limite_parcela:
            print("Empréstimo negado: parcela excede 50% do saldo disponível.")
            return False

        return True

# Teste inicial de exemplo:
if __name__ == "__main__":
    from Saldo import Saldo

    saldo_usuario = Saldo("123456")
    saldo_usuario.adicionar_saldo(1000)

    emprestimo_estudantil = EmprestimoEstudantil(500, 12)
    if emprestimo_estudantil.validar_emprestimo(saldo_usuario):
        emprestimo_estudantil.registrar_emprestimo(saldo_usuario)
        print(f"Parcela mensal: R$ {emprestimo_estudantil.calcular_valor_parcela():.2f}")

    emprestimo_pessoal = EmprestimoPessoal(2000, 24)
    if emprestimo_pessoal.validar_emprestimo(saldo_usuario):
        emprestimo_pessoal.registrar_emprestimo(saldo_usuario)
        print(f"Parcela mensal: R$ {emprestimo_pessoal.calcular_valor_parcela():.2f}")
