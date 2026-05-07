import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats, signal


def dynamic_pressure(v,h):
    
    var_density=1.225*math.exp(-h/8400)
    q=.5*var_density*(v**2)
    
    return q/1000


def rmse(y_true, y_pred):
       return np.sqrt(np.mean((y_true - y_pred) ** 2))

    
df1=pd.read_csv("Booster_Telemetry.csv")
df2=pd.read_csv("Ship_Telemetry.csv")

fig,axs1=plt.subplots(1,2,figsize=(27,10))
plt.style.use("dark_background")

#---------------------------------------BOOSTER-----------------------------------------------
axs1[0].plot(df1["TIME[S]"],df1["SPEED"]*.2778,linewidth=1)
axs1[0].set_xlabel("Time(s)")
axs1[0].set_ylabel("Speed(m/s)")
axs1[0].set_title("TIME vs SPEED(Booster)")
axs1[0].grid(True,linewidth=.2)

axs1[1].plot(df1["TIME[S]"],df1["altitude"]*1000,linewidth=1)
axs1[1].set_xlabel("Time(s)")
axs1[1].set_ylabel("Altitude(m)")
axs1[1].set_title("TIME vs ALTITUDE(Booster)")
axs1[1].grid(True,linewidth=.2)

#---------------------------------------SHIP-----------------------------------------------
fig,axs2=plt.subplots(1,2,figsize=(27,10))
plt.style.use("dark_background")

axs2[0].plot(df2["TIME[S]"],df2["SPEED"]*.2778,linewidth=1)
axs2[0].set_xlabel("Time(s)")
axs2[0].set_ylabel("Speed(m/s)")
axs2[0].set_title("TIME vs SPEED(Ship)")
axs2[0].grid(True,linewidth=.2)

axs2[1].plot(df2["TIME[S]"],df2["altitude"]*1000,linewidth=1)
axs2[1].set_xlabel("Time(s)")
axs2[1].set_ylabel("Altitude(m)")
axs2[1].set_title("TIME vs ALTITUDE(Ship)")
axs2[1].grid(True,linewidth=.2)
#------------------------------------Acceleration---------------------------------------

plt.figure()
acc=[]
for i in range(len(df1["SPEED"])):
    try :
        acc.append(((df1["SPEED"][i+1]-df1["SPEED"][i])/1))
    except:
        acc.append(0)

        
    
plt.plot(df1["TIME[S]"],acc)
plt.title("Time(s) vs Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.ylabel("acceleration(m/s)")
plt.grid(True)
#-----------------------------------MAX-Q--------------------------------------------------

DP=[]
t=[]

for i in range(len(df1)):
    if i<=200:
        t.append(i)
        v=(df1["SPEED"][i]*1000)/3600
        h=df1["altitude"][i]*1000
        
        DP.append(dynamic_pressure(v, h))

    
plt.figure()
plt.plot(t,DP)
plt.title("Determining MAX-Q through plotting")
plt.xlabel("Time(s)")
plt.ylabel("Dynamic pressure")
plt.axhline(np.max(DP),linestyle="dotted",linewidth=1.5,color="red")
plt.annotate(f"MAX-Q = {np.round(np.max(DP),2)}kPa",(0,np.max(DP)),(110,17))

MAX_Q_index=DP.index(np.max(DP))
print(f"MAXIMUM DYNAMIC PRESSURE:{np.round(np.max(DP),2)}kPa")
plt.axvline(t[MAX_Q_index],linestyle="dotted",linewidth=1.5,color="red")
plt.scatter(t[MAX_Q_index],np.max(DP),color="blue")




#--------------------------------------REGRESSION PLOT--------------------------------
plt.figure()
plt.scatter(df1["TIME[S]"][60:100],acc[60:100],label="Actual data")

linreg=stats.linregress(df1["TIME[S]"][60:100],acc[60:100])
pred=linreg.slope*df1["TIME[S]"][60:100]+linreg.intercept

plt.plot(df1["TIME[S]"][60:100],pred,color="red",linewidth=2,label="Regression line")
plt.xlabel("Time(s)")
plt.ylabel("acceleration(m/s)")
plt.legend()
plt.grid(True,linewidth=0.3)

#-------------------------ROOT MEAN SQUARE ERROR---------------------------------------


acc_base = np.full_like(acc[60:100], fill_value=np.mean(acc[60:100]))

print("\nRMSE Baseline =",rmse(acc[60:100],acc_base))
print("RMSE Model =", rmse(acc[60:100],pred))

