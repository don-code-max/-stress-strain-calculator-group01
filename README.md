```
STRESS AND STRAIN ANALYSIS SYSTEM
Group Members
Member	Primary Responsibility
Don Derek Magpantay	    Task 1 – Basic Calculations
Daniel Nico Del Mundo	Task 2 – Control Structures
Robert Gabriel Roldan	Task 3 – Data Structures
Luis Cruzado	        Task 4 – Functions
Carlos Lopez	        Task 5 – OOP

Task 6 – Modular Integration was completed collaboratively by all members.

PROJECT DESCRIPTION
This program is a Python-based Stress and Strain Analysis System that helps engineers calculate and evaluate the mechanical stress and strain of materials under an applied load. It started as a simple calculator and evolved, step by step, into a modular, object-oriented application with a material database, session tracking, and file export capabilities.
Program Features
•	Calculates stress (σ = F/A) and strain (ε = ΔL/L₀) from user-provided force, area, and length measurements.
•	Includes a predefined materials database (Steel, Aluminum, Titanium) with yield strength and Young's modulus, plus support for entering a custom material.
•	Calculates factor of safety and flags whether a material is SAFE, in CAUTION, or expected to fail (WARNING) under the given load.
•	Implements an object-oriented material hierarchy (Material, Metal, Plastic, Composite) and a TestCollection class for analyzing multiple tests.
•	Saves and loads test results to/from JSON.
•	Exports test results to CSV.
•	Timestamps each test using datetime.

INSTALLATION/REQUIREMENTS
•	Python 3.9 or later.
•	No external packages required, the program uses only the Python standard library.

HOW TO RUN THE PROGRAM
Python -m stress_calculator.main

REPOSITORY STRUCTURE
•	material.py — Contains the Material class hierarchy (Material, Metal, Plastic, Composite).
•	properties.py — Contains the MaterialProperties dataclass and shared unit constants.
•	tests.py — Contains the StressStrainTest and TestAnalyzer classes used to track and analyze tests.
•	utils.py — Contains calculation, validation, and display functions, plus the JSON/CSV save-load-export utilities.
•	database.py — Contains the predefined materials database and functions to access it.
•	main.py — The main entry point; imports and coordinates all other modules through a menu-driven interface.

```
