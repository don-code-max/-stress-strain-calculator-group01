MATERIALS_DATABASE = {
    "Steel": {"yield_strength": 250e6, "youngs_modulus": 200e9},
    "Aluminum": {"yield_strength": 95e6, "youngs_modulus": 69e9},
    "Titanium": {"yield_strength": 880e6, "youngs_modulus": 114e9},
}

def get_materials_database():
    """Return the dictionary of predefined material properties."""
    return MATERIALS_DATABASE

def get_material_properties(material_name, database):
    """Retrieve the properties for a given material."""
    if material_name not in database:
        raise KeyError(f"Material '{material_name}' not found in database.")
    return database[material_name]