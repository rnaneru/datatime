from datetime import datetime
date_formats = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y"
}
def convert_date(date_string):
    for format_name, date_format in date_formats.items():
        try:
            date_obj = datetime.strptime(date_string, date_format)
            print(f"{format_name}: {date_obj}")
            return
        except ValueError:
            continue
    print("Неверный формат даты:", date_string)
while True:
    user_input = input("Введите дату (или 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        break
    convert_date(user_input)