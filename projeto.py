from fpdf import FPDF

def gerar_pdf(projeto, horas_previstas, valor_hora, prazo, valor_total, contador):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")

    pdf.image("template.png", x=0, y=0)

    pdf.text(115, 145, projeto)
    pdf.text(115, 160, horas_previstas)
    pdf.text(115, 175, valor_hora)
    pdf.text(115, 190, prazo)
    pdf.text(115, 205, str(valor_total))

    filename = f"Orçamento_{contador}.pdf"
    pdf.output(filename)
    print(f"Orçamento gerado com sucesso! Arquivo salvo como: {filename}")

def main():
    contador = 1
    while True:
        print("Escolha uma opção:")
        print("1- Gerar PDF")
        print("2- Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            projeto = input("Digite a descrição do projeto: ")
            horas_previstas = input("Digite a quantidade de horas previstas: ")
            valor_hora = input("Digite o valor da hora trabalhada: ")
            prazo = input("Digite o prazo estimado: ")

            print(projeto)
            print(horas_previstas)
            print(valor_hora)
            print(prazo)

            valor_total = int(horas_previstas) * int(valor_hora)

            gerar_pdf(projeto, horas_previstas, valor_hora, prazo, valor_total, contador)
            contador += 1
        elif opcao == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()