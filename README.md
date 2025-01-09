# <img src="src/pinguim/linux2.gif" width="50"/> Linux-lessons <img src="src/pinguim/linux2.gif" width="50"/>

## Index 🐧

<table style="border-collapse: collapse; border: none;">
  <tr>
    <td style="vertical-align: top; text-align: left; border: none;">
<!-- INDICE -->
 - <a href="#básicos">Básicos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#sistema-de-arquivos">Sistema de Arquivos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#comandos-basicos">Comandos Basicos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#listar-arquivos">Listar Arquivos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#permissões">Permissões</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#visualizando-permissões">Visualizando Permissões</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#alterando-permissões">Alterando Permissões</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#adicionar-diretório-no-`path`">Adicionar Diretório no `PATH`</a><br>
 - <a href="#partições">Partições</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#ver-partições">Ver Partições</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#1-usando-o-comando-lsblk">1. Usando o comando lsblk</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#2-usando-o-comando-fdisk">2. Usando o comando fdisk</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#3-usando-o-comando-df">3. Usando o comando df</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#4-usando-o-parted">4. Usando o parted</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#5-com-gui-se-você-prefere-interface-gráfica">5. Com GUI (Se você prefere interface gráfica)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#gparted">GParted</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#discos-gnome-disks">Discos (gnome-disks)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#montar-partição">Montar Partição</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#montar-a-partição-caso-não-esteja-montada">Montar a Partição (Caso Não Esteja Montada)</a><br>
 - <a href="#criar-programas-personalizados">Criar programas Personalizados</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#cuidado-com-o-interpretador">Cuidado com o interpretador</a><br>
 - <a href="#verificar-origem-do-programa">Verificar origem do programa</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#ir-para-esse-repo">ir para esse repo</a><br>
 - <a href="#redirecionamento-e-pipes">Redirecionamento e pipes</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#redirecionando-a-saída-para-um-arquivo">Redirecionando a saída para um arquivo</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#redirecionando-de-entrada">Redirecionando de Entrada</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#redirecionamento-de-erros-2>-e-2>>">Redirecionamento de Erros (2> e 2>>)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#redirecionamento-de-saída-e-erros-&>-ou-2>&1">Redirecionamento de Saída e Erros (&> ou 2>&1)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#entrada-e-saída-padrão">Entrada e Saída Padrão</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#pipes-`|`">Pipes (`|`)</a><br>
 - <a href="#variáveis">Variáveis</a><br>
 - <a href="#operadores-bash">Operadores Bash</a><br>
 - <a href="#operadores-de-comparação">Operadores de Comparação</a><br>
 - <a href="#operadores-de-strings">Operadores de Strings</a><br>
 - <a href="#scripts-bash">Scripts Bash</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#operações-matemáticas">Operações Matemáticas</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#operadores-lógicos">Operadores Lógicos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#comparadores-numéricos">Comparadores Numéricos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#operadores-de-comparação-de-strings">Operadores de Comparação de Strings</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#comparadores-de-arquivos">Comparadores de Arquivos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#variaveis">Variaveis</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#variaveis-locais-e-globais-escopo">Variaveis Locais e Globais (Escopo)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#operações">Operações</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#if-else">If-else</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#com-operador-lógico">Com operador lógico</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#loops">LOOPs</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#loop-usando-o-for">Loop usando o For</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#loop-usando-o-while">Loop usando o While</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#loop-usando-o-until">Loop usando o until</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#switch-case">Switch Case</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#funções">Funções</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#função-com-parametros">Função com Parametros</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#função-com-retorno">Função com Retorno</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#exemplo-de-utilização">Exemplo de utilização</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#parâmetros-e-argumentos-do-script">Parâmetros e Argumentos do Script</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#processando-argumentos-com-getopts">Processando Argumentos com getopts</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#função-sem-argumentos-getopts">Função sem argumentos getopts</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#exemplo">Exemplo</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#input">Input</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#redirecionamento-e-pipe">Redirecionamento e Pipe</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#entrada-e-saída-padrão">Entrada e Saída Padrão</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#captura-de-erros">Captura de erros</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#tratamento-de-erros">Tratamento de Erros</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#interromper-o-script-em-caso-de-erros">Interromper o Script em Caso de Erros</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#verificar-status-de-saída-do-comando">Verificar Status de Saída do Comando</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#função-de-tratamento-de-erro">Função de Tratamento de Erro</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#regex">REGEX</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#depuração-de-scripts">Depuração de Scripts</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#manipulando-arquivos">Manipulando Arquivos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#ler-arquivos">Ler Arquivos</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#lendo-um-arquivo-linha-por-linha">Lendo um arquivo linha por linha</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#ler-primeiras-e-ultimas-linhas">Ler primeiras e ultimas linhas</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="#scripts-modulares---chamando-outros-scripts">Scripts Modulares - Chamando outros Scripts</a><br>
   </td>
    <td style="vertical-align: top; border: none;">
      <img src="src/pinguim/Linux1.gif" alt="Pinguim animado" width="200"/>
    </td>
  </tr>
</table>

# Básicos
## Sistema de Arquivos 
File Hierarchy Standard (FHS)

| Path     | Content                             |
| -------- | ----------------------------------- |
| `/bin`   | Binaries (User)                     |
| `/boot`  | Static boot loader files            |
| `/etc`   | Host specific configs               |
| `/lib`   | Shared libraries and kernel modules |
| `/sbin`  | Binaries (System/root)              |
| `/var`   | Varying files (e.g. Logs)           |
| `/usr`   | 3rd party software                  |
| `/proc`  | Pseudo file system                  |
| `/sys`   | Pseudo file system                  |
| `/mnt`   | Mountpoint for internal drives      |
| `/media` | Mountpoint for external drives      |
| `/home`  | User homes                          |
| `/run`   | PID files of running processes      |

---
## Comandos Basicos
Aqui estão alguns comandos básicos que você vai usar frequentemente:

ls: Lista arquivos e diretórios no diretório atual.
    Exemplo: ls ou ls -l (para listar detalhes).
cd: navega entre diretorios.
    Exemplo: cd /home/usuario ou cd .. (para voltar um diretório).
pwd: Mostra o diretório atual 
touch: Cria um novo arquivo vazio.
    Exemplo: touch novo_arquivo.txt.
mkdir: Cria um novo diretório.
    Exemplo: mkdir novo_diretorio.
rm [nome]: Remove arquivos ou diretórios.
    rm -r: Remove diretórios recursivamente.
    Exemplo: rm arquivo.txt ou rm -r diretorio (para remover diretórios).
cp: Copia arquivos ou diretórios.
    Exemplo: cp arquivo.txt copia.txt.
mv: Move ou renomeia arquivos e diretórios.
    Exemplo: mv arquivo.txt novo_diretorio/ ou mv arquivo.txt novo_nome.txt.
touch [nome]: Cria um novo arquivo vazio.
    Exemplo: touch arquivo.txt
## Listar Arquivos
ls -l /usr/local/bin/token


## Permissões
### Visualizando Permissões
`ls -l` : Isso mostrará a lista de arquivos do diretorio e suas permissões

    -rw-r--r-- 1 usuario grupo  1234 Dec 27 10:00 arquivo.txt

O primeiro conjunto (-rw-r--r--) indica permissões:

    r: Leitura (read).
    w: Escrita (write).
    x: Execução (execução).
### Alterando Permissões

```bash
chmod +x script.sh   # Torna o arquivo executável executável por todos os usuários
chmod 644 arquivo.txt  # Define permissões numéricas
```

Se você quiser que apenas você possa executá-lo, ajuste as permissões para o seu usuário:

```bash
sudo chown $(whoami):$(whoami) <arquivo>
sudo chmod 755 <arquivo>
```

Ou, se você só precisa que o arquivo seja executável pelo seu usuário:

```bash
sudo chmod u+x /usr/local/bin/token
```
## Adicionar Diretório no `PATH` 

Exemplo adicionando esse diretório `(/home/ahmarcacini/.local/bin)` no `PATH`

```bash
nano ~/.bashrc
```

Coloque no final do arquivo

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Salve e feche o editor

Recarregue o arquivo .bashrc para apliacar as mudanças usando `source ~/.bashrc` ou feche e abra um novo terminal

Verificando 

```bash
ahmarcacini@kurumina-desktop:~/Git/AnaMarcacini/Linux-lessons$ echo $PATH
/home/ahmarcacini/.local/bin:/home/ahmarcacini/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

# Partições 
## Ver Partições 
### 1. Usando o comando lsblk
Mostra informações sobre os discos e partições de forma hierárquica:
```bash
lsblk
```
Se quiser ver com detalhes adicionais, como os pontos de montagem e tamanhos:

```bash
lsblk -f

```
### 2. Usando o comando fdisk
Para listar as partições de um disco específico (substitua /dev/sdX pelo seu disco):

```bash
sudo fdisk -l
```
Exemplo: 
```bash
sudo fdisk -l /dev/sda
```
### 3. Usando o comando df
Se você deseja visualizar apenas partições montadas:

```bash
df -h
```
### 4. Usando o parted
Para uma visão mais detalhada e interativa das partições:

```bash
sudo parted /dev/sdX
```
No terminal interativo, você pode usar o comando print para listar as partições.

### 5. Com GUI (Se você prefere interface gráfica)
Se você está em um ambiente gráfico, pode usar ferramentas como:

#### GParted:
Instale com:

```bash
sudo apt install gparted
```
E execute:
```bash
sudo gparted
```
#### Discos (gnome-disks):
Em distribuições baseadas no GNOME, pode abrir diretamente o aplicativo "Discos".

## Montar Partição

### Montar a Partição (Caso Não Esteja Montada)
Se por algum motivo a partição não estiver montada, você precisará montá-la manualmente. Para isso:

Verifique o ponto de montagem desejado ou crie um diretório para isso:

```bash
sudo mkdir -p /mnt/Dados
```
(-p -> cria os diretorios e subdiretorios se necessário)
Monte a partição:

```bash
sudo mount /dev/nvme0n1p9 /mnt/Dados
```
Verifique se foi montada corretamente:

```bash
df -h
```

----> OBS : Permissões
Se você tiver problemas de permissão ao acessar os arquivos, pode ajustar com:

```bash
sudo chmod -R 777 /mnt/Dados
```
Ou tornar-se o usuário root temporariamente:

```bash
sudo su
cd /mnt/Dados
```



# Criar programas Personalizados
Local do executavel : /usr/local/bin
exemplo : /usr/local/bin/traduz


Suponha que você tenha um arquivo chamado meu_programa.c. Você pode compilar este arquivo usando gcc (GNU Compiler Collection):

```sh
gcc meu_programa.c -o meu_programa
```

Mover o executável para /usr/local/bin (requer permissão de superusuário):

```sh
sudo mv meu_programa /usr/local/bin/
```

Mover o executável para ~/bin (não requer permissão de superusuário):

```sh
mv meu_programa ~/bin/
```


Nota: Para garantir que ~/bin esteja no seu PATH, você pode adicionar a seguinte linha ao seu arquivo .bashrc ou .profile:

```sh
export PATH=$HOME/bin:$PATH
```
E depois recarregar o arquivo:

```sh
source ~/.bashrc  # ou source ~/.profile
```
Após esses passos, você deve ser capaz de executar o seu programa de qualquer lugar no terminal digitando meu_programa.
## Cuidado com o interpretador
Certifique-se de que o script x tenha o shebang correto na primeira linha para garantir que ele seja executado pelo interpretador correto. Por exemplo, para um script Bash, a primeira linha deve ser: _#!/bin/bash_ ou _#!/usr/bin/env bash_
# Verificar origem do programa 
Para descobrir exatamente onde o script está localizado, você pode usar o comando which:

```sh
which <codigo>
```
Exemplo :

```sh
which python
which <comando criado >
which nmp
which cd
```
## ir para esse repo 
```bash
cd $(dirname $(which token))
```
Explicação do comando:

- which token: Isso retorna o caminho completo do seu script token.
- dirname $(which token): Isso extrai o diretório do caminho completo retornado pelo which token.
- cd $(dirname $(which token)): Isso muda o diretório para o diretório onde o script token está localizado.


# Redirecionamento e pipes
Bash permite redirecionar a saída de comandos para arquivos ou até mesmo usá-los em conjunto com outros comandos através de pipes (|).

## Redirecionando a saída para um arquivo

  * `>` : Redireciona a saída para um arquivo (sobrescreve).
  * `>>` : Redireciona a saída para um arquivo (anexa).

```bash
echo "texto" > arquivo.txt: Cria (ou substitui) um arquivo com o texto.
echo "texto" >> arquivo.txt: Adiciona ao final de um arquivo existente.
```

## Redirecionando de Entrada

Permite usar o conteúdo de um arquivo como entrada para um comando.
```bash
while read linha; do
    echo "Linha do arquivo: $linha"
done < arquivo.txt
```

## Redirecionamento de Erros (2> e 2>>)

Captura mensagens de erro geradas por comandos.

Exemplo:

```sh
ls /caminho/invalido 2> erros.log
```

      erros.log:
        ls: cannot access '/caminho/invalido': No such file or directory

## Redirecionamento de Saída e Erros (&> ou 2>&1)

Redireciona saída padrão e erros para o mesmo destino.

Exemplo:

```sh
comando &> tudo.log
```

## Entrada e Saída Padrão

    Descritores de Arquivo
      0: Entrada padrão (stdin)
      1: Saída padrão (stdout)
      2: Erro padrão (stderr)

Exemplo de Uso Explícito:

```bash
comando 1> saida.txt 2> erros.txt
```
      Conteúdo de saida.txt (se houver saída normal):
          Saída do comando aqui
      Conteúdo de erros.txt (se houver erros):
          Erro do comando aqui


## Pipes (`|`):

Encaminha a saída de um comando como entrada para outro

`ls | grep "documento"`: Lista arquivos e filtra com grep para mostrar apenas os que contêm "documento".

# Variáveis
Você pode criar variáveis para armazenar dados.

Definindo uma variável: `nome="João"`

Usando a variável: `echo $nome` # Exibe o conteúdo da variável.

```bash
variavel="valor"
echo $variavel  # Exibe o valor da variável
```
    Regras para Nomes de Variáveis:
      * Devem começar com uma letra ou sublinhado (_).
      * Podem conter letras, números e sublinhados, mas não espaços.
      * São sensíveis a maiúsculas e minúsculas.

```bash
## Exemplos
nome="Maria"
id=123
_usuario="admin"
echo "Usuário: $nome, ID: $id"
```
# Operadores Bash
O Bash suporta operações matemáticas usando o comando expr ou $(( )):
```bash
x=10
y=5

# Soma
echo $((x + y))

# Subtração
echo $((x - y))

# Multiplicação
echo $((x * y))

# Divisão
echo $((x / y))

# Módulo
echo $((x % y))
```

# Operadores de Comparação

Comparações numéricas são realizadas usando os seguintes operadores:

-`eq`: Igual a.

-`ne`: Diferente de.

-`lt`: Menor que.

-`le`: Menor ou igual a.

-`gt`: Maior que.

-`ge`: Maior ou igual a.

```bash
if [ $x -gt $y ]; then
  echo "$x é maior que $y"
fi
```
# Operadores de Strings

Para strings, os operadores são:

-`=`: Igual a.

-`!`=: Diferente de.

-`z`: Verdadeiro se a string estiver vazia.

-`n`: Verdadeiro se a string não estiver vazia.

```bash
str="Hello"
if [ -n "$str" ]; then
  echo "A string não está vazia."
fi
```

![alt text](src/Shell/shell-scripting-linux.png)

# Scripts Bash 

<table style="border-collapse: collapse; border: none;">
  <tr>
    <td style="vertical-align: top; text-align: justify; border: none;">
    1. O que é Bash?
    Bash (Bourne Again Shell) é um interpretador de comandos usado em sistemas Unix, como Linux e macOS. Ele permite que você interaja com o sistema operacional executando comandos e criando scripts para automatizar tarefas. É importante deixar o arquivo .sh executável.
    Principais Características do Bash:
        É amplamente utilizado em distribuições Linux.Suporta programção de scripts para automação de tarefas repetitivas.
        Permite gerenciar arquivos, processos e configurar o sistema.
    No Linux, cada arquivo tem permissões de leitura, gravação e execução, que podem ser ajustadas com o comando chmod.<br>
      chmod +x script.sh: Torna o arquivo executável.<br>
      chmod 755 arquivo.txt: Define permissões para o dono do arquivo, grupo e outros.
      <br>
      Todo script começa com a linha "#!/bin/bash", que indica o interpretador do script. Isso é chamado de "shebang".
    </td>
    <td style="vertical-align: top; border: none;">
      <img src="src/Shell/bash.webp" alt="Pinguim animado" width="2000"/>
    </td>
  </tr>
</table>

bash --version
Se você estiver no Windows, pode usar o Windows Subsystem for Linux (WSL) ou instalar um emulador de terminal como o Git Bash.

```bash
#!/bin/bash
echo "Olá, Mundo!" # retorna olá mundo
```

Tornando o Script Executável

```bash
chmod +x meu_script.sh
```

Executando o Script

Para rodar o script, basta usar:

```bash
./meu_script.sh
```

## Operações Matemáticas

| Operador | Descrição                      | Exemplo                  | Resultado |
|----------|--------------------------------|--------------------------|-----------|
| `+`      | Adição                         | `echo $((3 + 5))`        | `8`       |
| `-`      | Subtração                      | `echo $((10 - 7))`       | `3`       |
| `*`      | Multiplicação                  | `echo $((4 * 6))`        | `24`      |
| `/`      | Divisão                        | `echo $((12 / 4))`       | `3`       |
| `%`      | Módulo (resto da divisão)      | `echo $((10 % 3))`       | `1`       |
| `**`     | Potência                       | `echo $((2 ** 3))`       | `8`       |
| `+=`     | Incremento com soma            | `x=5; x+=3; echo $x`     | `8`       |
| `-=`     | Decremento com subtração       | `x=5; x-=2; echo $x`     | `3`       |
| `*=`     | Incremento com multiplicação   | `x=5; x*=2; echo $x`     | `10`      |
| `/=`     | Decremento com divisão         | `x=10; x/=2; echo $x`    | `5`       |
|`++`|Incremento| Aumenta o valor de uma variável em 1	|`((a++))`| 
|`--`|Decremento| Diminui o valor de uma variável em 1	|`((a--))`| 
---

## Operadores Lógicos

| Operador | Descrição                         | Exemplo                            | Resultado |
|----------|-----------------------------------|------------------------------------|-----------|
| `&&` ou `-a`    | E lógico (true se ambas forem true) | `[ $a -lt 10 ] && [ $b -gt 5 ]`   | `true`    |
| `\|\|` ou ``-o  | OU lógico (true se uma for true)   | `[ $a -lt 10 ] \|\| [ $b -gt 5 ]` | `true`    |
| `!`      | NÃO lógico (inverte o valor lógico) | `[ ! $a -lt 10 ]`                 | `false`   |

---

## Comparadores Numéricos

| Operador | Descrição              | Exemplo             | Resultado    |
|----------|------------------------|---------------------|--------------|
| `-eq` ou `==`   | Igual a                | `[ $a -eq $b ]` ou `[ 5 == 5 ]`    | `true/false` |
| `-ne` ou `!=`   | Diferente de           | `[ $a -ne $b ]`   ou `[ 5 != 3 ]`  | `true/false` |
| `-lt`    | Menor que              | `[ $a -lt $b ]`     | `true/false` |
| `-le`    | Menor ou igual a       | `[ $a -le $b ]`     | `true/false` |
| `-gt`    | Maior que              | `[ $a -gt $b ]`     | `true/false` |
| `-ge`    | Maior ou igual a       | `[ $a -ge $b ]`     | `true/false` |

---
## Operadores de Comparação de Strings 
***Comparadores de Strings***

| Operador | Descrição              | Exemplo             | Resultado    |
|----------|------------------------|---------------------|--------------|
| `=`      | Strings são iguais     | `[ "$a" = "$b" ]`   | `true/false` |
| `!=`     | Strings são diferentes | `[ "$a" != "$b" ]`  | `true/false` |
| `-z`     | String é vazia         | `[ -z "$a" ]`       | `true/false` |
| `-n`     | String não é vazia     | `[ -n "$a" ]`       | `true/false` |

---


| Operador | Descrição                 | Exemplo                 | Resultado |
|----------|---------------------------|-------------------------|-----------|
| `==`     | Igual a                  | `[ "abc" == "abc" ]`    | `true`    |
| `!=`     | Diferente de             | `[ "abc" != "def" ]`    | `true`    |
| `<`      | Menor lexicograficamente | `[ "abc" < "def" ]`     | `true`    |
| `>`      | Maior lexicograficamente | `[ "def" > "abc" ]`     | `true`    |
| `-z`     | String vazia             | `[ -z "" ]`             | `true`    |
| `-n`     | String não vazia         | `[ -n "texto" ]`        | `true`    |

**Nota:** Use aspas ao comparar strings para evitar erros.

## Comparadores de Arquivos

| Operador | Descrição                      | Exemplo                 | Resultado    |
|----------|--------------------------------|-------------------------|--------------|
| `-e`     | Arquivo ou diretório existe                | `[ -e arquivo.txt ]`    | `true/false` |
| `-f`     | Arquivo existe e é um arquivo regular (comum)          | `[ -f arquivo.txt ]`    | `true/false` |
| `-d`     | Existe e é um diretório                | `[ -d diretorio/ ]`     | `true/false` |
| `-r`     | Possui permissão de leitura   | `[ -r arquivo.txt ]`    | `true/false` |
| `-w`     | Possui permissão de escrita   | `[ -w arquivo.txt ]`    | `true/false` |
| `-x`     | Possui permissão de execução  | `[ -x script.sh ]`      | `true/false` |
| `-s`     | Não está vazio                | `[ -s arquivo.txt ]`    | `true/false` |

Um arquivo regular é o tipo de arquivo mais comum em sistemas Unix/Linux. Ele contém dados, como texto, código-fonte, binários, ou qualquer outro tipo de conteúdo. Em contraste, existem outros tipos de arquivos no sistema, como diretórios, links simbólicos, dispositivos, entre outros.

Exemplos de Arquivo Regular
Um arquivo de texto, como documento.txt.
Um script ou programa, como script.sh.
Um arquivo executável, como programa.
```bash
#!/bin/bash

arquivo="documento.txt"

if [ -f "$arquivo" ]; then
  echo "$arquivo é um arquivo regular."
else
  echo "$arquivo não é um arquivo regular ou não existe."
fi
```


O que ***NÃO*** é um arquivo regular
Diretórios: Pastas do sistema, como /home/usuario. Para verificar diretórios, usamos -d.
```bash
if [ -d "meu_diretorio" ]; then echo "É um diretório."; fi
```

Links Simbólicos: Referências para outro arquivo ou diretório. Para verificar links simbólicos, usamos -L.
```bash
if [ -L "link_para_arquivo" ]; then echo "É um link simbólico."; fi
```
Dispositivos: Arquivos especiais usados para interagir com hardware, como /dev/sda (um disco rígido).
Sockets e Pipes: Usados para comunicação entre processos.



## Variaveis

```bash
#!/bin/bash
nome="João"
echo "Olá, $nome!"
## If-Else:
```

Cuidado: não pode ter espaço (nome = ) tem que ser sem espaço (nome=)
### Variaveis Locais e Globais (Escopo)

No Bash, as variáveis são globais por padrão, ou seja, podem ser acessadas fora da função. Para criar variáveis locais, use a palavra-chave `local`.
```bash
minha_funcao() {
    local variavel_local="local"
    variavel_global="global"
    echo "Dentro da função: $variavel_local"
}

minha_funcao

# Tentativa de acessar as variáveis fora da função
echo "Fora da função: $variavel_global"
echo "Fora da função: $variavel_local"  # Não estará disponível
```
Saída:

    Dentro da função: local
    Fora da função: global
    Fora da função:
## Operações

```bash

#!/bin/bash
a=10
b=5
soma=$((a + b))
echo "A soma de $a e $b é $soma"
```

## If-else

*Estrutura:*

```bash

if [ condicao ]; then
    # Comandos executados se a condição for verdadeira
elif [ outra_condicao ]; then
    # Comandos executados se outra_condicao for verdadeira
else
    # Comandos executados se nenhuma condição for verdadeira
fi
```

*Estrutura Simplificada (operador ternário)*

```bash
[ $num -gt 5 ] && echo "Maior" || echo "Menor ou igual"
```

```bash
if [ $nome == "João" ]; then
  echo "Olá João!"
else
  echo "Olá, estranho!"
fi

###################################
#!/bin/bash
idade=20

if [ $idade -ge 18 ]; then
  echo "Você é maior de idade."
else
  echo "Você é menor de idade."
fi
###################################
num=10

if [ $num -gt 5 ]; then
    echo "$num é maior que 5."
elif [ $num -eq 5 ]; then
    echo "$num é igual a 5."
else
    echo "$num é menor que 5."
fi

```

### Com operador lógico

```bash
#!/bin/bash
nome="João"
idade=22

if [ $nome == "João" ] && [ $idade -ge 18 ]; then
  echo "Você é o João e é maior de idade!"
fi

```

## LOOPs
### Loop usando o For:

```bash
for item in lista; do
    # Comandos executados para cada item
done

for i in 1 2 3 4 5; do
    echo "Iteração: $i"
done

for i in {1..5}; do
  echo "Número $i"
done
```
### Loop usando o While:

```bash
while [ condicao ]; do
    # Comandos executados enquanto a condição for verdadeira
done
```

```bash
count=1
while [ $count -le 5 ]; do
    echo "Contagem: $count"
    count=$((count + 1))
done
###############################
i=1
while [ $i -le 5 ]; do
  echo "Número $i"
  ((i++))
done
```

### Loop usando o until
O loop until executa comandos até que uma condição se torne verdadeira.

Sintaxe:
```bash
until [ condicao ]; do
    # Comandos executados até que a condição seja verdadeira
done
```
Exemplo:
```bash
count=1
until [ $count -gt 5 ]; do
    echo "Contagem: $count"
    count=$((count + 1))
done
```
## Switch Case

A instrução case é usada para comparar uma variável com vários valores e executar comandos correspondentes.

Sintaxe:
```bash
case variavel in
    valor1)
        # Comandos para valor1
        ;;
    valor2)
        # Comandos para valor2
        ;;
    *)
        # Comandos para qualquer outro valor
        ;;
esac
```

Exemplo:
```bash
read -p "Digite um dia da semana: " dia

case $dia in
    "segunda")
        echo "Início da semana!"
        ;;
    "sexta")
        echo "Fim de semana chegando!"
        ;;
    *)
        echo "Dia normal."
        ;;
esac
```


## Funções
```bash
###############################
saudacao() {
    echo "Olá, seja bem-vindo ao script Bash!"
}

# Chamada da função
saudacao
```

```bash
verificar_paridade() {
    if (( $1 % 2 == 0 )); then
        echo "$1 é par."
    else
        echo "$1 é ímpar."
    fi
}

verificar_paridade 4
verificar_paridade 7


```

### Função com Parametros

```bash
funcao_ola() {
  echo "Olá, $1!"
}
funcao_ola "Maria"

###############################
#!/bin/bash
saudacao() {
  echo "Olá, $1!"
}

saudacao "Maria"
saudacao "João"
```

O $1 representa o primeiro argumento passado para a função. Você pode passar múltiplos parâmetros para funções, como $2, $3, etc.
```bash

saudar_usuario() {
    echo "Olá, $1!"
    echo "É um prazer conhecer você, $2."
}

# Chamando a função com argumentos
saudar_usuario "Maria" "Santos"
```

### Função com Retorno

Embora o Bash não suporte diretamente retornos como linguagens tradicionais, você pode usar comandos como `return` para retornar códigos de status ou `echo` para devolver valores.

```bash
soma() {
    return $(( $1 + $2 ))
}

soma 3 7
resultado=$?
echo "Resultado da soma: $resultado"
```

```bash
multiplicar() {
    echo $(( $1 * $2 ))
}

resultado=$(multiplicar 4 5)
echo "Resultado da multiplicação: $resultado"
```

```bash


soma() {
    local resultado=$(( $1 + $2 ))
    return $resultado
}

soma 3 5
echo "Código de retorno: $?"  # Mostra o valor retornado


```

### Exemplo de utilização

```bash
exibir_menu() {
    echo "1. Exibir data atual"
    echo "2. Listar arquivos no diretório atual"
    echo "3. Sair"
}

exibir_data() {
    echo "Data atual: $(date)"
}

listar_arquivos() {
    echo "Arquivos no diretório atual:"
    ls
}

while true; do
    exibir_menu
    read -p "Escolha uma opção: " opcao

    case $opcao in
        1)
            exibir_data
            ;;
        2)
            listar_arquivos
            ;;
        3)
            echo "Saindo..."
            break
            ;;
        *)
            echo "Opção inválida. Tente novamente."
            ;;
    esac
    echo
done
```
```bash

#!/bin/bash

# Função para exibir uma saudação personalizada
saudacao() {
    echo "Olá, $1! Como vai você?"
}

# Função para calcular a soma de dois números
soma() {
    local num1=$1
    local num2=$2
    echo "A soma de $num1 e $num2 é $((num1 + num2))."
}

# Chamada das funções
saudacao "João"
soma 5 7
```
    Olá, João! Como vai você?
    A soma de 5 e 7 é 12.
## Parâmetros e Argumentos do Script

Scripts Bash podem aceitar argumentos da linha de comando.

Exemplo:
```bash
#!/bin/bash

# Exibe o primeiro e o segundo argumentos
echo "Argumento 1: $1"
echo "Argumento 2: $2"

Executando o Script:

./meu_script.sh arg1 arg2
```

    Saída:

    Argumento 1: arg1
    Argumento 2: arg2

Usando shift para Processar Vários Argumentos

```bash
while [[ $# -gt 0 ]]; do
    echo "Argumento atual: $1"
    shift
done
```

### Processando Argumentos com getopts

argumentos.sh:
```bash
#!/bin/bash

# Função de ajuda
ajuda() {
    echo "Uso: $0 [-n nome] [-i idade]"
    exit 1
}

# Processa os argumentos
while getopts "n:i:" opt; do
    case $opt in
        n) nome=$OPTARG ;;
        i) idade=$OPTARG ;;
        *) ajuda ;;
    esac
done

# Verifica se os parâmetros foram fornecidos
if [[ -z "$nome" || -z "$idade" ]]; then
    ajuda
fi

echo "Olá, $nome. Você tem $idade anos."
```

./argumentos.sh -n Ana -i 30


    getopts processa argumentos da linha de comando.
    OPTARG contém o valor do argumento associado a uma opção.

***Explicação***

 `while getopts "n:i:" opt; do`
* `getopts`: É usado para analisar argumentos fornecidos ao script. Ele processa argumentos formatados como opções, por exemplo, -n Ana -i 30.
* `"n:i:"`: Define as opções aceitas pelo script, O : indica que essa opção precisa de um valor (ex.: -n Ana).

    * n: Aceita um argumento obrigatório. 
    * i: Também aceita um argumento obrigatório (ex.: -i 30).
    * Se uma opção não estiver listada ou o argumento obrigatorio for omitido, o bloco *) será acionado.
* `opt` : Variável onde será armazenada a opção atual sendo processada (ex.: n ou i).
*  `while ... do`: O while percorre todas as opções passadas ao script até que getopts esgote os argumentos fornecidos.

Bloco `case`:

`n) nome=$OPTARG ;;`


* `n`): Executa este bloco se opt for n, ou seja, se o argumento for -n.
* `nome=$OPTARG`: Armazena o valor fornecido para -n (o argumento associado, como Ana) na variável nome.
    * OPTARG é uma variável automática que contém o argumento da opção processada.


`*) ajuda ;;` :Opção Inválida ou Faltando Argumento. O caractere * é um curinga que captura qualquer opção não listada no getopts.Também captura casos onde um argumento obrigatório está ausente (ex.: -n sem valor). Ao ser acionado chama a função ajuda para exibir uma mensagem ao usuário (presumivelmente explicando o uso correto do script).

#### Função sem argumentos getopts 

```bash
while getopts "na:i:" opt; do
    case $opt in
        n) echo "Opção -n ativada sem argumentos";;
        a) idade=$OPTARG ;;
        *) ajuda ;;
    esac
done
```
./script.sh -na Ana

Neste caso, -n e -a podem ser usados juntos (se forem configurados para não exigir argumentos).

Detecção de Fim de Opções: Se houver argumentos adicionais que não são opções (por exemplo, -n Ana arquivo.txt), getopts para de processar ao encontrar o primeiro argumento que não começa com -.

#### Exemplo:

```bash

#!/bin/bash

# Função de ajuda
ajuda() {
    echo "Uso: $0 [opções]"
    echo
    echo "Opções:"
    echo "  -n NOME       Define o nome do usuário (opcional)"
    echo "  -i IDADE      Define a idade do usuário (opcional)"
    echo "  -h            Exibe esta mensagem de ajuda"
    echo
    echo "Exemplo:"
    echo "  $0 -n Ana -i 25"
    exit 0
}

# Variáveis padrão (valores opcionais)
nome="Usuário"
idade="Desconhecida"

# Processar argumentos
while getopts "n:i:h" opt; do
    case $opt in
        n) nome=$OPTARG ;;  # Nome fornecido
        i) idade=$OPTARG ;; # Idade fornecida
        h) ajuda ;;         # Exibe a ajuda e sai
        *) ajuda ;;         # Exibe ajuda para argumentos inválidos
    esac
done

# Mensagem final
echo "Olá, $nome! Sua idade é $idade."

```


1. Argumentos Não Obrigatórios: As variáveis nome e idade possuem valores padrão (Usuário e Desconhecida). Se o usuário não fornecer -n ou -i, o script usará esses valores.
2. Função ajuda: ajuda fornece uma descrição clara das opções disponíveis e exemplos de uso. É acionada com a opção -h ou por qualquer entrada inválida.
3. Comportamento dos Argumentos : -n e -i permitem substituir os valores padrão. O script continua executando mesmo que os argumentos opcionais não sejam fornecidos.

***Exemplos de execução:***

```bash
$ ./script.sh
Olá, Usuário! Sua idade é Desconhecida.
###################################################
$ ./script.sh -n Ana
Olá, Ana! Sua idade é Desconhecida.
###################################################
$ ./script.sh -n Ana -i 25
Olá, Ana! Sua idade é 25.

###################################################
$ ./script.sh -x
Uso: ./script.sh [opções]

Opções:
  -n NOME       Define o nome do usuário (opcional)
  -i IDADE      Define a idade do usuário (opcional)
  -h            Exibe esta mensagem de ajuda

Exemplo:
  ./script.sh -n Ana -i 25

###################################################
$ ./script.sh -h
Uso: ./script.sh [opções]

Opções:
  -n NOME       Define o nome do usuário (opcional)
  -i IDADE      Define a idade do usuário (opcional)
  -h            Exibe esta mensagem de ajuda

Exemplo:
  ./script.sh -n Ana -i 25

```


```bash

#!/bin/bash

# Função de ajuda
ajuda() {
    echo "Uso: $0 [-n NOME] [-i IDADE] [-h]"
    exit 0
}

# Variáveis padrão
nome=""
idade=""

# Processar argumentos
while getopts "n:i:h" opt; do
    case $opt in
        n) nome=$OPTARG ;;
        i) idade=$OPTARG ;;
        h) ajuda ;;
        *) ajuda ;;
    esac
done

# Verificar se argumentos foram fornecidos
if [[ -z "$nome" ]]; then
    nome="Visitante" # Nome padrão se não fornecido
fi

if [[ -z "$idade" ]]; then
    idade="Indefinida" # Idade padrão se não fornecida
fi

echo "Olá, $nome! Sua idade é $idade."
```

    $ ./script.sh
    Olá, Visitante! Sua idade é Indefinida.

## Input

```bash
#!/bin/bash
echo "Qual é o seu nome?"
read nome
echo "Olá, $nome!"
```

    Opções Comuns do read:
      -p: Exibe uma mensagem antes de capturar a entrada.
      -s: Oculta a entrada do usuário (ideal para   senhas).
      -n: Limita o número de caracteres que podem ser inseridos.

```bash
read -p "Qual é o seu nome? " nome
echo "Olá, $nome!"
#########################################
read -sp "Digite sua senha: " senha
echo "\nSenha armazenada com sucesso."
```

```bash

#!/bin/bash

# Este script exibe uma saudação personalizada para o usuário.

read -p "Qual é o seu nome? " nome

# Verifica se o usuário digitou algo
if [[ -z "$nome" ]]; then
    echo "Você não digitou um nome. Tente novamente."
    exit 1
fi

echo "Olá, $nome! Bem-vindo ao mundo do Bash scripting!"

```

Explicação:
    A verificação [[ -z "$nome" ]] garante que a variável nome não está vazia.
    exit 1 encerra o script com um código de erro se o usuário não fornecer um nome.

## Redirecionamento e Pipe
Você pode redirecionar a saída de um comando para um arquivo ou passar a saída de um comando para outro comando.

Redirecionando saída para um arquivo:

```bash
#!/bin/bash
echo "Isso será gravado em um arquivo" > arquivo.txt
```

Usando pipes (|): O comando grep pode ser combinado com outros comandos para filtrar a saída.

```bash
#!/bin/bash
ls | grep "documento"
```
Combinações de comandos também são possíveis:
```bash
cat arquivo.txt | sort | uniq
```

### Entrada e Saída Padrão

    Descritores de Arquivo
      0: Entrada padrão (stdin)
      1: Saída padrão (stdout)
      2: Erro padrão (stderr)

Exemplo de Uso Explícito:

```bash
comando 1> saida.txt 2> erros.txt
```
      Conteúdo de saida.txt (se houver saída normal):
          Saída do comando aqui
      Conteúdo de erros.txt (se houver erros):
          Erro do comando aqui
## Captura de erros

[VER AQUI](#redirecionamento-de-erros-2-e-2)

## Tratamento de Erros

### Interromper o Script em Caso de Erros

Adicione set -e no início do script para parar a execução ao encontrar um erro.

```bash
# Interrompe o script ao primeiro erro
set -e
cp arquivo_nao_existente.txt destino/
```
### Verificar Status de Saída do Comando

Use $? para capturar o status do último comando executado (0 indica sucesso).

```bash
cp arquivo.txt destino/
if [[ $? -ne 0 ]]; then
    echo "Erro ao copiar o arquivo."
    exit 1
fi
```

### Função de Tratamento de Erro

```bash

tratar_erro() {
    echo "Erro na linha $1."
    exit 1
}

trap 'tratar_erro $LINENO' ERR
```

```bash
#!/bin/bash

# Função de erro
erro() {
    echo "Erro na linha $1."
    exit 1
}

# Configuração de trap para capturar erros
trap 'erro $LINENO' ERR

# Simulação de erro
cp arquivo_inexistente.txt destino/

echo "Esta mensagem não será exibida se houver erro."

```

    Saída:
    Erro na linha 10.

Explicação:

    O comando trap associa o manipulador de erro erro ao evento ERR.

    `$LINENO` retorna o número da linha onde o erro ocorreu.

### REGEX

```bash
read -p "Digite um número: " numero
if [[ ! $numero =~ ^[0-9]+$ ]]; then
    echo "Por favor, insira um número válido."
    exit 1
fi

```

## Depuração de Scripts

**Modo Verbose e Debug**

      - `bash -v script.sh`: Exibe cada linha antes de executá-la.
      - `bash -x script.sh`: Mostra cada comando e sua saída durante a execução.

## Manipulando Arquivos

Você pode criar, ler, escrever e manipular arquivos dentro de um script.

Criando e escrevendo em um arquivo:

```bash
#!/bin/bash
echo "Este é um arquivo de texto" > arquivo.txt
```

```bash
cat > arquivo.txt << EOF
Linha 1
Linha 2
EOF
```

    Conteúdo de arquivo.txt:
      Linha 1
      Linha 2

### Ler Arquivos

```bash
cat arquivo.txt
```

### Lendo um arquivo linha por linha:

```bash
#!/bin/bash
while IFS= read -r linha; do
  echo $linha
done < arquivo.txt
##################################
while read linha; do
    echo "$linha"
done < arquivo.txt
```

### Ler primeiras e ultimas linhas

```bash
head -n 5 arquivo.txt  # Exibe as primeiras 5 linhas
tail -n 5 arquivo.txt  # Exibe as últimas 5 linhas
```



## Scripts Modulares - Chamando outros Scripts

Divida o script em módulos reutilizáveis.

Exemplo de Script Principal:
```bash
#!/bin/bash

source funcoes.sh

saudacao "Mundo"
soma 10 20
```

Arquivo `funcoes.sh`:

```bash

saudacao() {
    echo "Olá, $1!"
}

soma() {
    echo "$(( $1 + $2 ))"
}

```


source importa funções do arquivo funcoes.sh
Scripts modulares são fáceis de manter e reutilizar.



























