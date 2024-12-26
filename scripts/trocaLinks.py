import re

# Caminho do arquivo a ser modificado
caminho_arquivo = "100cmd.md"

# Links a serem substituídos
link_antigo = "https://github.com/bobbyiliev/101-linux-commands-ebook/blob/main/"
link_novo = "https://github.com/AnaMarcacini/Linux-lessons/blob/main/outros/101-linux-commands-ebook/"

# Função para substituir os links
def substituir_links(caminho_arquivo, link_antigo, link_novo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        
        # Substituição dos links
        conteudo_modificado = conteudo.replace(link_antigo, link_novo)
        
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo_modificado)
        
        print(f"Links substituídos com sucesso no arquivo: {caminho_arquivo}")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Executar a função
substituir_links(caminho_arquivo, link_antigo, link_novo)
