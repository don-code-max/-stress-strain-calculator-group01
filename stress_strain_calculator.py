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

    
def get_materials_database():
    """Return the dictionary of predefined material properties."""
    return MATERIALS_DATABASE


def get_material_properties(material_name, database):
    """Retrieve the properties for a given material."""
    if material_name not in database:
        raise KeyError(f"Material '{material_name}' not found in database.")
    return database[material_name]


def create_calculation_record(material, inputs, results):
    """Build a single calculation record from material, inputs, and results."""
    record = {"material": material}
    record.update(inputs)
    record.update(results)
    return record


def add_to_history(history_list, record):
    """Append a calculation record to the session history list."""
    history_list.append(record)


def display_material_menu(database):
    """Print the material selection menu, including a Custom option."""
    print("Select Material:")
    material_names = list(database.keys())
    for i, name in enumerate(material_names, start=1):
        print(f"{i}. {name}")
    print(f"{len(material_names) + 1}. Custom")


def display_selected_material(material_name, properties):
    """Print the chosen material's name, yield strength, and Young's modulus."""
    print(f"\nSelected Material: {material_name}")
    print(f"Yield Strength    : {properties['yield_strength'] / 1e6:.2f} MPa")
    print(f"Young's Modulus   : {properties['youngs_modulus'] / 1e9:.2f} GPa\n")


def display_calculation_results(record):
    """Format and print the results of one calculation."""
    print()
    print("=== RESULTS ===")
    print(f"Material            : {record['material']}")
    print(f"Applied Force       : {record['force']:.2f} N")
    print(f"Cross-Sectional Area: {record['area']:.6f} m^2")
    print(f"Original Length     : {record['original_length']:.4f} m")
    print(f"Change in Length    : {record['change_in_length']:.4f} m")
    print()
    print(f"Stress              : {record['stress']:.2f} Pa ({record['stress'] / 1e6:.2f} MPa)")
    print(f"Strain              : {record['strain']:.6f}")
    print(f"Young's Modulus     : {record['youngs_modulus'] / 1e9:.2f} GPa")
    print()
    print("=== Analysis Complete ===")
    print()


def display_safety_analysis(stress, yield_strength, safety_factor):
    """Print the yield strength and a STATUS line describing material safety."""
    print(f"Yield Strength      : {yield_strength:.2f} Pa ({yield_strength / 1e6:.2f} MPa)")
    print(f"Factor of Safety    : {safety_factor:.2f}")
    if stress >= yield_strength:
        status = f"WARNING - Material failure expected! Factor of safety: {safety_factor:.2f}"
    elif safety_factor < 1.25:
        status = f"CAUTION - Factor of safety: {safety_factor:.2f}"
    else:
        status = f"SAFE - Factor of safety: {safety_factor:.2f}"
    print(f"STATUS: {status}\n")


def display_session_summary(history, unique_materials):
    """Print the end-of-session summary and detailed history."""
    print("\n=== SESSION SUMMARY ===")
    total_calcs = len(history)
    print(f"Total calculations performed: {total_calcs}")

    if total_calcs == 0:
        return

    print(f"Unique materials tested: {', '.join(unique_materials)} ({len(unique_materials)} materials)")

    highest_stress_record = max(history, key=lambda x: x["stress"])
    avg_strain = sum(record["strain"] for record in history) / total_calcs

    print(f"Highest Stress Experienced: {highest_stress_record['stress'] / 1e6:.2f} MPa "
          f"(Material: {highest_stress_record['material']})")
    print(f"Average Strain Across All Tests: {avg_strain:.6f}")

    print("\n--- Detailed History ---")
    for i, record in enumerate(history, 1):
        print(f"Test {i}: {record['material']} | Force: {record['force']} {UNITS[0]} | "
              f"Stress: {record['stress'] / 1e6:.2f} MPa | FOS: {record['factor_of_safety']:.2f}")