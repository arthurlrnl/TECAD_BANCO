import tkinter as tk
from tkinter import messagebox
from Usuario import Usuario

class BancoGUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Banco UFMG")
        self.janela.geometry("400x300")
        self.inicializar_tela_inicial()

    def inicializar_tela_inicial(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Bem-vindo ao Banco UFMG", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.janela, text="Criar Conta", command=self.criar_conta, width=20).pack(pady=10)
        tk.Button(self.janela, text="Login", command=self.fazer_login, width=20).pack(pady=10)
        tk.Button(self.janela, text="Sair", command=self.janela.quit, width=20).pack(pady=10)

    def criar_conta(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Criar Conta", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Nome:").pack(pady=5)
        entrada_nome = tk.Entry(self.janela)
        entrada_nome.pack()

        tk.Label(self.janela, text="CPF:").pack(pady=5)
        entrada_cpf = tk.Entry(self.janela)
        entrada_cpf.pack()

        tk.Label(self.janela, text="Data de Nascimento (DD/MM/AAAA):").pack(pady=5)
        entrada_data_nascimento = tk.Entry(self.janela)
        entrada_data_nascimento.pack()

        tk.Label(self.janela, text="Endereço:").pack(pady=5)
        entrada_endereco = tk.Entry(self.janela)
        entrada_endereco.pack()

        tk.Label(self.janela, text="Senha:").pack(pady=5)
        entrada_senha = tk.Entry(self.janela, show="*")
        entrada_senha.pack()

        def salvar_conta():
            nome = entrada_nome.get().strip()
            cpf = entrada_cpf.get().strip()
            data_nascimento = entrada_data_nascimento.get().strip()
            endereco = entrada_endereco.get().strip()
            senha = entrada_senha.get().strip()

            if not nome or not cpf or not data_nascimento or not endereco or not senha:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                return

            if len(cpf) != 11 or not cpf.isdigit():
                messagebox.showerror("Erro", "CPF inválido. Insira 11 números.")
                return

            if not Usuario.validar_data_nascimento(data_nascimento):
                messagebox.showerror("Erro", "Data de nascimento inválida.")
                return

            if not Usuario.senha_valida(senha):
                messagebox.showerror("Erro", "Senha inválida. Verifique os requisitos.")
                return

            if Usuario.cpf_existente(cpf):
                messagebox.showerror("Erro", "CPF já cadastrado.")
                return

            numero_conta_corrente = Usuario.gerar_numero_conta_corrente()
            novo_usuario = Usuario(nome, cpf, data_nascimento, endereco, senha, numero_conta_corrente)
            Usuario.usuarios.append(novo_usuario)

            messagebox.showinfo("Sucesso", f"Conta criada com sucesso! Número da conta: {numero_conta_corrente}")
            self.inicializar_tela_inicial()

        tk.Button(self.janela, text="Salvar", command=salvar_conta, width=20).pack(pady=10)
        tk.Button(self.janela, text="Cancelar", command=self.inicializar_tela_inicial, width=20).pack(pady=10)

    def fazer_login(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Login", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.janela, text="CPF:").pack(pady=5)
        entrada_cpf = tk.Entry(self.janela)
        entrada_cpf.pack()

        tk.Label(self.janela, text="Senha:").pack(pady=5)
        entrada_senha = tk.Entry(self.janela, show="*")
        entrada_senha.pack()

        def autenticar():
            cpf = entrada_cpf.get()
            senha = entrada_senha.get()
            usuario = next((u for u in Usuario.usuarios if u.cpf == cpf and u.senha == senha), None)
            if usuario:
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                self.menu_usuario()
            else:
                messagebox.showerror("Erro", "CPF ou senha inválidos.")

        tk.Button(self.janela, text="Entrar", command=autenticar, width=20).pack(pady=10)
        tk.Button(self.janela, text="Voltar", command=self.inicializar_tela_inicial, width=20).pack(pady=10)

    def menu_usuario(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Menu do Usuário", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.janela, text="Exibir Saldo", command=lambda: messagebox.showinfo("Saldo", "Seu saldo é R$ 0,00."), width=20).pack(pady=10)
        tk.Button(self.janela, text="Realizar Transferência", command=lambda: messagebox.showinfo("Transferência", "A funcionalidade será implementada."), width=20).pack(pady=10)
        tk.Button(self.janela, text="Exibir Extrato", command=lambda: messagebox.showinfo("Extrato", "A funcionalidade será implementada."), width=20).pack(pady=10)
        tk.Button(self.janela, text="Logout", command=self.inicializar_tela_inicial, width=20).pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = BancoGUI()
    app.iniciar()
