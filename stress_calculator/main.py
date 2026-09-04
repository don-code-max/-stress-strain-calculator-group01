import csv
import json
from datetime import datetime
from pathlib import Path
from .database import get_materials_database
from .utils import add_to_history, run_calculation_round, display_session_summary

from .database import get_materials_database, get_material_properties
from .utils import (
    calculate_stress,
    calculate_strain,
    calculate_youngs_modulus,
    calculate_factor_of_safety,
    validate_force,
    validate_area,
    validate_original_length,
    validate_change_in_length,
    validate_yield_strength_input,
    validate_youngs_modulus_input,
)

def print_main_menu() -> None:
    print("\n=== Stress and Strain Calculator ===")
    print("1. Run a new calculation")
    print("2. View session summary")
    print("3. Save results to JSON")
    print("4. Load results from JSON")
    print("5. Export results to CSV")
    print("6. Generate simulated test data")
    print("7. Exit")

try:
    import ujson as json_engine
    JSON_BACKEND = "ujson (optimized)"
except ImportError:
    import json as json_engine
    JSON_BACKEND = "standard json"

def save_report(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json_engine.dump(data, f, indent=4)
    print(f"[✓] Export completed using {JSON_BACKEND} engine.")

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