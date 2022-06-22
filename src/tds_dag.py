from airflow.models import DAG
from airflow.decorators import dag
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from decrypt_data_save_gcs import decrypt_data_save_gcs
from load_json_gcs_to_bq import load_json_gcs_to_bq

default_args = {
    'owner': 'chiderabisong',
}

with DAG(
    'tds-decrypt-data-dag',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:
    dag.doc_md = "Workflow for decrypting data and storing \
    it to GCS(Google Cloud Storage) and BigQuery"

    t1 = PythonOperator(
        task_id='decrypt_data_save_gcs',
        python_callable=decrypt_data_save_gcs,
        op_kwargs={'data_path': 'data/sample_data.json.enc'},
    )
    t2 = PythonOperator(
        task_id='load_json_gcs_to_bq',
        python_callable=load_json_gcs_to_bq
    )

    t1 >> t2
