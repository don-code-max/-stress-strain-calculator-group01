class Material:
    """Base class for all materials."""

    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def can_withstand_stress(self, stress):
        return stress < self.properties.yield_strength

    def __str__(self):
        return f"{self.name} (Density: {self.properties.density} kg/m³)"


class Metal(Material):
    """Represents a metal material."""

    def __init__(self, name, properties, is_ferrous=False):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self):
        metal_type = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({metal_type} metal)"


class Plastic(Material):
    """Represents a plastic material."""

    def __init__(self, name, properties, plastic_type="Thermoplastic"):
        super().__init__(name, properties)
        self.plastic_type = plastic_type

    def __str__(self):
        return f"{self.name} ({self.plastic_type} plastic)"


class Composite(Material):
    """Represents a composite material."""

    def __init__(self, name, properties, reinforcement="Unknown"):
        super().__init__(name, properties)
        self.reinforcement = reinforcement

    def __str__(self):
        return f"{self.name} ({self.reinforcement} composite)"