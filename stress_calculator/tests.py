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