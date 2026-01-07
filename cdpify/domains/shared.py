import re
from dataclasses import asdict, dataclass, fields
from typing import Any, Self


@dataclass
class CDPModel:
    def to_cdp_params(self) -> dict[str, Any]:
        return {self._to_camel(k): v for k, v in asdict(self).items() if v is not None}

    @staticmethod
    def _to_camel(s: str) -> str:
        parts = s.split("_")
        return parts[0] + "".join(p.title() for p in parts[1:])

    @classmethod
    def from_cdp(cls, data: dict) -> Self:
        snake_data = {cls._to_snake(k): v for k, v in data.items()}
        valid_fields = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in snake_data.items() if k in valid_fields})

    @staticmethod
    def _to_snake(s: str) -> str:
        import re

        return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()
