from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, Field
import os

class AppSettings(BaseSettings):
    # App General Settings
    APP_TITLE: str = "AI Knowledge Assistant"
    DEBUG: bool = False
    
    # Storage Architecture Properties
    # Using Field to enforce strict configuration boundaries
    UPLOAD_DIR: str = Field(default="uploads", description="Directory for staging document uploads")
    MAX_FILE_SIZE_MB: int = Field(default=5, description="Maximum allowable PDF file size in Megabytes")

    @property
    def max_file_size_bytes(self) -> int:
        """Dynamically computes bytes from MB threshold."""
        return self.MAX_FILE_SIZE_MB * 1024 * 1024

    # Enforce loading configuration parameters directly via an external environment file
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # Safely drops extraneous system environment parameters
    )

# Instantiate a single global settings snapshot (Singleton Pattern)
settings = AppSettings()

# Proactively guarantee that the physical storage layout directory exists at compilation
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)