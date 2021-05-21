import numpy as np
from dataclasses import dataclass

@dataclass
class AudioArray:
    array: np.array
    sample_rate: int