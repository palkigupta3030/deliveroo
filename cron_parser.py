#!/usr/bin/env python3

import sys

def parse_cron_expression(expression):
    cron_fields = expression.strip().split()
    if len(cron_fields) != 6:
        raise ValueError("Invalid cron expression: Must have 6 fields.")

    minute, hour, day_of_month, month, day_of_week, command = cron_fields

    expanded_fields = {
        'minute': expand_field(minute, 0, 59),
        'hour': expand_field(hour, 0, 23),
        'day of month': expand_field(day_of_month, 1, 31),
        'month': expand_field(month, 1, 12),
        'day of week': expand_field(day_of_week, 0, 6),
        'command': command
    }

    return expanded_fields

def expand_field(field, min_value, max_value):
    if field == '*':
        return list(range(min_value, max_value + 1))

    values = set()

    for part in field.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            values.update(range(start, end + 1))
        elif '/' in part:
            value, interval = map(int, part.split('/'))
            values.update(range(min_value, max_value + 1, interval))
        else:
            values.add(int(part))

    return sorted(value for value in values if min_value <= value <= max_value)

def format_output(expanded_fields):
    for field, values in expanded_fields.items():
        print(f"{field:<14}{' '.join(map(str, values))}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cron_parser.py 'cron_expression'")
        sys.exit(1)

    cron_expression = sys.argv[1]
    try:
        expanded_fields = parse_cron_expression(cron_expression)
        format_output(expanded_fields)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
