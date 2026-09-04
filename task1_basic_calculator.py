def main():
    """Main function for the stress and strain calculator."""

    while True:
        print("=== Stress and Strain Calculator ===")
        print()

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

