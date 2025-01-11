class Transferencia:
    @staticmethod
    def realizar_transferencia(remetente, usuarios, numero_conta_destino):
        conta_destino = next((usuario for usuario in usuarios if usuario.numero_conta_corrente == numero_conta_destino), None)

        if not conta_destino:
            print("Erro: Conta destino não encontrada.")
            return False

        print(f"Você está enviando para: {conta_destino.nome}")
        
        while True:
            try:
                valor = float(input("Informe o valor da transferência: R$ "))
                if valor <= 0:
                    print("Erro: O valor deve ser positivo.")
                    continue
                break
            except ValueError:
                print("Erro: Informe um valor numérico válido.")

        senha = input("Informe sua senha: ").strip()
        if remetente.senha != senha:
            print("Erro: Senha incorreta.")
            return False

        if not remetente.saldo.subtrair_saldo(valor):
            print("Erro: Saldo insuficiente para a transferência.")
            return False

        conta_destino.saldo.adicionar_saldo(valor)
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso para {conta_destino.nome}.")
        return True
