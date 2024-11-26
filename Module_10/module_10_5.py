import time
import multiprocessing

filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


# Линейный
# start_time = time.time()
# for file in filenames:
#     read_info(file)
# end_time = time.time()
# print(f'Время выполнения: {end_time - start_time}')

# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(len(filenames)) as p:
        start_time = time.time()
        p.map(read_info, filenames)
        end_time = time.time()
        print(f'Время выполнения: {end_time - start_time}')
