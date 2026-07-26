Dictionary = {
    'Mahesh': 51,
    'veera': 75,
    'Charan': 49,
    'Eswar': 50,
    'Surendra': 99
}

highest = max(Dictionary.values())
Avg = sum(Dictionary.values()) / len(Dictionary)  # ← moved here

for key, value in Dictionary.items():
    if value > 50:
        print(f'{key} passed')
    elif value < 50:
        print(f'{key} Failed')
    else:
        print(f'{key} Got exactly 50')
    if value == highest:
        print(f'{key} got highest marks')

print(f'Average is {Avg}')