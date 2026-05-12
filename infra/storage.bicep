param location string
param storageAccountName string
resource st 'Microsoft.Storage/storageAccounts@2023-05-01' = { name: storageAccountName location: location sku: { name: 'Standard_LRS' } kind: 'StorageV2' properties: { allowBlobPublicAccess: false minimumTlsVersion: 'TLS1_2' supportsHttpsTrafficOnly: true } }
resource artifacts 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = { name: '${st.name}/default/artifacts' properties: { publicAccess: 'None' } }
output tableEndpoint string = st.properties.primaryEndpoints.table
output blobEndpoint string = st.properties.primaryEndpoints.blob
output storageId string = st.id
