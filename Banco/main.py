if __name__ == "__main__":
    from BancoGUI import BancoGUI
    from SistemaBancario import SistemaBancario

    sistema = SistemaBancario()
    sistema.executar_transferencias_periodicas()  # Executa transferências automáticas, se aplicável

    app = BancoGUI()
    app.janela.mainloop()
