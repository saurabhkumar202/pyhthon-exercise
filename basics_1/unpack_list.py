x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for a, b, c in x:
    print(f"{a}{b}{c}")

x = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for temp in x:
    print(f"{temp}")

for a, b, c in x:
    print(f"{a}{b}{c}")

week_day_dict = [{"MONDAY": "OFFICE", "TUESDAY": "WFH", "WEDNESDAY": "WFH", "THURSDAY": "WFH", "FRIDAY": "WFH"}]

for item in week_day_dict:
    print(f"{item}")
    for local_item in item.items():
        print(f"{local_item[0]} {local_item[1]}")


