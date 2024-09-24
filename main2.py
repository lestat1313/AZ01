import pandas as pd

# Указываем путь к файлу CSV
file_path = 'dz.csv'

# Загружаем CSV файл в DataFrame
df = pd.read_csv(file_path)

# Вычисляем среднюю зарплату по городам
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Преобразуем результат в словарь и выводим его
average_salary_dict = average_salary_by_city.to_dict()

print("Средняя зарплата по городам:")
for city, salary in average_salary_dict.items():
    print(f"{city}: {salary}")
