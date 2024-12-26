# <img src="src/pinguim/linux2.gif" width="50"/> Linux-lessons <img src="src/pinguim/linux2.gif" width="50"/>

## Index 🐧

<table style="border-collapse: collapse; border: none;">
  <tr>
    <td style="vertical-align: top; text-align: left; border: none;">
<!-- INDICE -->
 - <a href="link">Básicos</a><br>
 - <a href="link">Partições</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">Ver Partições</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">1. Usando o comando lsblk</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">2. Usando o comando fdisk</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">3. Usando o comando df</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">4. Usando o parted</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">5. Com GUI (Se você prefere interface gráfica)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">GParted</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">Discos (gnome-disks)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">Montar Partição</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - <a href="link">Montar a Partição (Caso Não Esteja Montada)</a><br>
   </td>
    <td style="vertical-align: top; border: none;">
      <img src="src/pinguim/Linux1.gif" alt="Pinguim animado" width="200"/>
    </td>
  </tr>
</table>

# Básicos
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



