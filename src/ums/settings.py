from pydantic_settings import BaseSettings


class FileSettings(BaseSettings):
    endpoints_file: str = "ENDPOINTS.md"


class EndpointSettings(BaseSettings):
    # login_ep: str = "/login"
    # register_ep: str = "/register"
    # user_me_ep: str = "/users/me"
    # logout_ep: str = "/logout"

    # Test enpoints
    ping_ep: str = "/ping"


class Settings(BaseSettings):
    file: FileSettings = FileSettings()
    endpoint: EndpointSettings = EndpointSettings()


settings = Settings()
