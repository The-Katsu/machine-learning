import matplotlib.pyplot as plt
import pandas as pd
import squarify
import random
import csv
import math

# Load Data
df_raw = pd.read_csv('vgsales.csv')


##################################################
# Прибыльность регионов
#################################################
#
# na = df_raw['NA_Sales']
# na_avg = 0
# for x in na:
#     na_avg += x
# na_avg = na_avg/len(na)
#
# eu = df_raw['EU_Sales']
# eu_avg = 0
# for x in eu:
#     eu_avg += x
# eu_avg = eu_avg/len(eu)
#
# jp = df_raw['JP_Sales']
# jp_avg = 0
# for x in jp:
#     jp_avg += x
# jp_avg = jp_avg/len(jp)
#
# other = df_raw['Other_Sales']
# other_avg = 0
# for x in other:
#     other_avg += x
# other_avg = other_avg/len(other)
#
# g = df_raw['Global_Sales']
# g_avg = 0
# for x in g:
#     g_avg += x
# g_avg = g_avg/len(g)
#
# list = [na_avg, eu_avg, jp_avg, other_avg]
# label = ["North America" "\n (" + str(round(na_avg, 3)) + ")",
#          "Europe" "\n (" + str(round(eu_avg, 3)) + ")",
#          "Japan" "\n (" + str(round(jp_avg, 3)) + ")",
#          "Others" "\n (" + str(round(other_avg, 3)) + ")"]
# color=['red','blue','green','grey']
#
# squarify.plot(sizes=list, label=label, color=color, alpha=0.6 )
# plt.title("Регионы - лидеры продаж" + "\n (В среднем продано копий)")
# plt.axis('off')
# plt.show()

# ###############################################
# # Games by Platform
# ##############################################
#
# # Prepare Data
# df = df_raw.groupby('Platform').size().reset_index(name='counts')
# n = df['Platform'].unique().__len__()+1
# all_colors = list(plt.cm.colors.cnames.keys())
# random.seed(100)
# c = random.choices(all_colors, k=n)
#
# # Plot Bars
# plt.figure(figsize=(16,10), dpi= 80)
# plt.bar(df['Platform'], df['counts'], color=c, width=.5)
# for i, val in enumerate(df['counts'].values):
#     plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})
#
# # Decoration
# plt.gca().set_xticklabels(df['Platform'], rotation=60, horizontalalignment= 'right')
# plt.title("Number of Games by Platform", fontsize=22)
# plt.ylabel('# Games')
# plt.ylim(0, 2500)
# plt.show()

# ##################################################
# # Genres
# ##################################################
#
# # Prepare Data
# df = df_raw.groupby('Genre').size().reset_index(name='counts')
#
# # Draw Plot
# fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)
#
# data = df['counts']
# categories = df['Genre']
#
# def func(pct, allvals):
#     absolute = int(pct/100.*np.sum(allvals))
#     return "{:.1f}% ({:d} )".format(pct, absolute)
#
# wedges, texts, autotexts = ax.pie(data,
#                                   autopct=lambda pct: func(pct, data),
#                                   textprops=dict(color="w"),
#                                   colors=plt.cm.tab20.colors,
#                                  startangle=140,
#                                  explode=None)
#
# # Decoration
# ax.legend(wedges, categories, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
# plt.setp(autotexts, size=10, weight=700)
# ax.set_title("Games genres: Pie Chart")
# plt.show()