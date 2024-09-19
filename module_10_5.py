import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


def main():
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.datetime.now()
    print("Линейный вызов:", (end_time - start_time))

    if __name__ == '__main__':
        start_time = datetime.datetime.now()
        with multiprocessing.Pool() as pool:
            pool.map(read_info, filenames)
        end_time = datetime.datetime.now()
        print("Многопроцессный вызов:", (end_time - start_time))


if __name__ == '__main__':
    main()

# Линейный вызов: 0:00:06.139587
# Многопроцессный вызов: 0:00:02.559634
