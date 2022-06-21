# decrypt_data_save_gcs.py

import json

from google.cloud import storage

from util import load_json_to_bq

def load_json_gcs_to_bq():
    # project attributes
    json_uri = 'gs://cbisong-ta-data-engineer/data/sample_data.json'
    
    project_id = 'ebisong-sandbox'
    dataset_name = 'tds_dataset'
    table_name = 'tds_table'
    
    table_id = f'{project_id}.{dataset_name}.{table_name}'
    
    # gcs attributes
    load_json_to_bq(json_uri, table_id)
    
if __name__ == '__main__':
    load_json_gcs_to_bq()
    