from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_pdf():
    # Cria um canvas para o PDF
    c = canvas.Canvas("orcamento_teste.pdf", pagesize=letter)

    # Retângulo azul claro para o cabeçalho
    c.setFillColorRGB(0.2, 0.4, 0.8)  # AZUL CLARO
    c.rect(0, 720, 612, 100, fill=1)  # Coordenadas: (x, y, largura, altura)

    # Adicionando o nome e informações da empresa
    nome_empresa = "Nome da Empresa"
    endereco_empresa = "Endereço da Empresa"
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(1, 1, 1)  # Cor branca
    c.drawString(220, 760, nome_empresa)
    c.setFont("Helvetica", 12)
    c.drawString(220, 740, endereco_empresa)

    # Linha decorativa abaixo do cabeçalho
    c.setStrokeColorRGB(0, 0, 0)  # Cor preta
    c.setLineWidth(1)
    c.line(50, 720, 562, 720)

    # Adicionando logo
    c.drawImage('logo.png', 50, 725, width=150, height=60)

    # Linha decorativa abaixo dos descontos
    c.setStrokeColorRGB(0, 0, 0)  # Cor preta
    c.setLineWidth(1)
    c.line(50, 400, 562, 400)

    # Adicionando informações do cliente (simulação de dados)
    first_name = "João"
    last_name = "Silva"
    phone = "123456789"

    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(0, 0, 0)  # Cor preta
    c.drawString(50, 670, "Informações do Cliente:")
    c.setFont("Helvetica", 12)
    c.drawString(70, 650, f"Nome: {first_name} {last_name}")
    c.drawString(70, 630, f"Telefone: {phone}")

    # Adicionando itens do orçamento em uma tabela
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 600, "Itens do Orçamento:")
    c.setFont("Helvetica", 12)

    vertical_pos = 580
    # Definindo larguras das colunas
    col_widths = [50, 250, 80, 100]

    # Desenhando linhas horizontais da tabela
    c.setStrokeColorRGB(0, 0, 0)  # Cor preta
    c.setLineWidth(1)
    c.line(50, vertical_pos, sum(col_widths), vertical_pos)  # Linha do cabeçalho
    c.line(50, vertical_pos - 20, sum(col_widths), vertical_pos - 20)  # Linha abaixo do cabeçalho

    # Definindo cabeçalho da tabela
    c.drawString(70, vertical_pos, "Qtd")
    c.drawString(120, vertical_pos, "Descrição")
    c.drawString(300, vertical_pos, "Preço")
    c.drawString(380, vertical_pos, "Total")

    vertical_pos -= 20

    # Desenhando linhas verticais da tabela
    c.line(70, vertical_pos, 70, vertical_pos + 20)  # Linha vertical da coluna "Qtd"
    c.line(300, vertical_pos, 300, vertical_pos + 20)  # Linha vertical da coluna "Preço"
    c.line(380, vertical_pos, 380, vertical_pos + 20)  # Linha vertical da coluna "Total"

    # Adicionando itens fictícios ao orçamento (simulação de dados)
    items = [
        [1, "Item 1", 10.00, 10.00],
        [2, "Item 2", 15.00, 30.00],
        [3, "Item 3", 20.00, 60.00]
    ]

    for item in items:
        # Exibindo valores na tabela
        for i, value in enumerate(item):
            c.drawString(70 + sum(col_widths[:i]), vertical_pos, str(value))

        vertical_pos -= 20

    # Desenhando linhas horizontais das células da tabela
    vertical_pos -= 20
    c.line(50, vertical_pos, sum(col_widths), vertical_pos)  # Linha após os valores dos itens
    c.line(50, vertical_pos - 20, sum(col_widths), vertical_pos - 20)  # Linha abaixo dos valores dos itens

    # Adicionando total (simulação de dados)
    total = sum([item[3] for item in items])
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, vertical_pos - 20, f"Total: R$ {total:.2f}")

    # Salva o arquivo PDF
    c.save()

# Chama a função para gerar o PDF
gerar_pdf()
