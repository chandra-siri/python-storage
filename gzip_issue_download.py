import os
from google.cloud import storage
from google.cloud.exceptions import NotFound

def download_gcs_object(gcs_uri: str, destination_file_name: str):
    if not gcs_uri.startswith("gs://"):
        raise ValueError("Invalid GCS URI. Must start with 'gs://'.")

    # Parse the GCS URI
    try:
        # Remove "gs://" prefix and split into bucket and object name
        path_parts = gcs_uri[5:].split("/", 1)
        bucket_name = path_parts[0]
        if len(path_parts) > 1 and path_parts[1]:
            blob_name = path_parts[1]
        else:
            raise ValueError(f"Invalid GCS URI: Missing object name in '{gcs_uri}'")
    except (IndexError, ValueError) as e:
        raise ValueError(f"Could not parse GCS URI '{gcs_uri}': {e}")

    destination_dir = os.path.dirname(destination_file_name)
    if destination_dir and not os.path.exists(destination_dir):
        print(f"Creating directory: {destination_dir}")
        os.makedirs(destination_dir)

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        if not blob.exists():
            print(f"Error: Object {blob_name} not found in bucket {bucket_name}.")
            return False

        print(f"Downloading gs://{bucket_name}/{blob_name} to {destination_file_name}...")
        blob.download_to_filename(destination_file_name)
        print(f"Successfully downloaded to {destination_file_name}")
        return True

    except NotFound:
        print(f"Error: Bucket '{bucket_name}' or Blob '{blob_name}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    import sys
    # --- Configuration ---
    # Replace with your actual GCS URI
    # gcs_object_uri = "gs://gzip-issue-bucket/sample-upload.png"
    gcs_object_uri = sys.argv[1]
    # Replace with your desired local file path for the download
    # local_download_path = "downloaded_sample_by_python_script.png"
    local_download_path = sys.argv[2]
    # --- End Configuration ---

    print(f"Attempting to download: {gcs_object_uri}")
    print(f"Target local path: {local_download_path}")

    success = download_gcs_object(gcs_object_uri, local_download_path)

    if success:
        print("Download process completed successfully.")
    else:
        print("Download process failed.")
