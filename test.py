import numpy as np
import pandas as pd

from data_processing import get_data_ready, get_ground_truths

a,b = get_data_ready(True)
print(get_ground_truths(b,0))

print('test')