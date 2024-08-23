# Gerador de Orçamentos em PDF

Este projeto é um simples gerador de orçamentos em PDF usando a biblioteca `FPDF` em Python. O programa permite que o usuário insira informações de um projeto, como a descrição, horas previstas, valor da hora trabalhada e o prazo estimado, para gerar automaticamente um arquivo PDF com os detalhes do orçamento.

## Funcionalidades

- Geração de PDF a partir das informações fornecidas pelo usuário.
- Inserção de imagem de template no PDF para personalização.
- Cálculo automático do valor total do projeto com base nas horas previstas e valor da hora.
- Nomeação automática dos arquivos PDF gerados para facilitar o armazenamento.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Instale a biblioteca `FPDF` caso ainda não a tenha instalada:

    ```bash
    pip install fpdf
    ```

3. Execute o script `main.py`:
   
    ```bash
    python main.py
    ```

4. No menu, escolha a opção "1- Gerar PDF" para criar um novo orçamento.
5. Preencha as informações solicitadas, como descrição do projeto, horas previstas, valor da hora e prazo estimado.
6. O PDF será gerado e salvo automaticamente com o nome no formato `Orçamento_<contador>.pdf`.

7. Para sair do programa, escolha a opção "2- Sair".

## Exemplo de Uso

Abaixo está um exemplo de entrada de dados e o resultado esperado:

- **Descrição do Projeto:** Desenvolvimento de Website
- **Horas Previstas:** 40
- **Valor da Hora:** 50
- **Prazo Estimado:** 2 semanas

**Resultado:** Um arquivo PDF é gerado contendo todas as informações fornecidas, com o nome `Orçamento_1.pdf`.

## Requisitos

- Python 3.x
- Biblioteca [FPDF](http://www.fpdf.org/)

## Autor

Kaio Vitor - [GitHub](https://github.com/Kaio-0708)
