from google.cloud import bigquery
from datetime import timedelta, date

def monthly_photo_hp_hc_cps(request):

  # It runs monthly at 1th. Therefore, it gets the last day of the previous month
  today = date.today()-timedelta(days=1)
  # Set local client
  bq_client = bigquery.Client()

  #BigQuery queries
  create_hst_table =f"""
      create or replace table `data-lake.sandbox.hist_table_{today.year}_{today.month}` PARTITION BY tb_month AS
        SELECT
          *,
          date_sub(date_trunc(current_date('America/Sao_Paulo'), month), INTERVAL 1 month) as tb_month
        FROM `data-lake.sandbox.table` """

  # API requests
  bq_client.query(create_hst_table)

  return f"monthly_photo_table_name compleated"