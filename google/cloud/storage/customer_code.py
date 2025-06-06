import sys
from google.cloud import storage

bucket_name = 'chandrasiri-pysdk-grpc'
object_name = 'ask_chandrasiri_before_deleting'

grpc_client: storage.Client = storage.GrpcClient()


bucket = grpc_client.bucket(bucket_name=bucket_name)
blob = bucket.blob(object_name)
blob_contents  = blob.download_as_bytes()
print(blob_contents)