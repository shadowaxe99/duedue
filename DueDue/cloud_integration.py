```python
import os
import shutil
from google.cloud import storage

cloud_services = ["Google Cloud Storage", "Amazon S3", "Azure Blob Storage"]

def sync_to_cloud(service, bucket_name, source_file_name, destination_blob_name):
    if service == "Google Cloud Storage":
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")

    elif service == "Amazon S3":
        # Code for Amazon S3 integration goes here
        pass

    elif service == "Azure Blob Storage":
        # Code for Azure Blob Storage integration goes here
        pass

    else:
        print(f"Unsupported service: {service}. Please choose from {cloud_services}.")

def backup_to_local(source_file_name, backup_directory):
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    shutil.copy2(source_file_name, backup_directory)

    print(f"File {source_file_name} backed up to {backup_directory}.")
```