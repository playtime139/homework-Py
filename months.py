import calendar

# Get and display all month names
for month in calendar.month_name:
    if month:   # skip empty string at index 0
        print(month)
