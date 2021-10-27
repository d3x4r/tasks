from threading import Thread


def get_happy_tickets(tickets_list):
    result = []

    def get_sum(ticket_number, result_array):
        converted_values = [int(num) for num in ticket_number]
        result_array.append(sum(converted_values))

    for ticket in tickets_list:
        sum_result = []
        first_part = ticket[:6]
        second_part = ticket[6:]
        th1 = Thread(target=get_sum, args=(first_part, sum_result))
        th2 = Thread(target=get_sum, args=(second_part, sum_result))
        th1.start()
        th2.start()
        th1.join()
        th2.join()
        if (sum_result[0] == sum_result[1]):
            result.append(ticket)

    return result
