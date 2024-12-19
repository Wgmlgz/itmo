import locale
import re


def parse_simulation_report(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    # Регулярные выражения для извлечения данных
    generate_pattern = re.compile(r"\s+1\s+GENERATE\s+(\d+)")
    total1_pattern = re.compile(r"PRIBOR_1\s+3\s+TEST\s+(\d+)")
    terminate1_pattern = re.compile(r"REJECT_1\s+17\s+SAVEVALUE\s+(\d+)")
    queue1_pattern = re.compile(
        r"\s*BUF_1\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d.]+)\s+([\d.]+)"
    )
    dev_pattern = re.compile(
        r"TU_BUF\s*([\d.]+)\s+([\d.]+)"
    )
    storage1_pattern = re.compile(r"\s*UNIT_1\s+\d+\s+([\d.]+)")

    terminate2_pattern = re.compile(r"REJECT_2\s+19\s+SAVEVALUE\s+(\d+)")
    total2_pattern = re.compile(r"PRIBOR_2\s+11\s+TRANSFER\s+(\d+)")

    # queue2_pattern = re.compile(r'\s*BUF2\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d.]+)\s+([\d.]+)')
    storage2_pattern = re.compile(r"\s*UNIT_2\s+\d+\s+([\d.]+)")

    # Извлечение данных для прибора 1
    generate_match = generate_pattern.search(data)
    reject1_match = terminate1_pattern.search(data)
    total1_match = total1_pattern.search(data)
    queue1_match = queue1_pattern.search(data)
    storage1_match = storage1_pattern.search(data)
    dev_match = dev_pattern.search(data)

    # За подавку общего числа заявок
    total_requests = int(generate_match.group(1)) if generate_match else 0

    # Данные для прибора 1
    if reject1_match and queue1_match and storage1_match:
        rejected1_count = int(reject1_match.group(1))
        total1_count = int(total1_match.group(1))
        max_queue1 = float(queue1_match.group(1))
        ave_queue_length1 = float(queue1_match.group(5))
        ave_wait_time1 = float(queue1_match.group(6))
        util_rate1 = float(storage1_match.group(1))
        util_rate1 = float(storage1_match.group(1))
        dev = float(dev_match.group(2))
    else:
        rejected1_count = 0
        max_queue1, ave_queue_length1, ave_wait_time1, util_rate1 = (0.0, 0.0, 0.0, 0.0)

    # Данные для прибора 2
    reject2_match = terminate2_pattern.search(data)
    total2_match = total2_pattern.search(data)
    # queue2_match = queue2_pattern.search(data)
    storage2_match = storage2_pattern.search(data)

    if reject2_match and storage2_match:
        rejected2_count = int(reject2_match.group(1))
        # total2_count = int(total2_match.group(1))
        # max_queue2 = 0
        # ave_queue_length2 = 0
        # ave_wait_time2 = 0
        util_rate2 = float(storage2_match.group(1))
    else:
        rejected2_count = 0
        max_queue2, ave_queue_length2, ave_wait_time2, util_rate2 = (0.0, 0.0, 0.0, 0.0)

    # Рассчитываем данные на уровне всей системы
    total_rejected_count = rejected1_count + rejected2_count
    overall_rejection_probability = (
        total_rejected_count / total_requests if total_requests > 0 else 0.0
    )

    # devices_data = {
    #     "прибор 1": {
    #         "заявок потерянных": rejected1_count,
    #         "Длина очереди": max_queue1,
    #         "Средняя длина очереди": ave_queue_length1,
    #         "Среднее время в очереди": ave_wait_time1,
    #         "Использование": util_rate1,
    #         "Вероятность потери": (
    #             rejected1_count / total1_count if total_requests > 0 else 0.0
    #         ),
    #     },
    #     "прибор 2": {
    #         "заявок потерянных": rejected2_count,
    #         "Длина очереди": max_queue2,
    #         "Средняя длина очереди": ave_queue_length2,
    #         "Среднее время в очереди": ave_wait_time2,
    #         "Использование": util_rate2,
    #         "Вероятность потери": (
    #             rejected2_count / total2_count if total_requests > 0 else 0.0
    #         ),
    #     },
    #     "система": {
    #         "Загрузка": (util_rate1 + util_rate2) / 2,
    #         "Длина очереди": (ave_queue_length1 + ave_queue_length2),
    #         "Вероятность потери": (
    #             (rejected1_count / total1_count if total_requests > 0 else 0.0)
    #             + rejected2_count / total2_count
    #             if total_requests > 0
    #             else 0.0
    #         ),
    #         "Время ожидания": (ave_wait_time1 + ave_wait_time2) / 2,
    #         "Время пребывания": (),
    #     },
    # }

    locale.setlocale(locale.LC_NUMERIC, "en_DK.UTF-8")
    print(
        str(total_requests)
        + "; "
        + str(rejected1_count + rejected2_count)
        + "; "
        + "; "
        + "; "
        + str(ave_queue_length1).replace('.', ',')
        + "; "
        + f"{(util_rate1 + util_rate2) / 2:,}".replace('.', ',')
        + "; "
        + f"{ave_wait_time1:,}".replace('.', ',')
        + "; "
        + "; "
        + f"{dev:,}".replace('.', ',')
    )
    # return devices_data


# Применение
file_path = "sim.txt"
devices_data = parse_simulation_report(file_path)

# Вывод данных
# for device, data in devices_data.items():
# print(f"Характеристики для {device}:")
# for key, value in data.items():
#     print(f"  {key}: {value}")
# print()
