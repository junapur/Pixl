from pydantic import BaseModel
from pydantic_extra_types.color import Color
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)


class EmbedColors(BaseModel):
    main: Color = Color("#3699FB")
    warn: Color = Color("#FBBD36")
    error: Color = Color("#FB3640")


class Settings(BaseSettings):
    token: str
    prefix: str = "+"
    when_mentioned: bool = True
    embed_colors: EmbedColors = EmbedColors()
    error_messages: list[str] = [
        "An error occurred.",
        "Oops! Something went wrong.",
        "This is awkward...",
        "Erm...",
    ]
    model_config = SettingsConfigDict(frozen=True, yaml_file="config.yaml")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (YamlConfigSettingsSource(settings_cls),)
