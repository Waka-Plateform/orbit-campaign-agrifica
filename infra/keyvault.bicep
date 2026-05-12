param location string
param keyVaultName string
param tenantId string
param principalId string
resource kv 'Microsoft.KeyVault/vaults@2023-07-01' = { name: keyVaultName location: location properties: { tenantId: tenantId sku: { family: 'A' name: 'standard' } enableRbacAuthorization: true enablePurgeProtection: true enabledForTemplateDeployment: true } }
resource secretsUser 'Microsoft.Authorization/roleAssignments@2022-04-01' = { name: guid(kv.id, principalId, 'Key Vault Secrets User') scope: kv properties: { principalId: principalId roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', '4633458b-17de-408a-b874-0445c86b69e6') principalType: 'ServicePrincipal' } }
output keyVaultUri string = kv.properties.vaultUri
