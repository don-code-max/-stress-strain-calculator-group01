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


def validate_non_zero(value, parameter_name):
    """Validate that a number is not zero, to prevent division-by-zero errors."""
    if value == 0:
        raise ValueError(f"{parameter_name} cannot be zero.")
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
    """Validate a custom Young's modulus input."""
    return validate_positive_number(value, "Young's modulus")


def get_validated_input(prompt, validator_func):
    """Prompt the user until they enter a value that passes validation."""
    while True:
        try:
            value = float(input(prompt))
            return validator_func(value)
        except ValueError as error:
            print(f"Invalid input: {error}")


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


def get_custom_material_properties():
    """Prompt the user for a custom material's yield strength and Young's modulus."""
    yield_strength = get_validated_input("Enter yield strength (MPa): ", validate_yield_strength_input) * 1e6
    youngs_modulus = get_validated_input("Enter Young's modulus (GPa): ", validate_youngs_modulus_input) * 1e9
    return {"yield_strength": yield_strength, "youngs_modulus": youngs_modulus}


def select_material_choice(database):
    """Show the material menu and return the chosen material's name and properties."""
    display_material_menu(database)
    material_names = list(database.keys())
    custom_option = len(material_names) + 1

    while True:
        choice = input(f"Enter choice (1-{custom_option}): ").strip()
        if not choice.isdigit():
            print("Please enter a valid number!")
            continue
        choice_num = int(choice)
        if 1 <= choice_num <= len(material_names):
            name = material_names[choice_num - 1]
            return name, get_material_properties(name, database)
        if choice_num == custom_option:
            return "Custom", get_custom_material_properties()
        print("Invalid choice. Please select a valid option.")


def collect_calculation_inputs():
    """Prompt for and validate force, area, original length, and change in length."""
    force = get_validated_input("Enter the applied force (N): ", validate_force)
    area = get_validated_input("Enter the cross-sectional area (m^2): ", validate_area)
    original_length = get_validated_input("Enter the original length (m): ", validate_original_length)
    change_in_length = get_validated_input("Enter the change in length (m): ", validate_change_in_length)
    return {
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length,
    }


def compute_results(inputs, properties):
    """Compute stress, strain, Young's modulus, and factor of safety."""
    stress = calculate_stress(inputs["force"], inputs["area"])
    strain = calculate_strain(inputs["original_length"], inputs["change_in_length"])
    factor_of_safety = calculate_factor_of_safety(properties["yield_strength"], stress)
    youngs_modulus = (
        calculate_youngs_modulus(stress, strain) if strain > 0 else properties["youngs_modulus"]
    )
    return {
        "stress": stress,
        "strain": strain,
        "youngs_modulus": youngs_modulus,
        "factor_of_safety": factor_of_safety,
        "yield_strength": properties["yield_strength"],
    }


def run_calculation_round(database):
    """Run one full calculation: selection, input, computation, and display."""
    material_name, properties = select_material_choice(database)
    display_selected_material(material_name, properties)

    inputs = collect_calculation_inputs()
    results = compute_results(inputs, properties)
    record = create_calculation_record(material_name, inputs, results)

    display_calculation_results(record)
    display_safety_analysis(results["stress"], properties["yield_strength"], results["factor_of_safety"])
    return record


def main():
    """Main function for the stress and strain calculator."""
    database = get_materials_database()
    calculations_history = []
    unique_materials = set()

    while True:
        print("=== Stress and Strain Calculator ===\n")
        record = run_calculation_round(database)
        add_to_history(calculations_history, record)
        unique_materials.add(record["material"])

        repeat = input("Do you want to run another calculation? (y/n): ").strip().lower()
        if repeat != "y":
            print("Exiting calculator.")
            break
        print()

    display_session_summary(calculations_history, unique_materials)


if __name__ == "__main__":
    main()