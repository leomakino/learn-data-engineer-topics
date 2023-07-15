from google.cloud import storage
import os
import csv
import tarfile
import io


# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/file_name.json"

# Set client
client = storage.Client(project='project_id')

# Variables
input_bucket = client.get_bucket('input_bucket_name')
output_bucket = client.get_bucket('output_bucket_name')
tar_blob = 'tar_blob_directory.tar'

# Dicts
extracted_tar_file = {"file_name_2023_07_15.txt" : "any_value"}

def write_read(input_bucket, tar_blob):
    """Extract a specific tar file, read it as txt and write as a csv
    This code is adapted to run on Google Cloud Function
    """

    input_blob_name = input_bucket.get_blob(tar_blob)
    input_blob = input_bucket.get_blob(tar_blob).download_as_string()

    
    filedate = input_blob_name.name[5:].split('.')[0]

    tar = tarfile.open(fileobj=io.BytesIO(input_blob))

    for arquivo in tar.getnames():
        if arquivo in extracted_tar_file:
            file_object = tar.extractfile(arquivo)
            file_object_list = io.TextIOWrapper(file_object).read()


        blob_dest = f"file_folder/filename_{filedate}.csv"
        blob_dst = output_bucket.blob(blob_dest)

        with blob_dst.open('w', newline='') as file:
            writer = csv.writer(file)     
            writer.writerow([filedate, file_object_list])


write_read(input_bucket, tar_blob)