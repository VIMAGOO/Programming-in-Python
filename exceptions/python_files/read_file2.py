from pathlib import Path

# Get all CSV files from the current directory
files = [Path('exceptions/python_files/data/bioinformatic1.csv'), Path('exceptions/python_files/data/bioinformatic2.csv')]
# Alternative:
#files = list(Path('.').glob('*.csv'))

# List to accumulate the data
lines = []

for file in files:
    try:
        with file.open(mode='r', encoding='utf-8') as file:
            # Skip the first row (headers)
            next(file)
            for line in file:
                try:
                    name, discovery, dates = line.strip().split(',')
                    lines.append((name, discovery, dates))
                except ValueError as e:
                    print(f"Error processing the line: {line.strip()}. Error: {e}")
    except FileNotFoundError:
        print(f"The file {file} was not found.")
    except OSError as e:
        print(f"An error occurred while trying to access the file: {e}")
    # This exception catches any other errors that may arise (good practice for debugging)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print(lines)
