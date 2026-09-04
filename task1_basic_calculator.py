def main():
    """Main function for the stress and strain calculator."""

    print("=== Stress and Strain Calculator ===")
    print()

    force = float(input("Enter the applied force (N): "))
    area = float(input("Enter the cross-sectional area (m^2): "))
    original_length = float(input("Enter the original length (m): "))
    change_in_length = float(input("Enter the change in length (m): "))

    stress = force / area
    strain = change_in_length / original_length

if __name__ == "__main__":
    main()

