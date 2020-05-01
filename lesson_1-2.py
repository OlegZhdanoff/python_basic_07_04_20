time_sec = int(input('Введите время в секундах\n'))
hours = time_sec // 3600
minutes = (time_sec % 3600) // 60
seconds = (time_sec % 3600) % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
