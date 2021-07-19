from azure.common.credentials import ServicePrincipalCredentials
from azure.storage.blob import BlockBlobService
from azure.storage.common import TokenCredential

TENANT_ID = "eb120e12-65f1-477a-be8c-fe4f65926724"
CLIENT_ID = "87255a9f-9e0c-4275-a5f2-9cad5ee7d2a4"
CLIENT_SECRET = "5c22_.6_dFxTL19GHysAhIl5pjz~_nnHkH"
RESOURCE = "https://storage.azure.com/"

credentials = ServicePrincipalCredentials(
    client_id = CLIENT_ID,
    secret = CLIENT_SECRET,
    tenant = TENANT_ID,
    resource = RESOURCE
) 
token_credential = TokenCredential(credentials.token["access_token"])

ACCOUNT_NAME = "clcmdatalakeaccount"
CONTAINER_NAME = "clcmdatalakeaccount"
blobService = BlockBlobService(account_name=ACCOUNT_NAME, token_credential=token_credential)
blob = blobService.get_blob_to_text(CONTAINER_NAME, "test.txt")
print(blob.content)