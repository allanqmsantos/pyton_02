import os
import logging
from datetime import datetime
import fitz  # PyMuPDF

def ler_arquivo(caminho_arquivo):
    """
    Lê o conteúdo de um arquivo de texto.

    :param caminho_arquivo: Caminho do arquivo.
    :return: Conteúdo do arquivo.
    """
    with open(caminho_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def escrever_arquivo(caminho_arquivo, conteudo):
    """
    Escreve uma string em um arquivo de texto.

    :param caminho_arquivo: Caminho do arquivo.
    :param conteudo: Conteúdo a ser escrito no arquivo.
    """
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

def main():
    # Configurar o logger
    logging.basicConfig(filename=r'\\192.168.254.5\enfermagem\logs\log.txt', level=logging.INFO)

    # Obter informações do usuário
    nome = input("Digite o nome do paciente: ").strip()
    unidade_internacao = input("Digite a unidade de internação: ").strip()

    # Nome do arquivo
    nome_arquivo = f"{nome}_{unidade_internacao}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

    # Caminho do arquivo modelo
    caminho_modelo = fr"\\192.168.254.5\enfermagem"

    # Caminho para salvar os novos arquivos
    caminho_atual = fr"\\192.168.254.5\enfermagem\atuais"

    # Lista de arquivos para escolher
    arquivos = [
        "ANOTACAO_DO_TECNICO_MANUAL.docx",
        "EVOLUCAO_TEC_ENFERMAGEM_ENFERMARIA.doc",
        "HBV_SAE.docx",
        "EVOLUCAO_DE_ENFERMEIRO_UTI.pdf"
    ]

    # Menu de escolha
    while True:
        print("Escolha o arquivo a ser aberto:")
        for i, arquivo in enumerate(arquivos, 1):
            print(f"{i}. {arquivo}")
        print("0. Sair")

        opcao = input("Digite o número correspondente ao arquivo desejado: ")

        if opcao == "0":
            print("Saindo do programa...")
            break

        try:
            opcao = int(opcao)
            if opcao < 1 or opcao > len(arquivos):
                raise ValueError
        except ValueError:
            print("Opção inválida. Digite um número correspondente à opção desejada.")
            continue

        # Nome do arquivo escolhido
        arquivo_escolhido = arquivos[opcao - 1]

        # Caminho completo do arquivo escolhido
        caminho_arquivo_escolhido = fr"{caminho_modelo}\{arquivo_escolhido}"

        # Copiar o arquivo modelo para a pasta de arquivos atuais
        os.system(fr"copy {caminho_arquivo_escolhido} {caminho_atual}\{nome_arquivo}.pdf")

        # Renomear o arquivo na pasta de arquivos atuais
        novo_caminho = fr"{caminho_atual}\{nome_arquivo}.pdf"
        os.rename(fr"{caminho_atual}\{arquivo_escolhido}", novo_caminho)

        # Abrir o arquivo
        abrir_arquivo(novo_caminho)

if __name__ == "__main__":
    main()
