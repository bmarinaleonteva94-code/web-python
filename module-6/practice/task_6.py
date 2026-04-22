logs = [
    ("ivan", "day", 8),
    ("ivan", "night", 4),
    ("olga", "day", 6),
    ("petr", "night", 2),
    ("anna", "day", 4),
    ("anna", "day", 3)
]

employee_shift = {}
shift_hours = {}
employee_hours = {}
for name, shift, hours in logs:
    if name not in employee_shift:
        employee_shift[name] = set()
    employee_shift[name].add(shift)

    if shift not in shift_hours:
        shift_hours[shift] = 0
    shift_hours[shift] += hours

    if name not in employee_hours:
        employee_hours[name] = 0
    employee_hours[name] += hours
multiple_shift = []
for employee in employee_shift:
    if len(employee_shift[employee]) == 2:
        multiple_shift.append(employee)

shifts_less  =[]
for shift in shift_hours:
    if shift_hours[shift] < 8:
        shifts_less.append(shift)

employees = []
for employee in employee_hours:
    if employee_hours[employee] >=12:
        employees.append(employee)


print(multiple_shift)
print(shifts_less)
print(employees)



# day_shift = []
# night_shift = []

# day_shift_lenght = []
# night_shift_lenght = []
# total_hours = {}
# for name, shift, hours in logs:
#     if shift == "day":
#         day_shift.append(name)
#         day_shift_lenght.append(hours)
#     else:
#         night_shift.append(name)
#         night_shift_lenght.append(hours)
#     if name not in total_hours:
#         total_hours[name] = 0
#     total_hours[name] += hours
    
# sum_day = sum(day_shift_lenght)
# sum_night = sum(night_shift_lenght)
 
# if sum_day < 8:
#     print("В дневную смену отработано меньше 8 часов")
# if sum_night < 8:
#     print("В ночную смену отработано меньше 8 часов.")

# over_12_hours = [name for name, total in total_hours.items() if total >= 12]

# day_set = set(day_shift)
# night_set = set(night_shift)
# day_night_shifts = list(day_set & night_set)

# print(f"Работал в разных сменах {day_night_shifts[0]}")
# print(over_12_hours)