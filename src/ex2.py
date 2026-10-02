import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# pyrefly: ignore [missing-import]
from learntools.core import binder; binder.bind(globals())
# pyrefly: ignore [missing-import]
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")