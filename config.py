from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    work_time_methods: bool


BASE_DIR = Path(__file__).resolve().parent
work_time_methods = True

settings = Settings(work_time_methods)
