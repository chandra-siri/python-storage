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
from google.storage import gapic_version as package_version

__version__ = package_version.__version__


from google.storage_v2.services.storage.client import StorageClient
from google.storage_v2.services.storage.async_client import StorageAsyncClient

from google.storage_v2.types.storage import AppendObjectSpec
from google.storage_v2.types.storage import BidiReadHandle
from google.storage_v2.types.storage import BidiReadObjectError
from google.storage_v2.types.storage import BidiReadObjectRedirectedError
from google.storage_v2.types.storage import BidiReadObjectRequest
from google.storage_v2.types.storage import BidiReadObjectResponse
from google.storage_v2.types.storage import BidiReadObjectSpec
from google.storage_v2.types.storage import BidiWriteHandle
from google.storage_v2.types.storage import BidiWriteObjectRedirectedError
from google.storage_v2.types.storage import BidiWriteObjectRequest
from google.storage_v2.types.storage import BidiWriteObjectResponse
from google.storage_v2.types.storage import Bucket
from google.storage_v2.types.storage import BucketAccessControl
from google.storage_v2.types.storage import CancelResumableWriteRequest
from google.storage_v2.types.storage import CancelResumableWriteResponse
from google.storage_v2.types.storage import ChecksummedData
from google.storage_v2.types.storage import CommonObjectRequestParams
from google.storage_v2.types.storage import ComposeObjectRequest
from google.storage_v2.types.storage import ContentRange
from google.storage_v2.types.storage import CreateBucketRequest
from google.storage_v2.types.storage import CustomerEncryption
from google.storage_v2.types.storage import DeleteBucketRequest
from google.storage_v2.types.storage import DeleteObjectRequest
from google.storage_v2.types.storage import GetBucketRequest
from google.storage_v2.types.storage import GetObjectRequest
from google.storage_v2.types.storage import ListBucketsRequest
from google.storage_v2.types.storage import ListBucketsResponse
from google.storage_v2.types.storage import ListObjectsRequest
from google.storage_v2.types.storage import ListObjectsResponse
from google.storage_v2.types.storage import LockBucketRetentionPolicyRequest
from google.storage_v2.types.storage import MoveObjectRequest
from google.storage_v2.types.storage import Object
from google.storage_v2.types.storage import ObjectAccessControl
from google.storage_v2.types.storage import ObjectChecksums
from google.storage_v2.types.storage import ObjectRangeData
from google.storage_v2.types.storage import Owner
from google.storage_v2.types.storage import ProjectTeam
from google.storage_v2.types.storage import QueryWriteStatusRequest
from google.storage_v2.types.storage import QueryWriteStatusResponse
from google.storage_v2.types.storage import ReadObjectRequest
from google.storage_v2.types.storage import ReadObjectResponse
from google.storage_v2.types.storage import ReadRange
from google.storage_v2.types.storage import ReadRangeError
from google.storage_v2.types.storage import RestoreObjectRequest
from google.storage_v2.types.storage import RewriteObjectRequest
from google.storage_v2.types.storage import RewriteResponse
from google.storage_v2.types.storage import ServiceConstants
from google.storage_v2.types.storage import StartResumableWriteRequest
from google.storage_v2.types.storage import StartResumableWriteResponse
from google.storage_v2.types.storage import UpdateBucketRequest
from google.storage_v2.types.storage import UpdateObjectRequest
from google.storage_v2.types.storage import WriteObjectRequest
from google.storage_v2.types.storage import WriteObjectResponse
from google.storage_v2.types.storage import WriteObjectSpec

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
