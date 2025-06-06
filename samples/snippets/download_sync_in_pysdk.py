import time
# from google import storage_v2
from storage_v2_py.google import storage_v2

transport_cls = storage_v2.StorageClient.get_transport_class()
channel = transport_cls.create_channel(attempt_direct_path=True)
transport = transport_cls(channel=channel)
client = storage_v2.StorageClient(transport=transport)

bucket='projects/_/buckets/chandrasiri-pysdk-grpc'

start = time.monotonic_ns()
stream = client.read_object(request=storage_v2.ReadObjectRequest(bucket=bucket, object='gapic'))
total = 0
iter_count = 0
for response in stream:
    total += len(response.checksummed_data.content)
    iter_count += 1
print('iter_count', iter_count)

print("download ran in {} ns and got {} bytes".format(time.monotonic_ns() - start, total))