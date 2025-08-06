# triangle-angle-calculator

This Python script calculates the internal angles of a triangle using the Law of Cosines and Law of Sines based on user-input side lengths.

## How it works:
The user enters **three side lengths in descending order**, and the program:
1. Uses the Law of Cosines to compute the largest angle (opposite the largest side).
2. Applies the Law of Sines to find the middle angle.
3. Calculates the smallest angle by subtracting the sum of the first two from 180°.
4. Prints all three angles in degrees.

##  Concepts Demonstrated:
- Trigonometric formulas (Law of Cosines, Law of Sines)
- Input validation
- Degree/radian conversion with `math` module
- Basic error handling

## Example:
- Enter length for side A (biggest value): 5
- Enter length for side B: 4
- Enter length for side C (smallest value): 3

- Solved successfully!
- The angles are:
- 90.0
- 53.13010235415598
- 36.86989764584401

 ## Assumptions:
- Input must be in descending order
- Inputs must be valid positive side lengths of a triangle
