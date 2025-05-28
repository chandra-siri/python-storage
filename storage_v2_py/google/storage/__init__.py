# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
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
#
from storage_v2_py.google.storage import gapic_version as package_version

__version__ = package_version.__version__


from storage_v2_py.google.storage_v2. services.storage.client import StorageClient
from storage_v2_py.google.storage_v2. services.storage.async_client import StorageAsyncClient

from storage_v2_py.google.storage_v2. types.storage import AppendObjectSpec
from storage_v2_py.google.storage_v2. types.storage import BidiReadHandle
from storage_v2_py.google.storage_v2. types.storage import BidiReadObjectError
from storage_v2_py.google.storage_v2. types.storage import BidiReadObjectRedirectedError
from storage_v2_py.google.storage_v2. types.storage import BidiReadObjectRequest
from storage_v2_py.google.storage_v2. types.storage import BidiReadObjectResponse
from storage_v2_py.google.storage_v2. types.storage import BidiReadObjectSpec
from storage_v2_py.google.storage_v2. types.storage import BidiWriteHandle
from storage_v2_py.google.storage_v2. types.storage import BidiWriteObjectRedirectedError
from storage_v2_py.google.storage_v2. types.storage import BidiWriteObjectRequest
from storage_v2_py.google.storage_v2. types.storage import BidiWriteObjectResponse
from storage_v2_py.google.storage_v2. types.storage import Bucket
from storage_v2_py.google.storage_v2. types.storage import BucketAccessControl
from storage_v2_py.google.storage_v2. types.storage import CancelResumableWriteRequest
from storage_v2_py.google.storage_v2. types.storage import CancelResumableWriteResponse
from storage_v2_py.google.storage_v2. types.storage import ChecksummedData
from storage_v2_py.google.storage_v2. types.storage import CommonObjectRequestParams
from storage_v2_py.google.storage_v2. types.storage import ComposeObjectRequest
from storage_v2_py.google.storage_v2. types.storage import ContentRange
from storage_v2_py.google.storage_v2. types.storage import CreateBucketRequest
from storage_v2_py.google.storage_v2. types.storage import CustomerEncryption
from storage_v2_py.google.storage_v2. types.storage import DeleteBucketRequest
from storage_v2_py.google.storage_v2. types.storage import DeleteObjectRequest
from storage_v2_py.google.storage_v2. types.storage import GetBucketRequest
from storage_v2_py.google.storage_v2. types.storage import GetObjectRequest
from storage_v2_py.google.storage_v2. types.storage import ListBucketsRequest
from storage_v2_py.google.storage_v2. types.storage import ListBucketsResponse
from storage_v2_py.google.storage_v2. types.storage import ListObjectsRequest
from storage_v2_py.google.storage_v2. types.storage import ListObjectsResponse
from storage_v2_py.google.storage_v2. types.storage import LockBucketRetentionPolicyRequest
from storage_v2_py.google.storage_v2. types.storage import MoveObjectRequest
from storage_v2_py.google.storage_v2. types.storage import Object
from storage_v2_py.google.storage_v2. types.storage import ObjectAccessControl
from storage_v2_py.google.storage_v2. types.storage import ObjectChecksums
from storage_v2_py.google.storage_v2. types.storage import ObjectRangeData
from storage_v2_py.google.storage_v2. types.storage import Owner
from storage_v2_py.google.storage_v2. types.storage import ProjectTeam
from storage_v2_py.google.storage_v2. types.storage import QueryWriteStatusRequest
from storage_v2_py.google.storage_v2. types.storage import QueryWriteStatusResponse
from storage_v2_py.google.storage_v2. types.storage import ReadObjectRequest
from storage_v2_py.google.storage_v2. types.storage import ReadObjectResponse
from storage_v2_py.google.storage_v2. types.storage import ReadRange
from storage_v2_py.google.storage_v2. types.storage import ReadRangeError
from storage_v2_py.google.storage_v2. types.storage import RestoreObjectRequest
from storage_v2_py.google.storage_v2. types.storage import RewriteObjectRequest
from storage_v2_py.google.storage_v2. types.storage import RewriteResponse
from storage_v2_py.google.storage_v2. types.storage import ServiceConstants
from storage_v2_py.google.storage_v2. types.storage import StartResumableWriteRequest
from storage_v2_py.google.storage_v2. types.storage import StartResumableWriteResponse
from storage_v2_py.google.storage_v2. types.storage import UpdateBucketRequest
from storage_v2_py.google.storage_v2. types.storage import UpdateObjectRequest
from storage_v2_py.google.storage_v2. types.storage import WriteObjectRequest
from storage_v2_py.google.storage_v2. types.storage import WriteObjectResponse
from storage_v2_py.google.storage_v2. types.storage import WriteObjectSpec

__all__ = ('StorageClient',
    'StorageAsyncClient',
    'AppendObjectSpec',
    'BidiReadHandle',
    'BidiReadObjectError',
    'BidiReadObjectRedirectedError',
    'BidiReadObjectRequest',
    'BidiReadObjectResponse',
    'BidiReadObjectSpec',
    'BidiWriteHandle',
    'BidiWriteObjectRedirectedError',
    'BidiWriteObjectRequest',
    'BidiWriteObjectResponse',
    'Bucket',
    'BucketAccessControl',
    'CancelResumableWriteRequest',
    'CancelResumableWriteResponse',
    'ChecksummedData',
    'CommonObjectRequestParams',
    'ComposeObjectRequest',
    'ContentRange',
    'CreateBucketRequest',
    'CustomerEncryption',
    'DeleteBucketRequest',
    'DeleteObjectRequest',
    'GetBucketRequest',
    'GetObjectRequest',
    'ListBucketsRequest',
    'ListBucketsResponse',
    'ListObjectsRequest',
    'ListObjectsResponse',
    'LockBucketRetentionPolicyRequest',
    'MoveObjectRequest',
    'Object',
    'ObjectAccessControl',
    'ObjectChecksums',
    'ObjectRangeData',
    'Owner',
    'ProjectTeam',
    'QueryWriteStatusRequest',
    'QueryWriteStatusResponse',
    'ReadObjectRequest',
    'ReadObjectResponse',
    'ReadRange',
    'ReadRangeError',
    'RestoreObjectRequest',
    'RewriteObjectRequest',
    'RewriteResponse',
    'ServiceConstants',
    'StartResumableWriteRequest',
    'StartResumableWriteResponse',
    'UpdateBucketRequest',
    'UpdateObjectRequest',
    'WriteObjectRequest',
    'WriteObjectResponse',
    'WriteObjectSpec',
)
