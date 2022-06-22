# encrypt_data.py

import json
from util import encrypt_symmetric, write_to_blob

def encrypt_data():
    # project attributes
    project_id = 'cbisong-sandbox'
    location_id = 'global'
    key_ring_id = 'tds-keyring'
    key_id = 'tds-symmetric-key'
    
    # gcs attributes
    bucket_name = 'cbisong-ta-data-engineer'
    
    # read plaintext
    plaintext = json.dumps(json.load(open('data/sample_data.json')))
    
    encrypted_file = encrypt_symmetric(project_id, location_id,
                                       key_ring_id, key_id, plaintext)
    
    with open('data/sample_data.json.enc', "wb") as file:
        file.write(encrypted_file)
        
    # save encrypted data to GCP
    file_name = 'landing_zone/sample_data.json.enc'
    
    write_to_blob(bucket_name, file_name, encrypted_file)
    
    print('File encryption completed')
    
if __name__ == '__main__':
    encrypt_data()
    