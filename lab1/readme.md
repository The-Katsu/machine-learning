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
![Картинка](https://github.com/The-Katsu/machine-learning/blob/main/lab1/genres.jpg?raw=true)  
### 2. Популярность игровой платформы
```python
# Импорт данных
df_raw = pd.read_csv('vgsales.csv')

# Подготовка данных
df = df_raw.groupby('Platform').size().reset_index(name='counts')
n = df['Platform'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

# Отрисовка графика
plt.figure(figsize=(16,10), dpi= 80)
plt.bar(df['Platform'], df['counts'], color=c, width=.5)
for i, val in enumerate(df['counts'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

# Корректировка графика
plt.gca().set_xticklabels(df['Platform'], rotation=60, horizontalalignment= 'right')
plt.title("Number of Games by Platform", fontsize=22)
plt.ylabel('# Games')
plt.ylim(0, 2500)
plt.show()
```
![Картинка](https://github.com/The-Katsu/machine-learning/blob/main/lab1/plafrotms.jpg?raw=true)  
### 3. Регионы с наибольшим количеством продаж
```python
# Импорт данных
df_raw = pd.read_csv('vgsales.csv')

# Получим средние количество проданных копий по
# Северной Америке
na = df_raw['NA_Sales']
na_avg = 0
for x in na:
    na_avg += x
na_avg = na_avg/len(na)
# Европе
eu = df_raw['EU_Sales']
eu_avg = 0
for x in eu:
    eu_avg += x
eu_avg = eu_avg/len(eu)
# Японии
jp = df_raw['JP_Sales']
jp_avg = 0
for x in jp:
    jp_avg += x
jp_avg = jp_avg/len(jp)
# Других стран
other = df_raw['Other_Sales']
other_avg = 0
for x in other:
    other_avg += x
other_avg = other_avg/len(other)

# Создадим контейнеры данных
list = [na_avg, eu_avg, jp_avg, other_avg]
label = ["North America" "\n (" + str(round(na_avg, 3)) + ")",
         "Europe" "\n (" + str(round(eu_avg, 3)) + ")",
         "Japan" "\n (" + str(round(jp_avg, 3)) + ")",
         "Others" "\n (" + str(round(other_avg, 3)) + ")"]
color=['red','blue','green','grey']

# Отрисовка графика
squarify.plot(sizes=list, label=label, color=color, alpha=0.6 )
plt.title("Регионы - лидеры продаж" + "\n (В среднем продано копий)")
plt.axis('off')
plt.show()
```
*Количество копий в миллионах!  

![Картинка](https://github.com/The-Katsu/machine-learning/blob/main/lab1/regions.jpg?raw=true)

---
## Выводы
В результате данной работы был проанализирован датасет - [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales).  
Исходя из полученных результатов можно сделать выводы, что Action является самым популярным издаваемым жанром, PS2 и DS до сих пор держат первенство у издателей, т.к. для них было выпущено больше всего игр, а самым прибыльным регионом является Северная Америка.