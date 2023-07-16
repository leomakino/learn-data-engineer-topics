from google.cloud import storage
import os
import pandas as pd
from datetime import datetime, timedelta

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/credentials.json"

# Set Client
storage_client = storage.Client(project='project_id')

# Set variables
bucket_data = storage_client.get_bucket('bucket-data')

query_distinct_ids = """
SELECT
  distinct color, format_timestamp('%d-%m-%Y_%H-%M',extraction_date) as extraction_date
FROM `project_id.dataset.table_3` 
WHERE DATE(extraction_date) = "2023-04-11"
"""

def query_shirt_by_color(color):
    """
    DOCUMENTATION
    """

    query_shirt_by_color = f"""
    SELECT
        field_1,
        field_2
    FROM `project_id.dataset.table_1` 
    WHERE DATE(extraction_date) = "2023-04-11"
    and color = "{color}"
    """

    df = pd.read_gbq(query_shirt_by_color, project_id='project_id',dialect='standard')
    return df

def query_campos_shirt_by_size(color):
    """
    DOCUMENTATION
    """

    query = f"""
    with size as (
        SELECT
            field_1,
            field_2
        FROM `project_id.dataset.table_2` 
        WHERE DATE(extraction_date) = "2023-04-11"
    ), temp as (
      select 
        distinct color,
        size
      from `project_id.dataset.table_1`
      WHERE DATE(extraction_date) = "2023-04-11"
    )
    select 
      size.size,
      temp.color,
    from size
    left join temp
    on size.key1 = temp.key2
    where size.color = "{color}"
    """

    df = pd.read_gbq(query, project_id='project_id',dialect='standard')
    return df


def query_from_bq():
    """
    Query from Bigquery;

    Save csv file per cp.
    """

    # Query distinct cp values.
    df_ids_list = pd.read_gbq(query_distinct_ids, project_id='project_id',dialect='standard')

    df_shirt_by_size_full = pd.DataFrame()

    for color,extraction_date in df_ids_list.itertuples(index=False):

        # Load data from Google BigQuery
        df_shirt_by_color = query_shirt_by_color(color)
        df_shirt_by_size = query_campos_shirt_by_size(color)

        # Blob names template
        blob_dest_size = f'gs://bucket-data/size/dt={extraction_date[:10]}/size_{color}_{extraction_date}.csv'
        blob_dest_color = f'gs://bucket-data/color/dt={extraction_date[:10]}/{color}_{extraction_date}.csv'

        # Create Csvs
        df_shirt_by_size.to_csv(blob_dest_size, index=False)
        df_shirt_by_color.to_csv(blob_dest_color, index=False)

        # Open created csvs
        blob_size_opened = bucket_data.blob(blob_dest_size)
        blob_shirt_opened = bucket_data.blob(blob_dest_color)

        # Create URLs
        url_size = blob_size_opened.generate_signed_url(
            version="v2",
            # This URL is valid for 20 minutes
            expiration=timedelta(minutes=20),
            # Allow GET requests using this URL.
            method="GET",
        )

        url_shirt = blob_shirt_opened.generate_signed_url(
            version="v2",
            # This URL is valid for 15 minutes
            expiration=timedelta(minutes=20),
            # Allow GET requests using this URL.
            method="GET",
        )

        # Add new columns
        df_shirt_by_size["SIZE_URL"] = url_size
        df_shirt_by_size["SIZE_TYPE"] = 'text/csv'
        df_shirt_by_size["SIZE_START_DATE"] = datetime.now()  
        df_shirt_by_size["SIZE_END_DATE"] = datetime.now() + timedelta(minutes=20)
        df_shirt_by_size["COLOR_URL"] = url_shirt
        df_shirt_by_size["COLOR_TYPE"] = 'text/csv'
        df_shirt_by_size["COLOR_DATA_INICIO"] = datetime.now()
        df_shirt_by_size["COLOR_END_DATE"] = datetime.now() + timedelta(minutes=20)

        # Append lines to the full dataframe
        df_shirt_by_size_full = df_shirt_by_size_full.append(df_shirt_by_size, ignore_index = True)

    # Insert data into DB
    df_shirt_by_size_full.to_csv(f'gs://bucket-data/color_size/full.csv', index=False)

query_from_bq()