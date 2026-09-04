from dataclasses import dataclass


UNITS = ("N", "m²", "m", "Pa")

@dataclass
class MaterialProperties:
    """Stores the properties of a material."""

    density: float
    yield_strength: float
    youngs_modulus: float

    def __post_init__(self):
        if self.density <= 0:
            raise ValueError("Density must be positive")
        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be positive")
        if self.youngs_modulus <= 0:
            raise ValueError("Young's modulus must be positive")