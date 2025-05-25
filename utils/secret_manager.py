import os

from infisical_sdk import InfisicalSDKClient

class InfisicalSecretManager:
    def __init__(self):
        self.infisical_host = os.getenv("INFISICAL_HOST", "http://infisical")
        self._infisical_token = os.getenv("INFISICAL_TOKEN", "st.4a03109c-48a5-4d92-a0b3-adaac7f60c15.66c306d7d7b0296377387b033a7a4b70.91167ff77ff3eb438278b2004cafc6e3")
        self.infisical_cache_ttl = int(os.getenv("INFISICAL_CACHE_TTL", 300))
        self.infisical_project_id = os.getenv("INFISICAL_PROJECT_ID", "talent-retention-mlops")
        self.infisical_environment_slug = os.getenv("INFISICAL_ENVIRONMENT_SLUG", "dev")
        self.infisical_secret_path = os.getenv("INFISICAL_SECRET_PATH", "/")
    
    def _create_infisical_client(self) -> InfisicalSDKClient:
        return InfisicalSDKClient(
            host = self.infisical_host,
            token = self._infisical_token,
            cache_ttl = self.infisical_cache_ttl
        )
    
    def get_secret(self, secret_name: str) -> str:
        client = self._create_infisical_client()

        secret = client.secrets.get_secret_by_name(
            project_id = self.infisical_project_id,
            environment_slug = self.infisical_environment_slug,
            secret_path = self.infisical_secret_path,
            secret_name = secret_name
        )
        return secret.secretValue