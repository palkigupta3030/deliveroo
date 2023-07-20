#!/usr/bin/env python3
import sys

def parse_field(field_str, max_val):
    if field_str == '*':
        return list(range(max_val + 1))
    values = []
    for part in field_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            values.extend(range(start, end + 1))
        else:
            values.append(int(part))
    return sorted(list(set(values)))

def parse_cron(cron_str):
    fields = cron_str.strip().split(' ')
    if len(fields) != 6:
        raise ValueError("Invalid cron string: 6 fields required.")
    
    minutes = parse_field(fields[0], 59)
    hours = parse_field(fields[1], 23)
    day_of_month = parse_field(fields[2], 31)
    months = parse_field(fields[3], 12)
    day_of_week = parse_field(fields[4], 7)
    command = fields[5]

    return minutes, hours, day_of_month, months, day_of_week, command

def format_output(minutes, hours, day_of_month, months, day_of_week, command):
    output = ""
    field_names = ["minute", "hour", "day of month", "month", "day of week"]
    fields = [minutes, hours, day_of_month, months, day_of_week]

    for name, field in zip(field_names, fields):
        output += f"{name:14s} {' '.join(map(str, field))}\n"

    output += f"{'command':14s} {command}\n"
    return output

def main():
    if len(sys.argv) != 2:
        print("Usage: python your_program.py <cron_string>")
        return

    try:
        cron_str = sys.argv[1]
        minutes, hours, day_of_month, months, day_of_week, command = parse_cron(cron_str)
        output = format_output(minutes, hours, day_of_month, months, day_of_week, command)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
