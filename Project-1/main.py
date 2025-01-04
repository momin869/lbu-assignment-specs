from logging import error

def process_race_data(filename):
    driver_names = []
    lap_times = []
    driver_laps = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if not lines:
            error("File is empty or could not be read")
            return

        print(lines[0].strip())  # Print the header

        for line in lines[1:]:
            driver = line[:3]
            lap_time = line[3:].strip()

            driver_names.append(driver)
            lap_times.append(lap_time)
            driver_laps.append((driver, lap_time))

        driver_laps.sort(key=lambda x: x[1])  # Sort by lap time

        print(driver_laps)
        print(f"THE FASTEST LAP TIME IN {filename} WAS:", driver_laps[0])

    except FileNotFoundError:
        error(f"File {filename} not found")
    except Exception as e:
        error(f"An error occurred: {e}")

def race_one():
    process_race_data("lap_times_1.txt")

def race_two():
    process_race_data("lap_times_2.txt")

def race_three():
    process_race_data("lap_times_3.txt")

# Run each race
race_one()
race_two()
race_three()
