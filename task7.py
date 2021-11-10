import time
import itertools
from concurrent.futures import ProcessPoolExecutor


data = (f'{q}{w}{e}{r}{t}{y}{u}{i}{o}{p}{a}{s}'
        for q in range(5)
        for w in range(5)
        for e in range(5)
        for r in range(5)
        for t in range(5)
        for y in range(5)
        for u in range(5)
        for i in range(5)
        for o in range(5)
        for p in range(5)
        for a in range(5)
        for s in range(5)
        )


def get_happy_tickets(tickets):
    tickets_list = []

    for ticket in tickets:
        ticket_first_part = ticket[:6]
        ticket_second_part = ticket[6:]

        if (sum([int(num) for num in ticket_first_part]) == sum([int(num) for num in ticket_second_part])):
            tickets_list.append(ticket)

    return tickets_list


if (__name__ == '__main__'):
    CHUNK_COUNT = 6
    start_time = time.time()
    with ProcessPoolExecutor() as executor:

        tickets_list = list(data)
        chunk_size = len(tickets_list) / CHUNK_COUNT

        chunks = [tickets_list[int(i * chunk_size): int((i + 1) * chunk_size)]
                  for i in range(CHUNK_COUNT)]

        result_chunks = executor.map(get_happy_tickets, chunks)

        result = itertools.chain(*result_chunks)
        print(len(list(result)))
        print("--- %s seconds ---" % (time.time() - start_time))
