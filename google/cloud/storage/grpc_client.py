from google.cloud import storage
from storage_v2_py.google.storage_v2 import StorageClient as StorageGapicClient
from google.cloud.storage.bucket import Bucket

class GrpcClient(storage.Client):
    def __init__(
        self,
        project='chandrasiri-gcs-prober', # for time being
        credentials=None,
        _http=None,
        client_info=None,
        client_options=None,
        use_auth_w_custom_endpoint=True,
        extra_headers={},
        *,
        api_key=None,
    ):
        super().__init__(
            project,
            credentials,
            _http,
            client_info,
            client_options,
            use_auth_w_custom_endpoint,
            extra_headers,
            api_key=api_key,
        )
        # transport_cls = storage_v2.StorageClient.get_transport_class()
        # channel = transport_cls.create_channel(attempt_direct_path=True)
        # transport = transport_cls(channel=channel)
        self.gapic_client = StorageGapicClient(
            credentials=credentials, 
            client_options=client_options, 
            client_info=client_info)
    
    def bucket(self, bucket_name, user_project=None, generation=None):
        # same as super.
        """Factory constructor for bucket object.

        .. note::
          This will not make an HTTP request; it simply instantiates
          a bucket object owned by this client.

        :type bucket_name: str
        :param bucket_name: The name of the bucket to be instantiated.

        :type user_project: str
        :param user_project: (Optional) The project ID to be billed for API
                             requests made via the bucket.

        :type generation: int
        :param generation: (Optional) If present, selects a specific revision of
                           this bucket.

        :rtype: :class:`google.cloud.storage.bucket.Bucket`
        :returns: The bucket object created.
        """
        return Bucket(
            client=self.gapic_client,
            name=bucket_name,
            user_project=user_project,
            generation=generation,
        )
    # @property
    # def _connection(self):
    #     """Get connection or batch on the client.

    #     :rtype: :class:`google.cloud.storage._http.Connection`
    #     :returns: The connection set on the client, or the batch
    #               if one is set.
    #     """
    #     return super()._connection




