# Speed Tracker 

This project generates simulated car data, validates number plates, and identifies speeding violations based on time and distance between two cameras. The project includes the following main components:

1. **TestDataGenerator**: Generates random car data and stores it in a CSV file.
2. **ValidNumberPlate**: Validates number plates against a specific format and updates the CSV file with validation results.
3. **Speeding**: Calculates the speed of cars based on time taken between two points and identifies those exceeding the speed limit.

## Installation

1. Clone the repository or download the source code.
2. Ensure Python 3.x is installed on your system.

## Usage

1. **Generate Test Data**:
   - Modify the `num_rows`, `field_names`, and `folder_name` parameters as needed.
   - Run the script to generate a CSV file with random car data.

2. **Validate Number Plates**:
   - The `ValidNumberPlate` class checks if the generated number plates follow the format `XX00 000`. Invalid plates are marked in the CSV file.

3. **Check for Speeding Violations**:
   - The `Speeding` class calculates the speed of each vehicle based on the time difference between two camera points.
   - Customise the `speed_limit` and `distance_miles` parameters to suit your use case.
   - Speed violators are printed to the console with their average speed.

## Output

- A CSV file named `data.csv` in the specified `folder_name` containing generated car data.
- The CSV file will be updated with a `Valid` column indicating whether the number plate is valid.
- Speed violators will be listed in the console output.

## Customisation

Feel free to modify the following parameters in the `main()` function:
- `num_rows`: Number of data rows to generate.
- `speed_limit`: Speed limit in miles per hour.
- `distance_miles`: Distance between camera points in miles.
- `start_hour` and `end_hour`: Time range for generating random times.

## Dependencies

This project uses Python's standard libraries:
- `csv`
- `random`
- `datetime`
- `re`
- `os`

## Contact

For any issues or improvements, feel free to reach out or open an issue in the repository.

