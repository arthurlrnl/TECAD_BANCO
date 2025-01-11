import tkinter as tk
from tkinter import messagebox
from Usuario import Usuario
from SistemaBancario import SistemaBancario


class BancoGUI:
    def __init__(self):
        self.sistema = SistemaBancario()
        self.usuario_logado = None
        self.janela = tk.Tk()
        self.janela.title("Banco UFMG")
        self.janela.geometry("400x500")
        self.dados_parciais = {}
        self.inicializar_tela_inicial()

    def inicializar_tela_inicial(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.janela, text="BANCO UFMG", font=("Arial", 30), fg="blue")
        titulo.pack(pady=50)

        botao_acessar = tk.Button(self.janela, text="ACESSAR", command=self.tela_acesso, width=20, height=2)
        botao_acessar.pack(pady=20)

    def tela_acesso(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.janela, text="Acesso ao Sistema", font=("Arial", 20), fg="blue")
        titulo.pack(pady=20)

        botao_criar_conta = tk.Button(self.janela, text="Criar Conta", command=self.tela_criar_conta_passo1, width=20)
        botao_criar_conta.pack(pady=10)

        botao_login = tk.Button(self.janela, text="Entrar", command=self.tela_login, width=20)
        botao_login.pack(pady=10)

        botao_voltar = tk.Button(self.janela, text="Voltar", command=self.inicializar_tela_inicial, width=20)
        botao_voltar.pack(pady=10)

    def tela_criar_conta_passo1(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Criar Conta - Passo 1", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Nome:").pack(pady=5)
        entrada_nome = tk.Entry(self.janela)
        entrada_nome.pack()

        tk.Label(self.janela, text="CPF (somente números):").pack(pady=5)
        entrada_cpf = tk.Entry(self.janela)
        entrada_cpf.pack()

        tk.Label(self.janela, text="Data de Nascimento (DD/MM/AAAA):").pack(pady=5)
        entrada_data_nasc = tk.Entry(self.janela)
        entrada_data_nasc.pack()

        tk.Label(self.janela, text="Endereço:").pack(pady=5)
        entrada_endereco = tk.Entry(self.janela)
        entrada_endereco.pack()

        def ir_para_passo2():
            self.dados_parciais = {
                "nome": entrada_nome.get().strip(),
                "cpf": entrada_cpf.get().strip(),
                "data_nascimento": entrada_data_nasc.get().strip(),
                "endereco": entrada_endereco.get().strip()
            }
            self.tela_criar_conta_passo2()

        tk.Button(self.janela, text="Próximo", command=ir_para_passo2, width=20).pack(pady=10)
        tk.Button(self.janela, text="Cancelar", command=self.tela_acesso, width=20).pack(pady=10)

    def tela_criar_conta_passo2(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Criar Conta - Passo 2", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Senha (mín. 8 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial):").pack(pady=5)
        entrada_senha = tk.Entry(self.janela, show="*")
        entrada_senha.pack()

        tipo_usuario_var = tk.StringVar(value="Aluno")
        nivel_fump_var = tk.StringVar(value="Não sou FUMPista")
        entrada_matricula = None

        numero_matricula_frame = tk.Frame(self.janela)
        numero_matricula_frame.pack(pady=10)
        fumpista_frame = tk.Frame(self.janela)
        fumpista_frame.pack(pady=10)

        def atualizar_campos():
            nonlocal entrada_matricula
            for widget in numero_matricula_frame.winfo_children():
                widget.destroy()
            for widget in fumpista_frame.winfo_children():
                widget.destroy()

            if tipo_usuario_var.get() == "Aluno":
                tk.Label(numero_matricula_frame, text="Número de Matrícula:").pack(pady=5)
                entrada_matricula = tk.Entry(numero_matricula_frame)
                entrada_matricula.pack()

                tk.Label(fumpista_frame, text="Nível FUMP (se aplicável):").pack(pady=5)
                tk.Radiobutton(fumpista_frame, text="Não sou FUMPista", variable=nivel_fump_var, value="Não sou FUMPista").pack()
                tk.Radiobutton(fumpista_frame, text="Nível I", variable=nivel_fump_var, value="I").pack()
                tk.Radiobutton(fumpista_frame, text="Nível II", variable=nivel_fump_var, value="II").pack()
                tk.Radiobutton(fumpista_frame, text="Nível III", variable=nivel_fump_var, value="III").pack()
                tk.Radiobutton(fumpista_frame, text="Nível IV", variable=nivel_fump_var, value="IV").pack()

        tk.Radiobutton(self.janela, text="Aluno", variable=tipo_usuario_var, value="Aluno", command=atualizar_campos).pack()
        tk.Radiobutton(self.janela, text="Servidor", variable=tipo_usuario_var, value="Servidor", command=atualizar_campos).pack()
        atualizar_campos()

        def criar_conta():
            try:
                tipo = tipo_usuario_var.get()
                self.dados_parciais.update({
                    "senha": entrada_senha.get().strip(),
                    "numero_conta_corrente": Usuario.gerar_numero_conta_corrente()
                })

                if tipo == "Aluno":
                    if entrada_matricula is None:
                        raise ValueError("Número de matrícula é obrigatório para alunos.")
                    self.dados_parciais["numero_matricula"] = entrada_matricula.get().strip()
                    self.dados_parciais["fumpista"] = nivel_fump_var.get() != "Não sou FUMPista"
                    self.dados_parciais["nivel_fump"] = nivel_fump_var.get() if self.dados_parciais["fumpista"] else None
                elif tipo == "Servidor":
                    self.dados_parciais["numero_matricula"] = None
                    self.dados_parciais["fumpista"] = False
                    self.dados_parciais["nivel_fump"] = None

                self.sistema.criar_conta(tipo, self.dados_parciais)
                messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
                self.tela_login()
            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.janela, text="Criar Conta", command=criar_conta, width=20).pack(pady=10)
        tk.Button(self.janela, text="Cancelar", command=self.tela_acesso, width=20).pack(pady=10)

    def tela_login(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        tk.Label(self.janela, text="Login", font=("Arial", 20), fg="blue").pack(pady=20)

        tk.Label(self.janela, text="CPF (somente números):").pack(pady=5)
        entrada_cpf = tk.Entry(self.janela)
        entrada_cpf.pack()

        tk.Label(self.janela, text="Senha:").pack(pady=5)
        entrada_senha = tk.Entry(self.janela, show="*")
        entrada_senha.pack()

        def login():
            try:
                cpf = entrada_cpf.get().strip()
                senha = entrada_senha.get().strip()
                self.usuario_logado = self.sistema.fazer_login(cpf, senha)
                messagebox.showinfo("Sucesso", f"Bem-vindo(a), {self.usuario_logado.nome}!")
                self.tela_principal()
            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.janela, text="Entrar", command=login, width=20).pack(pady=10)
        tk.Button(self.janela, text="Cancelar", command=self.tela_acesso, width=20).pack(pady=10)
