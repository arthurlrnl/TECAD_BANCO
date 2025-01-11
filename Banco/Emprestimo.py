class Emprestimo:
    def __init__(self, renda, valor_emprestimo, numero_parcelas):
        self.renda = renda
        self.valor_emprestimo = valor_emprestimo
        self.numero_parcelas = numero_parcelas
        self.taxa_juros = 0.05
        self.valor_parcela = self.calcular_valor_parcela()

    def calcular_valor_parcela(self):
        
        valor_total = self.valor_emprestimo * (1 + self.taxa_juros * self.numero_parcelas)
        return valor_total / self.numero_parcelas

    def validar_emprestimo(self, saldo):
        
        if saldo.saldo < 0:
            print("Empréstimo negado: saldo negativo devido ao uso do limite.")
            return False

        if hasattr(saldo, 'emprestimo_ativo') and saldo.emprestimo_ativo:
            print("Empréstimo negado: cliente já possui um empréstimo ativo.")
            return False

        limite_parcela = self.renda * 0.3
        if self.valor_parcela > limite_parcela:
            print("Empréstimo negado: parcela excede 30% da renda.")
            return False

        return True

    def registrar_emprestimo(self, saldo):
        saldo.adicionar_saldo(self.valor_emprestimo)
        saldo.emprestimo_ativo = True 
        print(f"Empréstimo aprovado! Valor de R$ {self.valor_emprestimo:.2f} adicionado ao saldo.")

    @staticmethod
    def solicitar_emprestimo(renda, saldo):
        print("Bem-vindo ao sistema de empréstimos!")
        print("Como estudante da UFMG, você possui um empréstimo pré-aprovado de R$ 500,00.")

        try:
            valor_pre_aprovado = 500.0
            confirmar_pre_aprovado = input("Deseja utilizar o empréstimo pré-aprovado de R$ 500,00? (S/N): ").strip().upper()
            if confirmar_pre_aprovado == 'S':
                emprestimo = Emprestimo(renda, valor_pre_aprovado, 1)
                if emprestimo.validar_emprestimo(saldo):
                    emprestimo.registrar_emprestimo(saldo)
                return

            valor_emprestimo = float(input("Informe o valor do empréstimo desejado: R$ "))
            numero_parcelas = int(input("Informe o número de parcelas: "))
            
            emprestimo = Emprestimo(renda, valor_emprestimo, numero_parcelas)

            print(f"Valor de cada parcela: R$ {emprestimo.valor_parcela:.2f}")
            print(f"Número de parcelas: {numero_parcelas}")

            if emprestimo.validar_emprestimo(saldo):
                confirmar = input("Deseja confirmar o empréstimo? (S/N): ").strip().upper()
                if confirmar == 'S':
                    emprestimo.registrar_emprestimo(saldo)
                else:
                    print("Empréstimo cancelado pelo cliente.")
            else:
                print("Empréstimo não aprovado.")

        except ValueError:
            print("Erro: Informe valores válidos para o empréstimo.")
