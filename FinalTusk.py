import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.divan.ru/category/divany"

try:

    response = requests.get(url)
    response.raise_for_status()  # Проверка успешности запроса
    soup = BeautifulSoup(response.text, 'html.parser')

    prices = []
    for price_tag in soup.find_all('div', class_='some-class-for-price'):  # Замените на реальный класс
        price_text = price_tag.get_text().strip()
        price = int(price_text.replace(' ', '').replace('₽', ''))  # Очистка и преобразование текста в число
        prices.append(price)

    if not prices:
        print("Не удалось найти цены на диваны.")
    else:
        df = pd.DataFrame(prices, columns=['Price'])
        df.to_csv('divan_prices.csv', index=False)

        average_price = df['Price'].mean()
        print(f"Средняя цена на диваны: {average_price}₽")

        plt.hist(df['Price'], bins=30, edgecolor='black', alpha=0.7)
        plt.title('Гистограмма цен на диваны')
        plt.xlabel('Цена (₽)')
        plt.ylabel('Количество')
        plt.show()

except requests.RequestException as e:
    print(f"Ошибка при получении данных: {e}")