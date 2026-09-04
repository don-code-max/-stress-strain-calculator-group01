UNITS = ("N", "m²", "m", "Pa")

MATERIALS_DATABASE = {
    "Steel": {"yield_strength": 250e6, "youngs_modulus": 200e9},
    "Aluminum": {"yield_strength": 95e6, "youngs_modulus": 69e9},
    "Titanium": {"yield_strength": 880e6, "youngs_modulus": 114e9},
}

def calculate_stress(force, area):
    """Calculate stress from applied force and cross-sectional area."""
    return force / area


def calculate_strain(original_length, change_in_length):
    """Calculate strain from original length and change in length."""
    return change_in_length / original_length


def calculate_youngs_modulus(stress, strain):
    """Calculate Young's modulus from stress and strain."""
    return stress / strain


def calculate_factor_of_safety(yield_strength, stress):
    """Calculate the factor of safety."""
    return yield_strength / stress