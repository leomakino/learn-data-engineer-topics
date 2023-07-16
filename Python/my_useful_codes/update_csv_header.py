import pandas as pd
from google.cloud import storage
import os

"""
Este código abre um csv, substitui o header da coluna 7 por um link
e faz o upload do novo csv
"""

# Credentials
credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/access.json"

# Set client and bucket
storage_client = storage.Client(project='project_id')
bucket_data = storage_client.get_bucket('bucket_name')

# Nomes dos arquivos
blob_source = 'FILE_20230330_112647.csv'
blob_dest = 'FILE_NEW_20230330_112647.csv'

# Abre os arquivos como blob
blob_opened = bucket_data.blob(blob_source)
blob_dest_opened = bucket_data.blob(blob_dest)

with blob_opened.open('r', newline='') as read_file:
    # Abro o arquivo como uma lista
    text_list = read_file.readlines()
    print(f"Leitura do arquivo de origem como uma lista é: {text_list}")

    # Pego o cabeçalho e transformo em uma lista
    leo_list = text_list[0].split(";")

    # Se o local de inserção do link for diferente da posição 6, criar regra para isso
    leo_list[6] = 'LINK_VEM_AQUI' # aqui vem o link

    # Retorno o cabeçalho de lista para o formato original com ;
    new_headers = ','.join(map(str, leo_list)).replace(',',";")
    text_list[0] = new_headers
    print(f"Conteúdo em formato de lista: {text_list}")

    # Transformo de lista para texto único.
    new_text = ','.join(map(str, text_list)).replace(',',"")
    print(f'A transformação em txt/plain é: {new_text}')

    # Uso da função upload_from_string para upar o texto único no novo bucket. O resultado final é um csv com o link incluido
    blob_dest_opened.upload_from_string(new_text)


