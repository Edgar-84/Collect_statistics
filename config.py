from dataclasses import dataclass


@dataclass
class Settings:
    work_time_methods: bool


work_time_methods = True

settings = Settings(work_time_methods)
