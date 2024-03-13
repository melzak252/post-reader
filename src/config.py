import dacite

from dataclasses import dataclass
from pathlib import Path
from typing import Self

import tomllib
import json

@dataclass(frozen=True, slots=True)
class PrawConfig:
    client_id: str
    client_secret: str
    user_agent: str
    username: str
    password: str
    


@dataclass(frozen=True, slots=True)
class Config:
    praw: PrawConfig
    
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return dacite.from_dict(Config, data)  

    @classmethod
    def from_toml(cls, file_path: Path) -> Self:
        if(file_path.exists()):
            with open(file_path, "+rb") as f:
                config = tomllib.load(f)
                return dacite.from_dict(Config, config)  
        else:
            raise ValueError(f"file: {file_path} does not exists!")

    @classmethod
    def from_json(cls, file_path: Path) -> Self:
        if(file_path.exists()):
            with open(file_path) as f:
                config = json.load(f)
                return dacite.from_dict(Config, config)  
        else:
            raise ValueError(f"File: {file_path} does not exists!")