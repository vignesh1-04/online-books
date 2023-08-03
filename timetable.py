def display_timetable(timetable):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    periods = ['1st', '2nd', '3rd', '4th', '5th']

    print("Timetable:")
    print("===========")

    # Print column headers (periods)
    print("\t", end="")
    for period in periods:
        print(period, end="\t")
    print()

    # Print rows (days) with the corresponding subjects
    for i, day in enumerate(days):
        print(day, end="\t")
        for j, period in enumerate(periods):
            subject = timetable[i][j]
            print(subject, end="\t")
        print()

if __name__ == "__main__":
    # Replace the subjects with your actual timetable data
    # Each inner list represents a day with subjects for each period
    timetable_data = [
        ['Math', 'English', 'Science', 'History', 'Break'],
        ['Physics', 'Chemistry', 'Math', 'Geography', 'Lunch'],
        ['Biology', 'English', 'Computer Science', 'Art', 'Break'],
        ['History', 'Math', 'Physics', 'Chemistry', 'Lunch'],
        ['Geography', 'Science', 'Biology', 'English', 'Break'],
    ]

    display_timetable(timetable_data)
