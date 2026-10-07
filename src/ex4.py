from pathlib import Path
import pandas as pd 
import os

import sys

sys.stdout.reconfigure(encoding='utf-8')
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "INvideos.csv"

vids = pd.read_csv(DATA_PATH)

os.system('cls')

# Task 4.1 (Single Group Aggregation): Group the data by category_id and find the maximum number of views in each category.
task4_1 = vids.groupby('category_id').views.max()
print(task4_1)

# Task 4.2 (Multi-metric Aggregation): Group by channel_title and compute count, min, max, and mean of views simultaneously in a single command using .agg()
task4_2 = vids.groupby('channel_title').views.agg([len, min, max])
print(task4_2)

# Task 4.3 (Multi-column Grouping): Group simultaneously by category_id and channel_title, then get the total number of trending entries for each pair.
task4_3 = vids.groupby(['category_id', 'channel_title']).size()
print(task4_3)

# Task 4.4 (Group and Extract): Group by channel_title and extract the very first row encountered for each channel.
task4_4 = vids.groupby('channel_title').first()
print(task4_4)

# Task 5.1 (Single Column Sort): Sort the entire dataset by views in descending order (highest viewed video first)
task5_1 = vids.sort_values(by='views', ascending=False)
print(task5_1)

# Task 5.2 (Multi-column Mixed Sort): Sort the dataset by views descending, and for videos with equal views, sort by likes ascending.
task5_2 = vids.sort_values(by=['views', 'likes'], ascending=[False, True])
print(task5_2)

# Task 5.3 (Index Sorting): Take your grouped result from Task 4.3 (or any aggregated output) and sort it back by its index labels using .sort_index().
task5_3 = task4_3.sort_index()
print(task5_3)