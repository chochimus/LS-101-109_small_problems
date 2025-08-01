def get_measurement():
    while True:
        try:
            return float(input())
        except ValueError:
            print("Invalid number, try again.")

def convert_to_feet(meters):
    return meters * 10.7639

def get_square(length, width):
    return length * width

print("Please enter the length in meters.")
length_meters = get_measurement()

print("Please enter the width in meters.")
width_meters = get_measurement()

square_meters = get_square(length_meters, width_meters)
square_feet = convert_to_feet(square_meters)

print(f'Your room is {square_meters} sq. m or {square_feet} sq. ft')