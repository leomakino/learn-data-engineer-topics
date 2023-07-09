import functions_framework
from datetime import date
from urllib.request import urlopen
import pandas as pd
from zipfile import ZipFile
from io import BytesIO

@functions_framework.http
def extract_dados_anatel_acessos(request):
    """
    Objective: Get the latest year csv.
    This code is adapted to run on Google Cloud Function
    configuration settings: 4 GB Ram to be able to extract the zip file in the memory.
    """
    bucket_dst = 'gs://bucket-name'

    # Source link
    url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"

    # Returns the current local date
    today = date.today()

    # Target table within the acessos_banda_larga_fixa.zip file
    current_year_data = f"Acessos_Banda_Larga_Fixa_{today.year}.csv"

    # Csv final name
    csv_name = f"{bucket_dst}/ANATEL_ACESSOS_BANDA_LARGA_FIXA_{today.year}.csv"

    # Get http response
    zip_request = urlopen(url)

    # Get zip file
    acessos_banda_larga_fixa_zip = ZipFile(BytesIO(zip_request.read()))

    try:
        # Read csv file zipped into DataFrame
        df_current_year_data = pd.read_csv(acessos_banda_larga_fixa_zip.open(current_year_data), sep=';', encoding='utf-8')

        # Write the dataframe to csv file
        df_current_year_data.to_csv(csv_name, sep=';', encoding='utf-8', index=False)
    except:
        # Do the same but with the previous year
        current_year_data = f"Acessos_Banda_Larga_Fixa_{today.year - 1}.csv"
        csv_name = f"{bucket_dst}/ANATEL_ACESSOS_BANDA_LARGA_FIXA_{today.year - 1}.csv"
        
        df_current_year_data = pd.read_csv(acessos_banda_larga_fixa_zip.open(current_year_data), sep=';', encoding='utf-8')
        df_current_year_data.to_csv(csv_name, sep=';', encoding='utf-8', index=False)

    return f'arquivo criado: {csv_name}'
