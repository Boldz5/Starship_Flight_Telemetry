import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, signal


df=pd.read_csv("IFT5_EDITED_1_ship_telemetry.csv")




plt.plot(df["TIME[S]"],df["SPEED"])
plt.grid(True)