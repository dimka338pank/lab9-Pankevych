try:
    n_str = input("Введіть n для визначення ознаки подільності:" )
    n = int(n_str)
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if i % j == 0:
                count+=1

        pluses = "+"*count
        print(f"{i} {pluses}")

except ValueError:
            print("Помилка: Будь ласка, вводьте лише цілі числа")