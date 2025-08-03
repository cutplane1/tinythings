from dataclasses import dataclass

@dataclass
class Game:
    name: str
    genres: list[str]
    optimization_level: str
    features: list[str]
    folder_to_save: str