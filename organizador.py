import os
import shutil

MAPEAMENTO_PASTAS = {'.7z': 'Arquivos Compactados', '.pdf': 'Documentos', '.exe': 'Programas', '.png': 'Imagens', '.jpg': 'Imagens', '.jpeg': 'Imagens', '.doc': 'Documentos', '.docx': 'Documentos', '.xls': 'Documentos', '.xlsx': 'Documentos', '.ppt': 'Documentos', '.pptx': 'Documentos', '.txt': 'Documentos', '.csv': 'Documentos', '.rar': 'Arquivos Compactados', '.zip': 'Arquivos Compactados', '.mp3': 'Musicas', '.mp4': 'Videos'}

caminho_home = os.path.expanduser('~') 
caminho_downloads = os.path.join(caminho_home, 'Downloads')

for nome_arquivo in os.listdir(caminho_downloads):
    caminho_completo = os.path.join(caminho_downloads, nome_arquivo)
    if os.path.isdir(caminho_completo):
        print(f'Ignorando Pasta')
        continue

    extensao = os.path.splitext(caminho_completo)[1].lower()
    if extensao in MAPEAMENTO_PASTAS:
        nome_pasta_destino = MAPEAMENTO_PASTAS[extensao]

        caminho_destino = os.path.join(caminho_downloads, nome_pasta_destino)

        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)
            print(f'Pasta "{nome_pasta_destino}" criada com sucesso.')
        try:
            shutil.move(caminho_completo, caminho_destino)
            print(f'Arquivo movido para a pasta "{nome_pasta_destino}" com sucesso.') 
        except Exception as e:
            print(f'Erro ao mover o arquivo: {e}')

    else:
        if extensao:
            print(f'Extensao "{extensao}" nao encontrada. Ignorando o arquivo.')

print('---')
print('Organizacao concluida com sucesso.')
print('---')