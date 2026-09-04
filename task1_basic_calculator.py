def main():
    """Main function for the stress and strain calculator."""

    while True:
        print("=== Stress and Strain Calculator ===")
        print()

        print("Select Material:")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom")

        while True:
            choice = input("Enter choice (1-4): ").strip()
            if choice == "1":
                material_name = "Steel"
                yield_strength = 250e6
                youngs_modulus = 200e9
                break
            elif choice == "2":
                material_name = "Aluminum"
                yield_strength = 95e6
                youngs_modulus = 69e9
                break
            elif choice == "3":
                material_name = "Titanium"
                yield_strength = 880e6
                youngs_modulus = 114e9
                break
            elif choice == "4":
                material_name = "Custom"
                while True:
                    try:
                        yield_strength = float(input("Enter yield strength (MPa): ")) * 1e6
                        if yield_strength > 0:
                            break
                        print("Yield strength must be positive!")
                    except ValueError:
                        print("Please enter a valid number!")
                while True:
                    try:
                        youngs_modulus = float(input("Enter Young's modulus (GPa): ")) * 1e9
                        if youngs_modulus > 0:
                            break
                        print("Young's modulus must be positive!")
                    except ValueError:
                        print("Please enter a valid number!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")

        print(f"\nSelected Material: {material_name}")
        print(f"Yield Strength    : {yield_strength / 1e6:.2f} MPa")
        print(f"Young's Modulus   : {youngs_modulus / 1e9:.2f} GPa\n")

        while True:
            try:
                force = float(input("Enter the applied force (N): "))
                if force > 0:
                    break
                print("Force must be positive!")
            except ValueError:
                print("Please enter a valid number!")

        while True:
            try:
                area = float(input("Enter the cross-sectional area (m^2): "))
                if area > 0:
                    break
                print("Area must be positive and non-zero!")
            except ValueError:
                print("Please enter a valid number!")

        while True:
            try:
                original_length = float(input("Enter the original length (m): "))
                if original_length > 0:
                    break
                print("Original length must be positive and non-zero!")
            except ValueError:
                print("Please enter a valid number!")

        while True:
            try:
                change_in_length = float(input("Enter the change in length (m): "))
                if change_in_length >= 0:
                    break
                print("Change in length cannot be negative!")
            except ValueError:
                print("Please enter a valid number!")

    force = float(input("Enter the applied force (N): "))
    area = float(input("Enter the cross-sectional area (m^2): "))
    original_length = float(input("Enter the original length (m): "))
    change_in_length = float(input("Enter the change in length (m): "))

    stress = force / area
    strain = change_in_length / original_length

    print()
    print("=== RESULTS ===")
    print(f"Applied Force        : {force:.2f} N")
    print(f"Cross-Sectional Area : {area:.6f} m^2")
    print(f"Original Length      : {original_length:.4f} m")
    print(f"Change in Length     : {change_in_length:.4f} m")
    print()
    print(f"Stress : {stress:.2f} Pa")
    print(f"Strain : {strain:.6f}")
    print()
    print("=== Analysis Complete ===")
    
if __name__ == "__main__":
    main()

