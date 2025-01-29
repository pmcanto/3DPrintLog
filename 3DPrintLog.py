import os
from collections import defaultdict

def listar_arquivos(diretorio):
    estrutura = {}

    for raiz, pastas, arquivos in os.walk(diretorio):
        rel_path = os.path.relpath(raiz, diretorio)
        if rel_path == ".":
            rel_path = ""  
        estrutura[rel_path] = []

        for arquivo in arquivos:
            if arquivo.endswith(('.txt', '.py', '.exe')):  # Adicione aqui os arquivos que você quer ignorar
                continue
            estrutura[rel_path].append(arquivo)

    return estrutura

def exibir_estrutura(estrutura, arquivo_saida):
    total_arquivos = 0
    total_impressao = 0

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        for pasta, arquivos in sorted(estrutura.items(), key=lambda x: x[0]):
            # Define the nivel variable here
            nivel = pasta.count(os.sep) if pasta else 0

            if pasta:  # Evita imprimir linha vazia para o diretório raiz
                f.write(f"{'\t' * nivel}{os.path.basename(pasta)}\n")

            contador_arquivos = defaultdict(int)

            for arquivo in arquivos:
                partes = arquivo.split("x ", 1)
                if len(partes) > 1 and partes[0].isdigit():
                    quantidade = int(partes[0])
                    nome_arquivo = partes[1]
                else:
                    quantidade = 1
                    nome_arquivo = arquivo

                contador_arquivos[nome_arquivo] += quantidade
                total_impressao += quantidade

            for arquivo, qtd in contador_arquivos.items():
                f.write(f"{'\t' * (nivel + 1)}{qtd}x {arquivo}\n")
                total_arquivos += 1

        f.write("\n\n\nResumo:\n")
        f.write(f"Total de tipos de arquivos: {total_arquivos}\n")
        f.write(f"Total de arquivos a serem impressos: {total_impressao}\n")

def main():
    try:
        while True:
            print("Menu:")
            print("1. Iniciar processo")
            print("2. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                diretorio_atual = os.getcwd()
                estrutura = listar_arquivos(diretorio_atual)
                arquivo_saida = "impressao_3d.txt"
                exibir_estrutura(estrutura, arquivo_saida)
                print(f"Estrutura salva em {arquivo_saida}")
                input("Pressione qualquer tecla para sair...")
                break
            elif escolha == "2":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione qualquer tecla para sair...")

if __name__ == "__main__":
    main()