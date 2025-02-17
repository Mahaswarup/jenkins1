import sys

def length_converter():
    print("Length Converter Selected")

def weight_converter():
    print("Weight Converter Selected")

def temperature_converter():
    print("Temperature Converter Selected")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <option>")
        sys.exit(1)

    main_choice = sys.argv[1]  # Read argument from command-line

    if main_choice == '1':
        length_converter()
    elif main_choice == '2':
        weight_converter()
    elif main_choice == '3':
        temperature_converter()
    else:
        print("Invalid choice")
