from pydantic import BaseModel


class ProtocolVersion(BaseModel):
    major: str
    minor: str


class ProtocolSpec(BaseModel):
    version: ProtocolVersion
    domains: list[dict]


class CDPSpecs(BaseModel):
    browser: ProtocolSpec
    js: ProtocolSpec

    @property
    def all_domains(self) -> list[dict]:
        return self.browser.domains + self.js.domains

    @property
    def version_string(self) -> str:
        return f"{self.browser.version.major}.{self.browser.version.minor}"
