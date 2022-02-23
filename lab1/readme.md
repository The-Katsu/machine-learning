# Продажа видеоигр
---
## Состав команды
* Авилов Владмир ИВТ-363
* Беляк Никит ИВТ-363
* Мельникова Валерия ИВТ-363
---
## Датасет и тема работы
Темой работы был выбран "Анализ продаж видеоигр", в связи с постоянно растущим влиянием игровой индустрии на мир, по сводкам за 2021 год игровая индустрия занимает [6 место в списке самых прибыльных отраслей в мире](https://pnktv.news/ru/blogs/kakie_otrasli_stali_samymi_pribylnymi_v_epohu_pandemii_covid_19_issledovanie_1017812).
  
Выбраннй датасет - Video Game Sales  
Количество записей - 16,598  
[Ссылка на датасет](https://www.kaggle.com/gregorut/videogamesales)

---
## Основные статистическе характеристики  
* Rank - Нумерация в списке  
* Name - Название игры 
* Platform - Платформа, на которую выпущена игра (PC,PS4, и т.д.)  
* Year - Год релиза  
* Genre - Жанр игры  
* Publisher - Издатель  
* NA_Sales - Продажи в Северной Америке (в миллионах)  
* EU_Sales - Продажи в Европе (в миллионах)  
* JP_Sales - Продажи в Японии (в миллионах)  
* Other_Sales - Продажи в остальном мире (в * миллионах)  
* Global_Sales - Всего продано копий(в миллионах).
---
## Визуализация данных
### 1. Популярность жанров  
```python
# Импорт данных
df_raw = pd.read_csv('vgsales.csv')

# Отрисовка графика
fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)

data = df['counts']
categories = df['Genre']

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data,
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"),
                                  colors=plt.cm.tab20.colors,
                                 startangle=140,
                                 explode=None)

# Корректировка отрисовки
ax.legend(wedges, categories, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=10, weight=700)
ax.set_title("Games genres: Pie Chart")
plt.show()  
```
