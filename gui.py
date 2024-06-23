
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas\
#
# import os
import locale
# Definindo a localização para o Brasil (pt_BR)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Cores
cor_fundo_1 = "#F0F0F0"  # Cinza claro
cor_fundo_2 = "#4B9CD3"  # Azul
cor_fundo_3 = "#FF6347"  # Vermelho
cor_fundo_4 = "#FFFFFF"  # Branco
cor_fundo_5 = "#000000"  # Preto
cor_azul="#093254"

total = 0  # Variável global para manter o total dos valores dos itens


# Criando janela
janela = Tk()
janela.title("Minha Janela")
janela.geometry('860x920')
janela.configure(background=cor_azul)
janela.resizable(width=True, height=True)



# Frames
# frameCima = Frame(janela, width=500, height=70, bg=cor_azul, relief="flat")
# frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

# frameMeio = Frame(janela, width=500, height=300, bg=cor_fundo_4, relief="solid")
# frameMeio.grid(row=1, column=0, sticky=NSEW)

frameMeio = Frame(janela, width=400, height=50, bg=cor_fundo_4, relief="solid")
frameMeio.place(relx=0.02, rely=0, relwidth=0.96, relheight=0.5)

frameBaixo = Frame(janela, width=700, height=150, bg=cor_fundo_4, relief="raised")
frameBaixo.place(relx=0.02, rely=0.4, relwidth=0.96, relheight=0.4)
frameUltimo = Frame(janela, width=400, height=150, bg=cor_fundo_4, relief="raised")
frameUltimo.place(relx=0.02, rely=0.8, relwidth=0.96, relheight=0.15)

# # Frames Cima
# app_logo = Label(frameCima, text="Orcamentos", compound=LEFT, padx=5, anchor=NW, font=('Arial', 22))
# app_logo.place(x=10, y=20)

# Funcoes ----------------------------

# Função para gerar o arquivo do orçamento
def gerar_pdf():

    # Cria um canvas para o PDF
    c = canvas.Canvas("orcamento.pdf", pagesize=letter)

    # if (nome_cliente_entry.get() == '' or
    #     telefone_cliente_entry.get() == '' or
    #     endereco_cliente_entry.get() == '' or
    #     bairro_cidade_entry.get() == ''):
    #     messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
    #     return

 # Obtendo informações
    nome_cliente = nome_cliente_entry.get()
    telefone_cliente = telefone_cliente_entry.get()
    endereco_cliente= endereco_cliente_entry.get()
    bairro_cidade_= bairro_cidade_entry.get()
    # desc = desc_entry.get()


    # Adicionando o nome e informações da empresa
    nome_empresa = "NOME DA EMPRESA"
    endereco_empresa = "Rua: XXXXXXXXXXX Bairro: XXXXXXXXX"
    bairro_empresa = "Bairro da Empresa"
    cpf_cnpj = "CPF/CNPG: 000.000.000/0000-0"
    telefone_empresa = "(00) 0000-0000"

    # Linha decorativa abaixo do cabeçalho
    c.setStrokeColorRGB(9 / 255, 50 / 255, 84 / 255)  # Cor preta
    c.setLineWidth(20)
    c.line(0, 783, 612, 783)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(310, 735, nome_empresa)
    c.setFillColorRGB(0, 0, 0)  # Cor preta
    c.setFont("Helvetica", 12)

    c.drawString(268, 710, f"CPF/CNPJ: {cpf_cnpj}")
    c.drawString(268, 690, f"Endereço: {endereco_empresa}")
    c.drawString(268, 670, f"Telefone: {telefone_empresa}")

    # Adicionando logo
    c.drawImage('logo1.png', 50, 650, width=137, height=119)


    # Linha decorativa abaixo do cabeçalho
    c.setStrokeColorRGB(9/255, 50/255, 84/255)   # Cor preta
    c.setLineWidth(5)
    c.line(0, 640, 612, 640)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(245, 590, "ORÇAMENTO")
    c.setFont("Helvetica", 12)

    # Adicionando informações do cliente ao PDF gerado
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(0, 0, 0)  # Cor preta
    c.drawString(50, 540, "Informações do Cliente:")
    c.setFont("Helvetica", 12)
    c.drawString(70, 520, f"Nome: {nome_cliente}")
    c.drawString(70, 500, f"Telefone: {telefone_cliente}")
    c.drawString(70, 480, f"Endereco: {endereco_cliente}")
    c.drawString(70, 460, f"Bairro: {bairro_cidade_}")


    # Adicionando itens do orçamento em uma tabela
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 430, "Itens do Orçamento:")
    c.setFont("Helvetica", 12)

    vertical_pos = 400
    # Definindo larguras das colunas
    col_widths = [50, 130, 300, 380]

    # Definindo cabeçalho da tabela
    c.drawString(50, vertical_pos, "Qtd")
    c.drawString(130, vertical_pos, "Descrição")
    c.drawString(300, vertical_pos, "Preço")
    c.drawString(380, vertical_pos, "Total")

    vertical_pos -= 20

    for item in tree.get_children():
        item_values = tree.item(item, 'values')
        # Exibindo valores na tabela
        for i, value in enumerate(item_values):
            c.drawString(col_widths[i], vertical_pos, str(value))
        vertical_pos -= 30

    # Adicionando total
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, vertical_pos , f"Total: R$ {total:.2f}")

    # Mensagem de agradecimento e assinatura
    mensagem_agradecimento = "Agradecemos por nos escolher!"
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(50, vertical_pos - 30, mensagem_agradecimento)

    assinatura_empresa = "Nome do Responsável / Cargo"
    c.setFont("Helvetica-Bold", 12)
    c.drawString(400,vertical_pos - 30  , assinatura_empresa)

    # Linha decorativa abaixo do cabeçalho
    c.setStrokeColorRGB(9 / 255, 50 / 255, 84 / 255)  # Cor preta
    c.setLineWidth(20)
    c.line(0, 10, 612, 10)

    # Salva o arquivo PDF
    c.save()

    # Exibe uma mensagem informando que o PDF foi gerado com sucesso
    messagebox.showinfo("Gerar PDF", "PDF gerado com sucesso!")



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

# Função para atualizar o rótulo de total
def update_total_label():
    total_label.config(text="Total: R$ {:.2f}".format(total))


# Função para validar a entrada de telefone
def validate_phone_input(new_value):
    return new_value.isdigit() or new_value == ""

# Treeview para exibir itens adicionados ao orçamento
columns = ('Qtd', 'Descrição', 'Preço', 'Total')
tree = ttk.Treeview(frameBaixo, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW, rowspan=1)

frameBaixo.grid_rowconfigure(1, weight=1)
frameBaixo.grid_columnconfigure(0, weight=1)

# Rótulo para exibir o total
total_label = Label(frameBaixo, text="Total: R$ 0.00", font=('Arial', 12))
total_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

def clear_entries():
    nome_cliente_entry.delete(0, END)
    telefone_cliente_entry.delete(0, END)
    qty_spinbox.delete(0, END)
    desc_entry.delete(0, END)
    price_spinbox.delete(0, END)
    endereco_cliente_entry.delete(0,END)
    bairro_cidade_entry.delete(0,END)

# Labels e campos de entrada para informações do cliente
nome_cliente_label = Label(frameMeio, text="Nome:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
nome_cliente_label.place(relx=0.05, rely=0.05, anchor='w')
nome_cliente_entry = Entry(frameMeio, font=('Arial', 12))
nome_cliente_entry.place(relx=0.2, rely=0.05, relwidth=0.4, anchor='w')

endereco_cliente_label = Label(frameMeio, text="Endereço:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
endereco_cliente_label.place(relx=0.05, rely=0.15, anchor='w')
endereco_cliente_entry = Entry(frameMeio, font=('Arial', 12))
endereco_cliente_entry.place(relx=0.2, rely=0.15, relwidth=0.4, anchor='w')

bairro_cidade_label = Label(frameMeio, text="Bairro/Cidade:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
bairro_cidade_label.place(relx=0.05, rely=0.25, anchor='w')
bairro_cidade_entry = Entry(frameMeio, font=('Arial', 12))
bairro_cidade_entry.place(relx=0.2, rely=0.25, relwidth=0.4, anchor='w')

telefone_cliente_label = Label(frameMeio, text="Telefone:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
telefone_cliente_label.place(relx=0.05, rely=0.35, anchor='w')
telefone_cliente_entry = Entry(frameMeio, font=('Arial', 12), validate="key")
telefone_cliente_entry['validatecommand'] = (telefone_cliente_entry.register(validate_phone_input), '%P')
telefone_cliente_entry.place(relx=0.2, rely=0.35, relwidth=0.4, anchor='w')


# Labels e campos de entrada para adicionar itens ao orçamento usando place
qty_label = Label(frameMeio, text="Qtd:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
qty_label.place(relx=0.05, rely=0.45, anchor='w')
qty_spinbox = Spinbox(frameMeio, from_=1, to=100)
qty_spinbox.place(relx=0.2, rely=0.45, relwidth=0.4, anchor='w')

desc_label = Label(frameMeio, text="Descrição:", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
desc_label.place(relx=0.05, rely=0.55, anchor='w')
desc_entry = Entry(frameMeio, font=('Arial', 12))
desc_entry.place(relx=0.2, rely=0.55, relwidth=0.4, anchor='w')

price_label = Label(frameMeio, text="Preço (R$):", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4)
price_label.place(relx=0.05, rely=0.65, anchor='w')
price_spinbox = Spinbox(frameMeio, from_=0.0, to=500, increment=0.5)
price_spinbox.place(relx=0.2, rely=0.65, relwidth=0.4, anchor='w')

# ----------------------------------------o

# Botão para iniciar um novo orçamento
new_invoice_button = Button(frameUltimo, text="Novo", font=('Arial', 12), bg=cor_fundo_4, command=new_invoice)
new_invoice_button.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.35)


# Botão para gerar o PDF
generate_pdf_button = Button(frameUltimo, text="Gerar PDF", font=('Arial', 12), fg=cor_fundo_5, bg=cor_fundo_4, command=gerar_pdf)
generate_pdf_button.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.35)



# Botões para adicionar item e limpar orçamento
add_item_button = Button(frameMeio, text="Adicionar Item", font=('Arial', 12), command=add_item)
add_item_button.place(relx=0.3, rely=0.7, relheight=0.10)



janela.mainloop()
