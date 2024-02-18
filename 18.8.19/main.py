def calculate_ticket_price():
    num_tickets = int(input("Сколько билетов вы хотите приобрести? "))
    total_price = 0

    for _ in range(num_tickets):
        age = int(input("Введите возраст посетителя: "))
        if age < 18:
            ticket_price = 0
        elif 18 <= age < 25:
            ticket_price = 990
        else:
            ticket_price = 1390

        total_price += ticket_price

    if num_tickets > 3:
        total_price *= 0.9

    return total_price

total = calculate_ticket_price()
print(f"Сумма к оплате: {total} руб.")