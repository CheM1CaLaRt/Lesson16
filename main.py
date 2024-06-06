import pandas as pd

# Создание DataFrame с данными
data = {
    'Ученик': ['Анна', 'Боб', 'Вася', 'Галя', 'Дима', 'Елена', 'Женя', 'Зина', 'Ира', 'Катя'],
    'Математика': [5, 4, 3, 2, 5, 4, 3, 2, 5, 4],
    'Физика': [4, 5, 3, 2, 5, 4, 3, 2, 5, 4],
    'Химия': [5, 4, 3, 2, 5, 4, 3, 2, 5, 4],
    'Литература': [4, 5, 3, 2, 5, 4, 3, 2, 5, 4],
    'История': [5, 4, 3, 2, 5, 4, 3, 2, 5, 4]
}
df = pd.DataFrame(data)

# Вывод первых нескольких строк DataFrame
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.drop('Ученик', axis=1).mean()
print(mean_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = df.drop('Ученик', axis=1).median()
print(median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f'Q1: {Q1_math}, Q3: {Q3_math}, IQR: {IQR_math}')

# Вычисление стандартного отклонения
std_dev = df.drop('Ученик', axis=1).std()
print(std_dev)