import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from SistemaBancario import SistemaBancario
from Usuario import Usuario, Aluno

class BancoGUI:
    def __init__(self):
        self.sistema = SistemaBancario()  # Sistema bancário para gerenciar os usuários
        self.usuario_logado = None
        self.janela = tk.Tk()
        self.janela.title("Banco UFMG")
        self.janela.geometry("650x900")
        self.janela.resizable(False, False)
        self.janela.configure(bg="white")
        self.dados_parciais = {}
        style = ttk.Style(self.janela)
        style.theme_use("clam")
        self.inicializar_tela_inicial()

    def inicializar_tela_inicial(self):
        # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        try:
            imagem = Image.open("UFMG.jpg")
            imagem = imagem.resize((650, 300))
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            label_imagem = tk.Label(self.janela, image=self.imagem_tk, bg="white")
            label_imagem.pack(pady=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
        
        titulo = tk.Label(self.janela, text="BANCO UFMG", font=("Arial", 28, "bold"), fg="#004080", bg="white")
        titulo.pack(pady=20)
        
        # Botões de ação
        botao_acessar = tk.Button(self.janela, text="ACESSAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.tela_acesso, relief="flat")
        botao_acessar.pack(pady=20)

    def tela_acesso(self):
        # Limpa a tela inicial e adiciona os componentes da tela de acesso
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        titulo = tk.Label(self.janela, text="Tela de Acesso", font=("Arial", 22, "bold"), fg="#004080", bg="white")
        titulo.pack(pady=20)
        
        # Caixa de entrada para CPF
        label_cpf = tk.Label(self.janela, text="CPF:", font=("Arial", 12), bg="white")
        label_cpf.pack(pady=5)
        self.entry_cpf = tk.Entry(self.janela, font=("Arial", 14))
        self.entry_cpf.pack(pady=10)
        
        # Caixa de entrada para senha
        label_senha = tk.Label(self.janela, text="Senha:", font=("Arial", 12), bg="white")
        label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.janela, font=("Arial", 14), show="*")
        self.entry_senha.pack(pady=10)

        # Botões
        botao_entrar = tk.Button(self.janela, text="ENTRAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.entrar, relief="flat")
        botao_entrar.pack(pady=10)

        botao_criar_conta = tk.Button(self.janela, text="CRIAR CONTA", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.criar_conta, relief="flat")
        botao_criar_conta.pack(pady=10)

        botao_voltar = tk.Button(self.janela, text="VOLTAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.inicializar_tela_inicial, relief="flat")
        botao_voltar.pack(pady=10)
        
    def entrar(self):
        cpf = self.entry_cpf.get()
        senha = self.entry_senha.get()
        usuario = self.sistema.autenticar_usuario(cpf, senha)

        if usuario:
            self.usuario_logado = usuario
            self.sistema.usuario_logado = usuario
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.tela_dashboard()  # Redireciona para uma tela de dashboard (a ser implementada)
        else:
            messagebox.showerror("Erro", "CPF ou senha incorretos. Tente novamente.")

    def criar_conta(self):
        # Limpa a tela atual para mostrar a tela de criação de conta
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        titulo = tk.Label(self.janela, text="CRIAR CONTA", font=("Arial", 22, "bold"), fg="#004080", bg="white")
        titulo.pack(pady=20)
        
        # Campo para Nome
        label_nome = tk.Label(self.janela, text="Nome:", font=("Arial", 12), bg="white")
        label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(self.janela, font=("Arial", 14))
        self.entry_nome.pack(pady=10)
        
        # Campo para CPF
        label_cpf = tk.Label(self.janela, text="CPF:", font=("Arial", 12), bg="white")
        label_cpf.pack(pady=5)
        self.entry_cpf = tk.Entry(self.janela, font=("Arial", 14))
        self.entry_cpf.pack(pady=10)
        
        # Campo para Data de Nascimento
        label_data_nasc = tk.Label(self.janela, text="Data de Nascimento (dd/mm/yyyy):", font=("Arial", 12), bg="white")
        label_data_nasc.pack(pady=5)
        self.entry_data_nasc = tk.Entry(self.janela, font=("Arial", 14))
        self.entry_data_nasc.pack(pady=10)

        # Botão Próximo
        botao_proximo = tk.Button(self.janela, text="PRÓXIMO", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.validar_primeira_parte_cadastro, relief="flat")
        botao_proximo.pack(pady=10)

        # Botão Voltar
        botao_voltar = tk.Button(self.janela, text="VOLTAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.inicializar_tela_inicial, relief="flat")
        botao_voltar.pack(pady=10)

    def validar_primeira_parte_cadastro(self):
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        data_nasc = self.entry_data_nasc.get().strip()

        if not nome:
            messagebox.showerror("Erro", "O nome não pode ser vazio.")
            return

    # Verifica se o nome contém apenas caracteres alfabéticos e espaços
        if not nome.replace(" ", "").isalpha():
            messagebox.showerror("Erro", "O nome deve conter apenas letras.")
            return

        if not Usuario.validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido. Deve conter 11 dígitos e ser numérico.")
            return

        if not Usuario.validar_data_nascimento(data_nasc):
            messagebox.showerror("Erro", "Data de nascimento inválida. Deve estar no formato dd/mm/yyyy e ser uma data válida no passado.")
            return

    # Verificar se o CPF já existe
        if self.sistema.data_manager.verificar_cpf_existente(cpf):
            messagebox.showerror("Erro", "CPF já cadastrado no sistema.")
            return

        self.dados_parciais = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nasc
    }

    # Chama a próxima etapa do cadastro
        self.criar_conta_passo_2()

    def criar_conta_passo_2(self):
        # Limpa a tela atual para mostrar a próxima etapa do cadastro
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        titulo = tk.Label(self.janela, text="CRIAR CONTA", font=("Arial", 22, "bold"), fg="#004080", bg="white")
        titulo.pack(pady=20)

        # Seleção de tipo de usuário
        self.tipo_usuario_var = tk.StringVar(value="Aluno")
        label_tipo_usuario = tk.Label(self.janela, text="Tipo de Usuário:", font=("Arial", 12), bg="white")
        label_tipo_usuario.pack(pady=5)

        tipo_aluno = tk.Radiobutton(self.janela, text="Aluno", variable=self.tipo_usuario_var, value="Aluno", font=("Arial", 12), bg="white", command=self.atualizar_opcoes_tipo_usuario)
        tipo_aluno.pack(pady=5)

        tipo_servidor = tk.Radiobutton(self.janela, text="Servidor", variable=self.tipo_usuario_var, value="Servidor", font=("Arial", 12), bg="white", command=self.atualizar_opcoes_tipo_usuario)
        tipo_servidor.pack(pady=5)

        # Frame para opções específicas
        self.frame_opcoes = tk.Frame(self.janela, bg="white")
        self.frame_opcoes.pack(pady=10)

        # Inicializa as opções específicas para "Aluno" por padrão
        self.atualizar_opcoes_tipo_usuario()

        # Botões
        botao_proximo = tk.Button(self.janela, text="PRÓXIMO", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.validar_segunda_parte_cadastro, relief="flat")
        botao_proximo.pack(pady=10)

        botao_voltar = tk.Button(self.janela, text="VOLTAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.criar_conta, relief="flat")
        botao_voltar.pack(pady=10)

    def atualizar_opcoes_tipo_usuario(self):
        # Limpa as opções específicas atuais
        for widget in self.frame_opcoes.winfo_children():
            widget.destroy()

        tipo_usuario = self.tipo_usuario_var.get()

        if tipo_usuario == "Aluno":
            # Opções para Aluno
            self.nivel_fump_var = tk.StringVar(value="None")
            label_nivel_fump = tk.Label(self.frame_opcoes, text="Nível FUMP:", font=("Arial", 12), bg="white")
            label_nivel_fump.pack(pady=5)

            opcoes_fump = [
                ("Não é assistido pela FUMP", "None"),
                ("FUMP Nível 1", "I"),
                ("FUMP Nível 2", "II"),
                ("FUMP Nível 3", "III"),
                ("FUMP Nível 4", "IV"),
            ]

            for texto, valor in opcoes_fump:
                radio = tk.Radiobutton(self.frame_opcoes, text=texto, variable=self.nivel_fump_var, value=valor, font=("Arial", 12), bg="white")
                radio.pack(anchor="w")
                
            label_matricula = tk.Label(self.frame_opcoes, text="Número de Matrícula:", font=("Arial", 12), bg="white")
            label_matricula.pack(pady=5)
            self.entry_matricula = tk.Entry(self.frame_opcoes, font=("Arial", 14))
            self.entry_matricula.pack(pady=10)

        elif tipo_usuario == "Servidor":
            # Opção para Servidor
            label_salario = tk.Label(self.frame_opcoes, text="Salário:", font=("Arial", 12), bg="white")
            label_salario.pack(pady=5)
            self.entry_salario = tk.Entry(self.frame_opcoes, font=("Arial", 14))
            self.entry_salario.pack(pady=10)

    def validar_segunda_parte_cadastro(self):
        tipo_usuario = self.tipo_usuario_var.get()

        if tipo_usuario == "Aluno":
            nivel_fump = self.nivel_fump_var.get()
            numero_matricula = self.entry_matricula.get().strip()

            if not numero_matricula:
                messagebox.showerror("Erro", "O número de matrícula não pode ser vazio.")
                return

            self.dados_parciais["tipo"] = "Aluno"
            self.dados_parciais["nivel_fump"] = nivel_fump
            self.dados_parciais["numero_matricula"] = numero_matricula

        elif tipo_usuario == "Servidor":
            salario = self.entry_salario.get().strip()
            if not salario.isdigit():
                messagebox.showerror("Erro", "Salário deve ser um valor numérico.")
                return
            self.dados_parciais["tipo"] = "Servidor"
            self.dados_parciais["salario"] = float(salario)
            
        self.criar_conta_passo_3()

    def criar_conta_passo_3(self):
    # Limpa a tela atual para mostrar a terceira etapa do cadastro
        for widget in self.janela.winfo_children():
            widget.destroy()
    
        titulo = tk.Label(self.janela, text="CRIAR CONTA", font=("Arial", 22, "bold"), fg="#004080", bg="white")
        titulo.pack(pady=20)

    # Campo para endereço
        label_endereco = tk.Label(self.janela, text="Endereço:", font=("Arial", 12), bg="white")
        label_endereco.pack(pady=5)
        self.entry_endereco = tk.Entry(self.janela, font=("Arial", 14))
        self.entry_endereco.pack(pady=10)

    # Campo para Senha
        label_senha = tk.Label(self.janela, text="Senha:", font=("Arial", 12), bg="white")
        label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.janela, font=("Arial", 14), show="*")
        self.entry_senha.pack(pady=10)

    # Campo para Confirmar Senha
        label_confirmar_senha = tk.Label(self.janela, text="Confirmar Senha:", font=("Arial", 12), bg="white")
        label_confirmar_senha.pack(pady=5)
        self.entry_confirmar_senha = tk.Entry(self.janela, font=("Arial", 14), show="*")
        self.entry_confirmar_senha.pack(pady=10)

    # Botões
        botao_finalizar = tk.Button(self.janela, text="FINALIZAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.finalizar_cadastro, relief="flat")
        botao_finalizar.pack(pady=10)

        botao_voltar = tk.Button(self.janela, text="VOLTAR", font=("Arial", 14, "bold"), fg="white", bg="#004080", activebackground="#002060", activeforeground="white", width=20, height=2, command=self.criar_conta_passo_2, relief="flat")
        botao_voltar.pack(pady=10)

    def finalizar_cadastro(self):
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()
        endereco = self.entry_endereco.get().strip()

    # Verifica se o endereço foi preenchido
        if not endereco:
            messagebox.showerror("Erro", "O endereço não pode estar vazio.")
            return

    # Verifica se as senhas coincidem
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        try:
        # Valida a senha usando o método do SistemaBancario
            self.sistema.validar_senha(senha)

        # Gerar número de conta corrente único
            numero_conta = Usuario.gerar_numero_conta_corrente()

        # Atualizar dados parciais com as informações finais
            self.dados_parciais.update({
                "senha": senha,
                "numero_conta_corrente": numero_conta,
                "endereco": endereco
        })

        # Criar conta no sistema
            self.sistema.criar_conta(self.dados_parciais["tipo"], self.dados_parciais)
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        
        # Voltar para a tela de login
            self.tela_acesso()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            
    def tela_dashboard(self):
    # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()
        
    # Cabeçalho com boas-vindas
        frame_header = tk.Frame(self.janela, bg="white")
        frame_header.pack(fill="x", padx=20, pady=20)
    
        bemvindo_label = tk.Label(
            frame_header, 
            text=f"Bem-vindo(a), {self.usuario_logado.nome}",
            font=("Arial", 24, "bold"),
            fg="#004080",
            bg="white"
    )
        bemvindo_label.pack(anchor="w")
    
    # Frame para informações da conta
        frame_conta = tk.Frame(self.janela, bg="white", relief="solid", borderwidth=1)
        frame_conta.pack(fill="x", padx=20, pady=10)
    
    # Saldo atual
        saldo_label = tk.Label(
            frame_conta,
            text="Saldo atual:",
            font=("Arial", 14),
            bg="white"
    )   
        saldo_label.pack(anchor="w", padx=10, pady=5)
    
        saldo_valor = tk.Label(
            frame_conta,
            text=f"R$ {self.usuario_logado.saldo.saldo:.2f}",
            font=("Arial", 24, "bold"),
            fg="#004080",
            bg="white"
    )
        saldo_valor.pack(anchor="w", padx=10, pady=5)
    
    # Frame para botões de ações
        frame_acoes = tk.Frame(self.janela, bg="white")
        frame_acoes.pack(fill="x", padx=20, pady=20)
        
        carteirinha_label = tk.Label(
            frame_conta,
            text="Saldo carteirinha RU:",
            font=("Arial", 14),
            bg="white"
            )   
        carteirinha_label.pack(anchor="w", padx=10, pady=5)

        carteirinha_valor = tk.Label(
            frame_conta,
            text=f"R$ {self.usuario_logado.carteirinha.saldo_carteirinha:.2f}",
            font=("Arial", 24, "bold"),
            fg="#004080",
            bg="white"
            )
        carteirinha_valor.pack(anchor="w", padx=10, pady=5)

# Frame para botões de ações
        frame_acoes = tk.Frame(self.janela, bg="white")
        frame_acoes.pack(fill="x", padx=20, pady=20)
        
        botao_deposito = tk.Button(
            frame_acoes,
            text="Realizar Depósito",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
           activeforeground="white",
           width=20,
           height=2,
           command=self.tela_deposito,
           relief="flat"
    )
        botao_deposito.pack(pady=10)
    
    # Botão de transferência
        botao_transferencia = tk.Button(
            frame_acoes,
            text="Realizar Transferência",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_transferencia,
            relief="flat"
    )
        botao_transferencia.pack(pady=10)
        
        botao_recarregar = tk.Button(
            frame_acoes,
            text="Recarregar Carteirinha",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_recarga_carteirinha,
            relief="flat"
            )
        botao_recarregar.pack(pady=10)

        botao_liberar = tk.Button(
            frame_acoes,
            text="Liberar Catraca RU",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.liberar_catraca,
            relief="flat"
            )
        botao_liberar.pack(pady=10)
        
        botao_emprestimo = tk.Button(
            frame_acoes,
            text="Solicitar Empréstimo",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_emprestimo,
            relief="flat"
            )
        botao_emprestimo.pack(pady=10)
        
        botao_extrato = tk.Button(
            frame_acoes,
            text="Visualizar Extrato",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
        command=self.tela_extrato,
        relief="flat"
        )
        botao_extrato.pack(pady=10)

        botao_sair = tk.Button(
            frame_acoes,
            text="Sair",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#800000",
            activebackground="#600000",
            activeforeground="white",
            width=20,
            height=2,
            command=self.inicializar_tela_inicial,
            relief="flat"
            )
        botao_sair.pack(pady=10)

    def tela_transferencia(self):
    # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        titulo = tk.Label(
            self.janela,
            text="Realizar Transferência",
            font=("Arial", 22, "bold"),
            fg="#004080",
            bg="white"
    )
        titulo.pack(pady=20)
    
    # Frame para o formulário
        frame_form = tk.Frame(self.janela, bg="white")
        frame_form.pack(pady=20)
    
    # CPF do destinatário
        label_cpf = tk.Label(
            frame_form,
            text="CPF do destinatário:",
            font=("Arial", 12),
            bg="white"
    )
        label_cpf.pack(pady=5)
        self.entry_cpf_destino = tk.Entry(frame_form, font=("Arial", 14))
        self.entry_cpf_destino.pack(pady=10)
    
    # Valor da transferência
        label_valor = tk.Label(
            frame_form,
            text="Valor da transferência:",
            font=("Arial", 12),
            bg="white"
    )
        label_valor.pack(pady=5)
        self.entry_valor = tk.Entry(frame_form, font=("Arial", 14))
        self.entry_valor.pack(pady=10)
    
    # Senha para confirmar
        label_senha = tk.Label(
            frame_form,
            text="Sua senha:",
            font=("Arial", 12),
            bg="white"
    )
        label_senha.pack(pady=5)
        self.entry_senha_transf = tk.Entry(frame_form, font=("Arial", 14), show="*")
        self.entry_senha_transf.pack(pady=10)
    
    # Botões
        botao_confirmar = tk.Button(
            frame_form,
            text="Confirmar Transferência",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.executar_transferencia,
            relief="flat"
    )
        botao_confirmar.pack(pady=10)
    
        botao_voltar = tk.Button(
            frame_form,
            text="Voltar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_dashboard,
            relief="flat"
    )
        botao_voltar.pack(pady=10)

    def executar_transferencia(self):
        try:
            cpf_destino = self.entry_cpf_destino.get().strip()
            valor = float(self.entry_valor.get().strip())
            senha = self.entry_senha_transf.get()
        
        # Realiza a transferência usando o sistema
            self.sistema.realizar_transferencia(cpf_destino, valor, senha)
        
            messagebox.showinfo("Sucesso", "Transferência realizada com sucesso!")
            self.tela_dashboard()  # Volta para o dashboard
        
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            
    def tela_deposito(self):
    # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()
    
        titulo = tk.Label(
            self.janela,
            text="Realizar Depósito",
            font=("Arial", 22, "bold"),
            fg="#004080",
            bg="white"
    )
        titulo.pack(pady=20)

    # Frame para o formulário
        frame_form = tk.Frame(self.janela, bg="white")
        frame_form.pack(pady=20)

    # Valor do depósito
        label_valor = tk.Label(
            frame_form,
            text="Valor do depósito:",
            font=("Arial", 12),
            bg="white"
    )
        label_valor.pack(pady=5)
        self.entry_valor_deposito = tk.Entry(frame_form, font=("Arial", 14))
        self.entry_valor_deposito.pack(pady=10)

    # Senha para confirmar
        label_senha = tk.Label(
            frame_form,
            text="Sua senha:",
            font=("Arial", 12),
            bg="white"
    )
        label_senha.pack(pady=5)
        self.entry_senha_deposito = tk.Entry(frame_form, font=("Arial", 14), show="*")
        self.entry_senha_deposito.pack(pady=10)

    # Botões
        botao_confirmar = tk.Button(
            frame_form,
            text="Confirmar Depósito",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.executar_deposito,
            relief="flat"
    )
        botao_confirmar.pack(pady=10)

        botao_voltar = tk.Button(
            frame_form,
            text="Voltar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_dashboard,
            relief="flat"
    )
        botao_voltar.pack(pady=10)

    def executar_deposito(self):
        try:
            valor = float(self.entry_valor_deposito.get().strip())
            senha = self.entry_senha_deposito.get()

        # Verificar senha
            if not self.usuario_logado.validar_senha(senha):
                messagebox.showerror("Erro", "Senha incorreta.")
                return

        # Verificar valor positivo
            if valor <= 0:
                messagebox.showerror("Erro", "O valor do depósito deve ser positivo.")
                return

        # Realizar o depósito
            self.usuario_logado.saldo.creditar(valor)
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            self.tela_dashboard()

        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número válido.")

    def tela_recarga_carteirinha(self):
    # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()
    
        titulo = tk.Label(
            self.janela,
            text="Recarregar Carteirinha",
            font=("Arial", 22, "bold"),
            fg="#004080",
            bg="white"
    )
        titulo.pack(pady=20)

    # Frame para o formulário
        frame_form = tk.Frame(self.janela, bg="white")
        frame_form.pack(pady=20)

    # Exibir saldo atual
        saldo_atual_label = tk.Label(
            frame_form,
            text=f"Saldo atual da carteirinha: R$ {self.usuario_logado.carteirinha.saldo_carteirinha:.2f}",
            font=("Arial", 12),
            bg="white"
    )
        saldo_atual_label.pack(pady=10)

    # Valor da recarga
        label_valor = tk.Label(
            frame_form,
            text="Valor da recarga:",
            font=("Arial", 12),
            bg="white"
    )
        label_valor.pack(pady=5)
        self.entry_valor_recarga = tk.Entry(frame_form, font=("Arial", 14))
        self.entry_valor_recarga.pack(pady=10)

    # Senha para confirmar
        label_senha = tk.Label(
            frame_form,
            text="Sua senha:",
            font=("Arial", 12),
            bg="white"
    )
        label_senha.pack(pady=5)
        self.entry_senha_recarga = tk.Entry(frame_form, font=("Arial", 14), show="*")
        self.entry_senha_recarga.pack(pady=10)

    # Botões
        botao_confirmar = tk.Button(
            frame_form,
            text="Confirmar Recarga",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.executar_recarga_carteirinha,
            relief="flat"
    )
        botao_confirmar.pack(pady=10)

        botao_voltar = tk.Button(
            frame_form,
            text="Voltar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_dashboard,
            relief="flat"
    )
        botao_voltar.pack(pady=10)

    def executar_recarga_carteirinha(self):
        try:
            valor = float(self.entry_valor_recarga.get().strip())
            senha = self.entry_senha_recarga.get()

        # Verificar senha
            if not self.usuario_logado.validar_senha(senha):
                messagebox.showerror("Erro", "Senha incorreta.")
                return

        # Verificar valor positivo
            if valor <= 0:
                messagebox.showerror("Erro", "O valor da recarga deve ser positivo.")
                return

        # Verificar se tem saldo suficiente na conta
            if self.usuario_logado.saldo.saldo < valor:
                messagebox.showerror("Erro", "Saldo insuficiente na conta bancária.")
                return

        # Realizar a recarga
            self.usuario_logado.saldo.debitar(valor)
            self.usuario_logado.carteirinha.adicionar_saldo(valor)
        
        # Salvar os dados atualizados
            self.sistema._salvar_dados()
        
            messagebox.showinfo("Sucesso", f"Recarga de R$ {valor:.2f} realizada com sucesso!")
            self.tela_dashboard()

        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número válido.")

    def liberar_catraca(self):
        try:
        # Verifica se tem saldo suficiente
            if isinstance(self.usuario_logado, Aluno):
                categoria = self.usuario_logado.nivel_fump
            else:
                categoria = "Professor"
        
            resultado = self.usuario_logado.carteirinha.liberar_catraca(categoria)
    
            if "insuficiente" in resultado:
                messagebox.showerror("Erro", resultado)
            else:
            # Salvar os dados atualizados
                self.sistema._salvar_dados()
                messagebox.showinfo("Sucesso", resultado)
                self.tela_dashboard()
            
        except Exception as e:  # Fixed indentation
            messagebox.showerror("Erro", str(e))
        
    def tela_emprestimo(self):
    # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        self.janela.configure(bg="white")
    
        titulo = tk.Label(
            self.janela,
            text="Solicitar Empréstimo",
            font=("Arial", 22, "bold"),
            fg="#004080",
            bg="white"
    )
        titulo.pack(pady=20)

    # Verifica se já existe empréstimo ativo
        if self.usuario_logado.tem_emprestimo_ativo:
            mensagem = tk.Label(
                self.janela,
                text="Você já possui um empréstimo ativo.\nNão é possível solicitar outro empréstimo.",
                font=("Arial", 14),
                fg="red",
                bg="white"
        )
            mensagem.pack(pady=20)
        
        # Botão voltar
            botao_voltar = tk.Button(
                self.janela,
                text="Voltar",
                font=("Arial", 12, "bold"),
                fg="white",
                bg="#004080",
                activebackground="#002060",
                activeforeground="white",
                width=20,
                height=2,
                command=self.tela_dashboard,
                relief="flat"
        )
            botao_voltar.pack(pady=10)
            return

    # Frame para o formulário
        frame_form = tk.Frame(self.janela, bg="white")
        frame_form.pack(pady=20)

    # Tipo de empréstimo
        label_tipo = tk.Label(
            frame_form,
            text="Tipo de Empréstimo:",
            font=("Arial", 12),
            bg="white"
    )
        label_tipo.pack(pady=5)

        self.tipo_emprestimo_var = tk.StringVar(value="Estudantil" if isinstance(self.usuario_logado, Aluno) else "Pessoal")
        tipo_emprestimo = tk.Label(
        frame_form,
        text=self.tipo_emprestimo_var.get(),
        font=("Arial", 14),
        bg="white"
    )
        tipo_emprestimo.pack(pady=10)

    # Valor do empréstimo
        label_valor = tk.Label(
            frame_form,
            text="Valor do empréstimo:",
            font=("Arial", 12),
            bg="white"
    )
        label_valor.pack(pady=5)
        self.entry_valor_emprestimo = tk.Entry(frame_form, font=("Arial", 14))
        self.entry_valor_emprestimo.pack(pady=10)

    # Número de parcelas
        label_parcelas = tk.Label(
            frame_form,
            text="Número de parcelas (1-24):",
            font=("Arial", 12),
            bg="white"
    )   
        label_parcelas.pack(pady=5)
        self.entry_parcelas = tk.Entry(frame_form, font=("Arial", 14))
        self.entry_parcelas.pack(pady=10)

    # Senha para confirmar
        label_senha = tk.Label(
            frame_form,
            text="Sua senha:",
            font=("Arial", 12),
            bg="white"
    )
        label_senha.pack(pady=5)
        self.entry_senha_emprestimo = tk.Entry(frame_form, font=("Arial", 14), show="*")
        self.entry_senha_emprestimo.pack(pady=10)

    # Botões
        botao_simular = tk.Button(
            frame_form,
            text="Simular Empréstimo",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.simular_emprestimo,
            relief="flat"
    )
        botao_simular.pack(pady=10)

        botao_confirmar = tk.Button(
            frame_form,
            text="Confirmar Empréstimo",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.executar_emprestimo,
            relief="flat"
    )
        botao_confirmar.pack(pady=10)

        botao_voltar = tk.Button(
            frame_form,
            text="Voltar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_dashboard,
            relief="flat"
    )
        botao_voltar.pack(pady=10)

    def simular_emprestimo(self):
        try:
            valor = float(self.entry_valor_emprestimo.get().strip())
            parcelas = int(self.entry_parcelas.get().strip())
        
            if parcelas < 1 or parcelas > 24:
                messagebox.showerror("Erro", "O número de parcelas deve estar entre 1 e 24.")
                return
            
            if valor <= 0:
                messagebox.showerror("Erro", "O valor do empréstimo deve ser positivo.")
                return

            taxa = 0.02 if isinstance(self.usuario_logado, Aluno) else 0.05
            valor_total = valor * (1 + taxa * parcelas)
            valor_parcela = valor_total / parcelas

            mensagem = f"""Simulação de Empréstimo:
                Valor solicitado: R$ {valor:.2f}
                Número de parcelas: {parcelas}
                Taxa de juros mensal: {taxa*100:.1f}%
                Valor total a pagar: R$ {valor_total:.2f}
                Valor de cada parcela: R$ {valor_parcela:.2f}"""
        
            messagebox.showinfo("Simulação de Empréstimo", mensagem)
        
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def executar_emprestimo(self):
        try:
            valor = float(self.entry_valor_emprestimo.get().strip())
            parcelas = int(self.entry_parcelas.get().strip())
            senha = self.entry_senha_emprestimo.get()

        # Verificar senha
            if not self.usuario_logado.validar_senha(senha):
               messagebox.showerror("Erro", "Senha incorreta.")
               return

        # Validar número de parcelas
            if parcelas < 1 or parcelas > 24:
                messagebox.showerror("Erro", "O número de parcelas deve estar entre 1 e 24.")
                return

        # Validar valor do empréstimo
            if valor <= 0:
                messagebox.showerror("Erro", "O valor do empréstimo deve ser positivo.")
                return

            tipo = "Estudantil" if isinstance(self.usuario_logado, Aluno) else "Pessoal"
        
        # Solicitar empréstimo através do sistema bancário
            emprestimo = self.sistema.solicitar_emprestimo(tipo, valor, parcelas)
        
            if emprestimo:
                self.usuario_logado._emprestimo_ativo = True
                self.usuario_logado._valor_emprestimo = valor
                self.usuario_logado._parcelas_restantes = parcelas
                self.usuario_logado.iniciar_emprestimo(valor, parcelas)
                messagebox.showinfo("Sucesso", "Empréstimo aprovado e processado com sucesso!")
                self.tela_dashboard()
            
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            
    def tela_extrato(self):
    # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.janela,
            text="Extrato da Conta",
            font=("Arial", 22, "bold"),
            fg="#004080",
            bg="white"
    )
        titulo.pack(pady=20)

    # Frame para exibir o extrato
        frame_extrato = tk.Frame(self.janela, bg="white")
        frame_extrato.pack(pady=20, padx=20, fill="both", expand=True)

    # Criar um widget Text para exibir o extrato
        texto_extrato = tk.Text(
            frame_extrato,
            font=("Courier", 12),
            bg="white",
            wrap=tk.WORD,
            height=20,
            width=60
    )
        texto_extrato.pack(side=tk.LEFT, fill="both", expand=True)

    # Adicionar scrollbar
        scrollbar = tk.Scrollbar(frame_extrato)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurar scrollbar
        texto_extrato.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=texto_extrato.yview)

    # Obter o extrato do usuário
        extrato = self.sistema.exibir_extrato()
    
    # Inserir o conteúdo no widget Text
        texto_extrato.insert(tk.END, extrato)
        texto_extrato.config(state=tk.DISABLED)  # Torna o texto não editável

    # Frame para os botões
        frame_botoes = tk.Frame(self.janela, bg="white")
        frame_botoes.pack(pady=20)

    # Botões de filtro
        frame_filtros = tk.Frame(self.janela, bg="white")
        frame_filtros.pack(pady=10)

    # Botão voltar
        botao_voltar = tk.Button(
            frame_botoes,
            text="Voltar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#004080",
            activebackground="#002060",
            activeforeground="white",
            width=20,
            height=2,
            command=self.tela_dashboard,
            relief="flat"
    )
        botao_voltar.pack(pady=10)

    def filtrar_extrato(self, texto_extrato, filtro):
    # Obter o extrato filtrado
        extrato_filtrado = self.sistema.exibir_extrato(filtro)
    
    # Limpar o texto atual
        texto_extrato.config(state=tk.NORMAL)
        texto_extrato.delete(1.0, tk.END)
    
    # Inserir o novo texto filtrado
        texto_extrato.insert(tk.END, extrato_filtrado)
        texto_extrato.config(state=tk.DISABLED)
