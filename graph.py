from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class ActivityNode:
    name: str
    time: int
    required: List[str]

    def __str__(self) -> str:
        return f"Activ {self.name} costs {self.time} requires {self.required}"
