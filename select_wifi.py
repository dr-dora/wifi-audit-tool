#!/usr/bin/env python3

import csv
import sys
import re

if len(sys.argv) < 2:
    print("Использование: python3 select_wifi.py scan-01.csv", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

mac_regex = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")

networks = []

try:
    with open(filename, newline="", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)

        headers = None

        for row in reader:
            if not row:
                continue

            first_cell = row[0].strip()

            # Когда начинается секция клиентов — прекращаем читать точки доступа
            if first_cell == "Station MAC":
                break

            # Заголовок таблицы сетей
            if first_cell == "BSSID":
                headers = [h.strip() for h in row]
                continue

            if headers is None:
                continue

            data = {}

            for i, header in enumerate(headers):
                if i < len(row):
                    data[header] = row[i].strip()
                else:
                    data[header] = ""

            bssid = data.get("BSSID", "")
            channel = data.get("channel", "")
            essid = data.get("ESSID", "")
            power = data.get("Power", "")
            privacy = data.get("Privacy", "")

            # Проверка MAC-адреса
            if not mac_regex.match(bssid):
                continue

            # Проверка канала
            if not channel.isdigit():
                continue

            if essid == "":
                essid = "<hidden>"

            networks.append({
                "bssid": bssid,
                "channel": channel,
                "essid": essid,
                "power": power,
                "privacy": privacy
            })

except FileNotFoundError:
    print(f"Файл не найден: {filename}", file=sys.stderr)
    sys.exit(1)

except PermissionError:
    print(f"Нет прав на чтение файла: {filename}", file=sys.stderr)
    sys.exit(1)

if not networks:
    print("Сети не найдены в CSV-файле.", file=sys.stderr)
    sys.exit(1)

print("\nНайденные Wi-Fi сети:\n", file=sys.stderr)

for i, net in enumerate(networks, start=1):
    print(
        f"{i}. {net['essid']} | CH: {net['channel']} | PWR: {net['power']} | {net['privacy']} | {net['bssid']}",
        file=sys.stderr
    )

print("", file=sys.stderr)

while True:
    print("Выбери номер сети: ", end="", file=sys.stderr)

    try:
        choice = input().strip()
    except KeyboardInterrupt:
        print("\nОтменено пользователем.", file=sys.stderr)
        sys.exit(1)

    if not choice.isdigit():
        print("Введи число.", file=sys.stderr)
        continue

    choice = int(choice)

    if 1 <= choice <= len(networks):
        selected = networks[choice - 1]

        # stdout только для Bash
        # Формат: BSSID<TAB>CHANNEL<TAB>ESSID
        print(
            f"{selected['bssid']}\t{selected['channel']}\t{selected['essid']}"
        )

        sys.exit(0)
    else:
        print("Такого номера нет.", file=sys.stderr)
