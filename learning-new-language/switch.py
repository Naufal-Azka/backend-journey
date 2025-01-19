def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"
        
print(day_of_week('aa'))


def is_weekend(day):
    match day:
        case 'Saturday' | 'Sunday':
            return True
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            return False
        case _:
            return "Invalid day"
        
print(is_weekend('a'))