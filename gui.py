from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Cores
cor_fundo_1 = "#F0F0F0"  # Cinza claro
cor_fundo_2 = "#4B9CD3"  # Azul
cor_fundo_3 = "#FF6347"  # Vermelho
cor_fundo_4 = "#FFFFFF"  # Branco
cor_fundo_5 = "#000000"  # Preto

total = 0  # Variável global para manter o total dos valores dos itens

# Função para limpar campos de entrada de item
def clear_item():
    qty_spinbox.delete(0, END)
    qty_spinbox.insert(0, "1")
    desc_entry.delete(0, END)
    price_spinbox.delete(0, END)
    price_spinbox.insert(0, "0.0")

# Função para adicionar um item ao orçamento
def add_item():
    global total
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty * price
    total += line_total
    invoice_item = [qty, desc, price, line_total]
    tree.insert('', END, values=invoice_item)
    clear_item()
    update_total_label()

# Função para limpar a janela e iniciar um novo orçamento
def new_invoice():
    global total
    tree.delete(*tree.get_children())
    total = 0
    update_total_label()
    clear_entries()

# Função para gerar o arquivo do orçamento
def gerar_pdf():
    if (first_name_entry.get() == '' or
            last_name_entry.get() == '' or
            phone_entry.get() == ''):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    # obtendo info
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone = phone_entry.get()

    # Cria um canvas para o PDF
    c = canvas.Canvas("orcamento.pdf", pagesize=letter)

    # Desenhando borda azul ao redor do cabeçalho
    c.setStrokeColorRGB(0.2, 0.4, 0.8)  # Cor azul clara
    c.setLineWidth(2)
    c.rect(0, 720, 612, 100)  # Borda azul ao redor do cabeçalho

    # Retângulo azul claro para o cabeçalho
    # c.setFillColorRGB(0.2, 0.4, 0.8)  # AZUL CLARO
    # c.rect(0, 720, 612, 100, fill=1)  # Coordenadas: (x, y, largura, altura)

    # Adicionando o nome e informações da empresa
    nome_empresa = "Nome da Empresa"
    endereco_empresa = "Endereço da Empresa"
    cpf_cnpj = "CPF/CNPG: 000.000.000/0000-0"
    telefone_empresa = "(00) 0000-0000"
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(1, 1, 1)  # Cor branca
    c.setFont("Helvetica", 12)
    c.drawString(220, 760, nome_empresa)
    c.drawString(220, 740, f"CPF/CNPJ: {cpf_cnpj}")
    c.drawString(220, 720, f"Endereço: {endereco_empresa}")
    c.drawString(220, 700, f"Telefone: {telefone_empresa}")

    # Adicionando logo
    c.drawImage('logo1.png', 50, 725, width=150, height=60)

    # Linha decorativa abaixo do cabeçalho
    c.setStrokeColorRGB(0, 0, 0)  # Cor preta
    c.setLineWidth(1)
    c.line(50, 720, 562, 720)

    # Adicionando informações do cliente ao PDF gerado
    nome_cliente = nome_cliente_entry.get()
    endereco_cliente = endereco_cliente_entry.get()
    bairro_cidade = bairro_cidade_entry.get()
    telefone_cliente = telefone_cliente_entry.get()

    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(0, 0, 0)  # Cor preta
    c.drawString(50, 670, "Informações do Cliente:")
    c.setFont("Helvetica", 12)
    c.drawString(70, 650, f"Nome: {nome_cliente}")
    c.drawString(70, 630, f"Endereço: {endereco_cliente}")
    c.drawString(70, 610, f"Bairro/Cidade: {bairro_cidade}")
    c.drawString(70, 590, f"Telefone: {telefone_cliente}")

    # Adicionando itens do orçamento em uma tabela
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 600, "Itens do Orçamento:")
    c.setFont("Helvetica", 12)

    vertical_pos = 580
    # Definindo larguras das colunas
    col_widths = [50, 250, 80, 100]

    # Definindo cabeçalho da tabela
    c.drawString(50, vertical_pos, "Qtd")
    c.drawString(120, vertical_pos, "Descrição")
    c.drawString(300, vertical_pos, "Preço")
    c.drawString(380, vertical_pos, "Total")

    vertical_pos -= 20

    # Desenhando linhas horizontais e verticais da tabela
    c.setStrokeColorRGB(0, 0, 0)  # Cor preta
    c.setLineWidth(1)
    c.line(50, vertical_pos, 480, vertical_pos)  # Linha do cabeçalho
    c.line(50, vertical_pos - 20, 480, vertical_pos - 20)  # Linha abaixo do cabeçalho
    c.line(50, vertical_pos, 50, vertical_pos - 20)  # Linha vertical da coluna "Qtd"
    c.line(120, vertical_pos, 120, vertical_pos - 20)  # Linha vertical da coluna "Descrição"
    c.line(300, vertical_pos, 300, vertical_pos - 20)  # Linha vertical da coluna "Preço"
    c.line(380, vertical_pos, 380, vertical_pos - 20)  # Linha vertical da coluna "Total"

    for item in tree.get_children():
        item_values = tree.item(item, 'values')
        # Exibindo valores na tabela
        for i, value in enumerate(item_values):
            c.drawString(col_widths[i], vertical_pos, str(value))
        vertical_pos -= 20

    # Desenhando linhas horizontais das células da tabela
    c.line(50, vertical_pos, 480, vertical_pos)  # Linha após os valores dos itens
    c.line(50, vertical_pos - 20, 480, vertical_pos - 20)  # Linha abaixo dos valores dos itens

    # Adicionando total
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, vertical_pos - 20, f"Total: R$ {total:.2f}")

    # Mensagem de agradecimento e assinatura
    mensagem_agradecimento = "Agradecemos o seu comprometimento e dedicação!"
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(50, 370, mensagem_agradecimento)

    assinatura_empresa = "Nome do Responsável / Cargo"
    c.setFont("Helvetica-Bold", 12)
    c.drawString(380, 340, assinatura_empresa)

    # Exibe uma mensagem informando que o PDF foi gerado com sucesso
    messagebox.showinfo("Gerar PDF", "PDF gerado com sucesso!")



# Função para atualizar o rótulo de total
def update_total_label():
    total_label.config(text="Total: R$ {:.2f}".format(total))

# Função para validar a entrada de telefone
def validate_phone_input(new_value):
    return new_value.isdigit() or new_value == ""
# Salva o arquivo PDF
    c.save()
# Criando janela
janela = Tk()
janela.title("Minha Janela")
janela.geometry('820x750')
janela.configure(background=cor_fundo_4)
janela.resizable(width=False, height=False)

# Frames
frameCima = Frame(janela, width=500, height=70, bg=cor_fundo_2, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameMeio = Frame(janela, width=500, height=300, bg=cor_fundo_4, relief="solid")
frameMeio.grid(row=1, column=0, sticky=NSEW)

frameBaixo = Frame(janela, width=500, height=150, bg=cor_fundo_2, relief="raised")
frameBaixo.grid(row=2, column=0, pady=10, sticky=NSEW)

# Frames Cima
app_logo = Label(frameCima, text="Orcamentos", compound=LEFT, padx=5, anchor=NW, font=('Arial', 22), bg=cor_fundo_2, fg=cor_fundo_4)
app_logo.place(x=10, y=20)

# Labels e campos de entrada para informações do cliente
nome_cliente_label = Label(frameMeio, text="Nome:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
nome_cliente_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
nome_cliente_entry = Entry(frameMeio, font=('Arial', 12))
nome_cliente_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

endereco_cliente_label = Label(frameMeio, text="Endereço:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
endereco_cliente_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
endereco_cliente_entry = Entry(frameMeio, font=('Arial', 12))
endereco_cliente_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

bairro_cidade_label = Label(frameMeio, text="Bairro/Cidade:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
bairro_cidade_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
bairro_cidade_entry = Entry(frameMeio, font=('Arial', 12))
bairro_cidade_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

telefone_cliente_label = Label(frameMeio, text="Telefone:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
telefone_cliente_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
telefone_cliente_entry = Entry(frameMeio, font=('Arial', 12), validate="key")
telefone_cliente_entry['validatecommand'] = (telefone_cliente_entry.register(validate_phone_input), '%P')
telefone_cliente_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


# Labels e campos de entrada para adicionar itens ao orçamento
qty_label = Label(frameMeio, text="Qtd:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
qty_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)
qty_spinbox = Spinbox(frameMeio, from_=1, to=100)
qty_spinbox.grid(row=5, column=1, padx=10, pady=5, sticky=W)

desc_label = Label(frameMeio, text="Descrição:", font=('Arial', 12),fg=cor_fundo_5, bg=cor_fundo_4)
desc_label.grid(row=6, column=0, padx=10, pady=5, sticky=W)
desc_entry = Entry(frameMeio, font=('Arial', 12))
desc_entry.grid(row=6, column=1, padx=10, pady=5, sticky=W)

price_label = Label(frameMeio, text="Preço (R$):", font=('Arial', 12),fg=cor_fundo_5, bg=cor_fundo_4)
price_label.grid(row=7, column=0, padx=10, pady=5, sticky=W)
price_spinbox = Spinbox(frameMeio, from_=0.0, to=500, increment=0.5)
price_spinbox.grid(row=7, column=1, padx=10, pady=5, sticky=W)

# Botões para adicionar item e limpar orçamento
add_item_button = Button(frameMeio, text="Adicionar Item", font=('Arial', 12), command=add_item)
add_item_button.grid(row=9, column=1,  padx=10, pady=10)

## Treeview para exibir itens adicionados ao orçamento
columns = ('Qtd', 'Descrição', 'Preço', 'Total')
tree = ttk.Treeview(frameBaixo, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

# Rótulo para exibir o total
total_label = Label(frameBaixo, text="Total: R$ 0.00", font=('Arial', 12), bg=cor_fundo_2, fg=cor_fundo_4)
total_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

def clear_entries():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0, END)
    qty_spinbox.delete(0, END)
    desc_entry.delete(0, END)
    price_spinbox.delete(0, END)

# Função para iniciar um novo orçamento

# Botão para iniciar um novo orçamento
new_invoice_button = Button(frameBaixo, text="Novo", font=('Arial', 12), bg=cor_fundo_4, command=new_invoice)
new_invoice_button.grid(row=3, column=0, padx=10, pady=10)

# Botão para gerar o PDF
generate_pdf_button = Button(frameBaixo, text="Gerar PDF", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4, command=gerar_pdf)
generate_pdf_button.grid(row=4, column=0, padx=10, pady=10)

janela.mainloop()
