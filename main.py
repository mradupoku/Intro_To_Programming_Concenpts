def main():
    total_rain = 0.0
    total_wind = 0.0
    day_count = 0

    while True:
        # Reading input from console
        line = input().split()

        # Checking sentinel value
        if not line or float(line[0]) == -1.0:
            break

        # Rain and wind
        rain = float(line[0])
        wind = float(line[1])

        # Add totals
        total_rain += rain
        total_wind += wind
        day_count += 1

    # Only perform calculations if at least one day of data was entered
    if day_count > 0:
        avg_rain = total_rain / day_count
        avg_wind = total_wind / day_count

        # Weather Severity formula: (average rain * 10) + average wind
        weather_severity = (avg_rain * 10) + avg_wind

        # Format and display output
        print(f"The average rain is {avg_rain:.1f} inches")
        print(f"The average wind is {avg_wind:.1f} mph")
        print(f"The weather severity for these {day_count} readings is:  {weather_severity:.1f}")


if __name__ == "__main__":
    main()
