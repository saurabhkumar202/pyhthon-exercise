week_day = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY")
print(f"Week days are {week_day}")

for item in week_day:
    print(f"Way 1- Week days are {item}")

for index in range(len(week_day)):
    print(f"Way 2- Week days are {week_day[index]}")

initial_index = 0
while initial_index < len(week_day):
    print(f"Way 3- Week days are {week_day[initial_index]}")
    initial_index += 1

numbered_week_day = [(1, "MONDAY", "Office"), (2, "TUESDAY", "WFH"), (3, "WEDNESDAY", "WFH"), (4, "THURSDAY", "WFH"),
                     (5, "FRIDAY", "WFH")]

for index, day, work_location in numbered_week_day:
    print(f"{index} {day} {work_location}")

week_day_dict = {"MONDAY": "OFFICE", "TUESDAY": "WFH", "WEDNESDAY": "WFH", "THURSDAY": "WFH", "FRIDAY": "WFH"}

for item in week_day_dict.items():
    print(f"{item[0]} {item[1]}")

for item in week_day_dict.keys():
    print(f"{item}")

keys = week_day_dict.keys()
# print(f"{keys}")
