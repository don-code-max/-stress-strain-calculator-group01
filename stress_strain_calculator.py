from dataclasses import dataclass

UNITS = ("N", "m²", "m", "Pa")

MATERIALS_DATABASE = {
    "Steel": {"yield_strength": 250e6, "youngs_modulus": 200e9},
    "Aluminum": {"yield_strength": 95e6, "youngs_modulus": 69e9},
    "Titanium": {"yield_strength": 880e6, "youngs_modulus": 114e9},
}

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
        
class StressStrainTest:
    """Represents a single stress-strain test."""

    def __init__(
        self,
        material,
        force,
        area,
        original_length,
        change_in_length
    ):
        if force <= 0:
            raise ValueError("Force must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if original_length <= 0:
            raise ValueError("Original length must be positive")
        if change_in_length < 0:
            raise ValueError("Change in length cannot be negative")

        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

    @property
    def stress(self):
        return self._force / self._area

    @property
    def strain(self):
        return self._change_in_length / self._original_length

    @property
    def youngs_modulus(self):
        if self.strain == 0:
            return self.material.properties.youngs_modulus
        return self.stress / self.strain

    @property
    def factor_of_safety(self):
        return self.material.properties.yield_strength / self.stress

    def will_fail(self):
        return not self.material.can_withstand_stress(self.stress)

    def safety_status(self):
        if self.will_fail():
            return "WARNING - Material failure expected!"
        elif self.factor_of_safety < 1.25:
            return "CAUTION"
        else:
            return "SAFE"

    def __str__(self):
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress / 1e6:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Factor of Safety={self.factor_of_safety:.2f}"
        )
    
class TestAnalyzer:
    """Stores and analyzes multiple stress-strain tests."""

    def __init__(self):
        self.tests = []

    def add_test(self, test):
        if not isinstance(test, StressStrainTest):
            raise TypeError("Only StressStrainTest objects can be added")
        self.tests.append(test)

    def highest_stress_test(self):
        if not self.tests:
            return None
        return max(self.tests, key=lambda test: test.stress)

    def average_strain(self):
        if not self.tests:
            return 0
        return sum(test.strain for test in self.tests) / len(self.tests)

    def safest_test(self):
        if not self.tests:
            return None
        return max(self.tests, key=lambda test: test.factor_of_safety)

    def failed_tests(self):
        return [test for test in self.tests if test.will_fail()]

    def display_summary(self):
        print("\n=== OOP TEST ANALYSIS ===")

        if not self.tests:
            print("No tests available.")
            return

        print(f"Total tests: {len(self.tests)}")

        highest = self.highest_stress_test()
        safest = self.safest_test()

        print(
            f"Highest Stress: {highest.stress / 1e6:.2f} MPa "
            f"({highest.material.name})"
        )

        print(f"Average Strain: {self.average_strain():.6f}")

        print(
            f"Safest Material: {safest.material.name} "
            f"(FOS: {safest.factor_of_safety:.2f})"
        )

        print(f"Failed Tests: {len(self.failed_tests())}")

        print("\n--- Test Details ---")

        for i, test in enumerate(self.tests, 1):
            print(f"Test {i}: {test}")
            print(f"Status: {test.safety_status()}")

def run_oop_demo():
    steel_properties = MaterialProperties(
        density=7850,
        yield_strength=250e6,
        youngs_modulus=200e9
    )

    aluminum_properties = MaterialProperties(
        density=2700,
        yield_strength=95e6,
        youngs_modulus=69e9
    )

    titanium_properties = MaterialProperties(
        density=4500,
        yield_strength=880e6,
        youngs_modulus=114e9
    )

    steel = Metal("Steel", steel_properties, is_ferrous=True)
    aluminum = Metal("Aluminum", aluminum_properties, is_ferrous=False)
    titanium = Metal("Titanium", titanium_properties, is_ferrous=False)

    test1 = StressStrainTest(
        steel, 5000, 0.001, 2, 0.001
    )

    test2 = StressStrainTest(
        aluminum, 100000, 0.001, 1, 0.002
    )

    test3 = StressStrainTest(
        titanium, 900000, 0.001, 2, 0.005
    )

    analyzer = TestAnalyzer()
    analyzer.add_test(test1)
    analyzer.add_test(test2)
    analyzer.add_test(test3)

    analyzer.display_summary()

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