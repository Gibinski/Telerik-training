def days_counter(years: list, days: int):
    days += 1
    if days == 7:
        print()
        print(len(years))
        print(years)

        years.clear()
        days = 0

    return [years, days]

    
year = 2020
years = []
days = 0

for j in range(100):    
    for i in range(4):    
        year += 1
        years.append(year)    
        years, days = days_counter(years, days)
    years, days = days_counter(years, days)

