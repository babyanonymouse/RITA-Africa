"""Task: Write a Python program that:
Declares two variables (length and width)
Calculates the area of a rectangle
Prints the result.
Use comments to explain each step.
"""
print("<-- AREA OF A RECTANGLE -->")  # Display a header

# Prompt the user to enter the length and width of the rectangle
rect_length = int(input("Enter the length of the Rectangle(metres): "))  # Input length
rect_width = int(input("Enter the width of the Rectangle(metres): "))  # Input width


# Function to calculate the area of a rectangle
def rectangle_area():
    # Area is calculated by multiplying rect_length and rect_width
    return rect_length * rect_width  # Return the calculated area


# Calculate the area and print the result
area = rectangle_area()  # Call the function
print("The area of the rectangle is {} metres²".format(area))  # Format and display the result