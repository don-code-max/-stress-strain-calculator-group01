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


def validate_positive_number(value, parameter_name):
    """Validate that a number is strictly positive."""
    if value <= 0:
        raise ValueError(f"{parameter_name} must be positive, got {value}")
    return value


def validate_non_negative(value, parameter_name):
    """Validate that a number is zero or positive."""
    if value < 0:
        raise ValueError(f"{parameter_name} cannot be negative, got {value}")
    return value


def validate_force(value):
    """Validate the applied force input."""
    return validate_positive_number(value, "Force")


def validate_area(value):
    """Validate the cross-sectional area input."""
    return validate_positive_number(value, "Area")


def validate_original_length(value):
    """Validate the original length input."""
    return validate_positive_number(value, "Original length")


def validate_change_in_length(value):
    """Validate the change in length input."""
    return validate_non_negative(value, "Change in length")


def validate_yield_strength_input(value):
    """Validate a custom yield strength input."""
    return validate_positive_number(value, "Yield strength")


def validate_youngs_modulus_input(value):