#!/usr/bin/env python

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# [START storage_file_download_into_memory]
from google.cloud import storage
from storage_v2_py.google import storage_v2
import time


def download_blob_into_memory(bucket_name, blob_name):
    """Downloads a blob into memory."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(blob_name)
    contents = blob.download_as_bytes()

    print(
        "Downloaded storage object {} from bucket {} as the following bytes object: {}.".format(
            blob_name, bucket_name, contents.decode("utf-8")
        )
    )


# [END storage_file_download_into_memory]

if __name__ == "__main__":
    download_blob_into_memory(
        bucket_name=sys.argv[1],
        blob_name=sys.argv[2],
    )
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
