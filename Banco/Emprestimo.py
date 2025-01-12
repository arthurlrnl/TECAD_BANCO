from abc import ABC, abstractmethod


class EmprestimoBase(ABC):
    """
    Classe abstrata para definir a interface de empréstimos.
    """
    def __init__(self, valor_emprestimo, numero_parcelas):
        self._valor_emprestimo = valor_emprestimo
        self._numero_parcelas = numero_parcelas
        self._taxa_juros = 0.05  # Juros padrão de 5% por mês
        self._valor_parcela = self.calcular_valor_parcela()

    @property
    def valor_emprestimo(self):
        return self._valor_emprestimo

    @property
    def numero_parcelas(self):
        return self._numero_parcelas

    @property
    def taxa_juros(self):
        return self._taxa_juros

    @property
    def valor_parcela(self):
        return self._valor_parcela

    @abstractmethod
    def calcular_valor_parcela(self):
        """
        Método abstrato para calcular o valor das parcelas.
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
        Registra o empréstimo adicionando o valor ao saldo e ao histórico.
        """
        saldo.creditar(self._valor_emprestimo)
        saldo._registrar_historico("Empréstimo recebido", self._valor_emprestimo)
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
        """
        Valida se o empréstimo pode ser aprovado para um estudante.
        """
        if saldo.saldo < 0:
            print("Empréstimo negado: saldo negativo.")
            return False

        limite_parcela = saldo.saldo * 0.3  # Estudantes podem comprometer até 30% do saldo
        if self._valor_parcela > limite_parcela:
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
        """
        Valida se o empréstimo pode ser aprovado para um cliente geral.
        """
        if saldo.saldo < 0:
            print("Empréstimo negado: saldo negativo.")
            return False

        limite_parcela = saldo.saldo * 0.5  # Clientes podem comprometer até 50% do saldo
        if self._valor_parcela > limite_parcela:
            print("Empréstimo negado: parcela excede 50% do saldo disponível.")
            return False

       
