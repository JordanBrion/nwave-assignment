import numpy as np

class Disk:
    def __init__(self, radius, position, color) -> None:
        self.radius = radius
        self.position = np.array(position)
        self.color = color