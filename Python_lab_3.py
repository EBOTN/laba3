def calculate(value, percents, months):
    result = round((value * (percents / 1200 + (percents / 1200) / ((1 + percents / 1200) ** months - 1))), 2)
    returnedArray = []
    for x in range(int(months)):
        returnedArray.append(f"{x + 1}, {value}, {round((value * percents / 1200), 2)}, {round((result - value * percents / 1200), 2)}, {result}")
        value = round((value + value*percents/1200 -result), 2)
    return returnedArray

def main():
    print('Введите сумму кредита')
    # value = float(input())
    value = 1000
    print('Введите длительность периода(в месяцах)')
    # months = int(input())
    months = 12
    print('Введите процентную ставку')
    # percents = float(input())
    percents = 5
    calculate(value, percents, months)

if __name__ == '__main__':
    main()