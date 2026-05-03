import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, signal


df1=pd.read_csv("Booster_Telemetry.csv")
df2=pd.read_csv("Ship_Telemetry.csv")


fig,axs=plt.subplots(2,2,figsize=(20,12))
#---------------------------------------BOOSTER-----------------------------------------------
axs[0,0].plot(df1["TIME[S]"],df1["SPEED"],linewidth=1)
axs[0,0].set_xlabel("Time(s)")
axs[0,0].set_ylabel("Speed(km/h)")
axs[0,0].set_title("TIME vs SPEED(Booster)")
axs[0,0].grid(True,linewidth=.2)



axs[0,1].plot(df1["TIME[S]"],df1["altitude"],linewidth=1)
axs[0,1].set_xlabel("Time(s)")
axs[0,1].set_ylabel("Altitude(Km)")
axs[0,1].set_title("TIME vs ALTITUDE(Booster)")
axs[0,1].grid(True,linewidth=.2)


#---------------------------------------SHIP-----------------------------------------------

axs[1,0].plot(df2["TIME[S]"],df2["SPEED"],linewidth=1)
axs[1,0].set_xlabel("Time(s)")
axs[1,0].set_ylabel("Speed(km/h)")
axs[1,0].set_title("TIME vs SPEED(Ship)")
axs[1,0].grid(True,linewidth=.2)

axs[1,1].plot(df2["TIME[S]"],df2["altitude"],linewidth=1)
axs[1,1].set_xlabel("Time(s)")
axs[1,1].set_ylabel("Altitude(Km)")
axs[1,1].set_title("TIME vs ALTITUDE(Ship)")
axs[1,1].grid(True,linewidth=.2)
