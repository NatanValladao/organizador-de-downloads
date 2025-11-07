# Meu Organizador de Downloads em Python

Cansado da bagunça na pasta "Downloads"? Eu também estava.

Decidi criar este script como meu primeiro projeto de automação em Python para resolver esse problema de uma vez por todas. Ele organiza automaticamente qualquer pasta, movendo os arquivos para subpastas com base em suas extensões.

## O que ele faz?

O script monitora uma pasta de origem (por padrão, a Downloads) e faz o seguinte:

Verifica cada item na pasta.

Ignora subpastas, processando apenas arquivos.

Identifica a extensão do arquivo (ex: .pdf, .jpg, .exe).

Consulta um "mapa" de regras (um dicionário Python).

Move o arquivo para uma pasta de destino correspondente (ex: "Documentos", "Imagens", "Programas").

Cria a pasta de destino (ex: "Imagens") se ela ainda não existir.

Ignora arquivos cuja extensão não esteja no mapa.

### Pastas e Extensões Suportadas

Atualmente, o script organiza:

Documentos: .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt, .csv

Programas: .exe

Imagens: .png, .jpg, .jpeg

Arquivos Compactados: .rar, .zip

Musicas: .mp3

Videos: .mp4

## Como Usar

### Pré-requisitos

Python 3 instalado no seu sistema.

### Execução

Clone ou baixe este repositório

Execute o script:
O script foi feito para rodar sem a necessidade de bibliotecas externas (além das que já vêm com o Python, como os e shutil).

python organizador.py


O script irá rodar uma vez e organizar todos os arquivos da pasta Downloads do usuário atual.

## Como Customizar

Quer adicionar novas extensões ou pastas? É muito fácil!

Basta abrir o arquivo organizador.py e editar o dicionário MAPEAMENTO_PASTAS no topo do arquivo.

Exemplo: Para fazer com que arquivos .iso também sejam movidos para a pasta "Programas", basta adicionar uma nova linha:

MAPEAMENTO_PASTAS = {
    '.pdf': 'Documentos', 
    '.exe': 'Programas',
    '.iso': 'Programas', # <-- NOVA LINHA ADICIONADA
    '.png': 'Imagens', 
     ... 
}


## 📜 Licença

Este projeto é distribuído sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
