from typing import Text
import matplotlib as plt
import numpy as np
import random
import seaborn as sns
from seaborn.utils import axes_ticklabels_overlap 

rolls = [random.randrange(1,7) for i in range(6000000)]
values, frequences = np.unique(rolls, return_counts=True)

title = f'Rolling a six-sided die {len(rolls)} times!'
sns.set_style('whitegrid')

axes = sns.barplot(x=values, y=frequences, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequences) * 1.10)

for bar, frequency in zip(axes.patches, frequences):
    text_x = bar.get_x() + bar.get_width() /2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')