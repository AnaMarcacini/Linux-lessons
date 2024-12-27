import re

def formatar_link(titulo):
    # Formatar o título para criar a âncora correspondente
    return titulo.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(':', '').replace('.', '')#.replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

def gerar_indice(linhas):
    # Padrão regex para detectar títulos no markdown
    padrao_titulo = re.compile(r'^(#+)\s+(.+)')
    # Lista para armazenar o índice
    indice = []
    dentro_bloco_codigo = False
    for linha in linhas:
        linha = linha.strip() #remover espaços em branco do início e do fim 
        # Detecta início e fim de blocos de código
        if linha.startswith("```"):
            dentro_bloco_codigo = not dentro_bloco_codigo
        if dentro_bloco_codigo:
            continue # ignorar
        
        # Procurar por títulos (sem código)
        match = padrao_titulo.match(linha)
        if match:
            nivel = len(match.group(1))  # Quantidade de '#' define o nível
            titulo = match.group(2).strip().replace(':', '')  # O título em si
            link = formatar_link(titulo)
            indice.append((nivel, titulo, link))
    exibir_indice(indice)
    return indice      
            
def atualizar_indice(arquivo_md):
    with open(arquivo_md, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    # Encontra o índice da linha onde começa # Básicos
    indice_basicos = None
    for i, linha in enumerate(linhas):
        if linha.strip() == "</td>":
            indice_basicos = i
            print(indice_basicos)
            break
    # Se o título não for encontrado, não faça nada
    if indice_basicos is None:
        print("Título '# Básicos' não encontrado.")
        return
    
    SemIndice = linhas[indice_basicos:]
    # print(SemIndice)
    indice_gerado = gerar_indice(SemIndice)
    # exibir_indice(indice_gerado)
    escrever_indice(arquivo_md,indice_gerado,SemIndice)

        
def escrever_indice(arquivo_md,indice,conteudo):
    # Escreve o novo conteúdo de volta no arquivo
    with open(arquivo_md, 'w', encoding='utf-8') as file:
        file.write('# <img src="src/pinguim/linux2.gif" width="50"/> Linux-lessons <img src="src/pinguim/linux2.gif" width="50"/>\n')
        file.write('\n')
        file.write('## Index 🐧\n')
        file.write('\n')
        file.write('<table style="border-collapse: collapse; border: none;">\n')
        file.write('  <tr>\n')
        file.write('    <td style="vertical-align: top; text-align: left; border: none;">\n')
        file.write('<!-- INDICE -->\n')

        for nivel, titulo, link in indice:
            indentacao = "&nbsp;&nbsp;&nbsp;&nbsp;" * (nivel - 1)
            file.write(f'{indentacao} - <a href="#{link}">{titulo}</a><br>')  # Adiciona cada título formatado
            file.write("\n")
        file.writelines(conteudo)

def exibir_indice(indice):
    for nivel, titulo, link in indice:
        indentacao = '  ' * (nivel - 1)
        print(f"{indentacao}- [{titulo}](#{link})")

if __name__ == "__main__":
    caminho_arquivo_md = "README.md"  
    atualizar_indice(caminho_arquivo_md)