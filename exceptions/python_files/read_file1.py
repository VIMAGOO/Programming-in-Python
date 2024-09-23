file = 'exceptions/python_files/data/bioinformatic1.csv'
# List to store the file lines
lines = []

try:
    with open(file, mode='r', encoding='utf-8') as file:
        # Skip the first row (headers)
        next(file)
        for line in file:
            try:
                # The separator for each data in the file is ','
                name, discovery, dates = line.strip().split(',')
                lines.append((name, discovery, dates))
            except ValueError as e:
                print(f"Error processing the line: {line.strip()}. Error: {e}")
                exit()  # Force program exit.

except FileNotFoundError:
    print(f"The file {file} was not found.")
except OSError as e:
    print(f"A system error occurred while trying to access the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"We successfully read the entire file!")
    print(lines[0])
finally:
    print("Thank you for trusting our software.")
