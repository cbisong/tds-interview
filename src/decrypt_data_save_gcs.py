# decrypt_data_save_gcs.py

import json

from google.cloud import storage

from util import decrypt_symmetric, write_to_blob

def decrypt_data_save_gcs():
    # project attributes
    project_id = 'ebisong-sandbox'
    location_id = 'global'
    key_ring_id = 'tds-keyring'
    key_id = 'tds-symmetric-key'
    
    # gcs attributes
    bucket_name = 'cbisong-ta-data-engineer'
    
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob('data/sample_data.json.enc')
    
    # read plaintext
    ciphertext = blob.download_as_string()
    
    # read plaintext
    # ciphertext = open('data/sample_data.json.enc', 'rb').read()
    
    decrypted_file = decrypt_symmetric(project_id, location_id,
                                       key_ring_id, key_id,
                                       ciphertext)
    
    print(decrypted_file)
    
    # with open('data/sample_data.json.enc', "wb") as file:
    #     file.write(decrypted_file)
    
    # save decrypted data to GCP
    file_name = 'data/sample_data.json'
    
    write_to_blob(bucket_name, file_name, decrypted_file)
    
if __name__ == '__main__':
    decrypt_data_save_gcs()
    