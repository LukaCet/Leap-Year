def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is INDEED a leap year.")
    else: 
        print(f"{year} is not a leap year...")

while True:
    year = int(input("Input a year: "))
    is_leap_year(year)
