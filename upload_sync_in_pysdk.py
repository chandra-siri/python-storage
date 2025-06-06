import time
from storage_v2_py.google import storage_v2
from google.api_core import grpc_helpers

channel = grpc_helpers.create_channel('storage.googleapis.com', attempt_direct_path=True)
transport_cls = storage_v2.StorageClient.get_transport_class()
transport = transport_cls(channel=channel)
client = storage_v2.StorageClient(transport=transport)

bucket='projects/_/buckets/chandrasiri-pysdk-grpc-ctop'
object_name = 'gapic_from_cloud_top'

test_bytes_16MiB = b"thisisatestbytes" * (1024 * 1024 * 16)

def request_generator():
    payload = test_bytes_16MiB
    CHUNK_SIZE = 2 * 1024 * 1024
    byte = 0
    final_msg = False
    while byte < len(payload):
        if (byte+CHUNK_SIZE) >= len(payload):
            final_msg = True
        request = storage_v2.WriteObjectRequest(
            write_object_spec={
                "resource": {
                    "name": object_name,
                    "bucket": bucket
                    }
                }, 
            write_offset=byte,
            finish_write=final_msg,
            checksummed_data={
                "content": payload[byte:min((byte+CHUNK_SIZE),
                                             len(payload))]
                }
            )
        yield request
        byte += CHUNK_SIZE

start = time.monotonic_ns()
response = client.write_object(requests=request_generator(), metadata=[("x-goog-request-params", "bucket={}".format(bucket))])
print("upload ran in {} ns".format(time.monotonic_ns() - start))