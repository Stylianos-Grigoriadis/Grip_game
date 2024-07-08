import pandas as pd
import matplotlib.pyplot as plt
import lib
df = pd.read_excel(r"C:\Users\Stylianos\OneDrive\Apollonios\Data from Grip\grip_strength_Grig_Styl___26Jan24_10_34_19.xlsx", skiprows=2, decimal=",",nrows=4548)
print(df)
print(type(df["Performance"]))
Game_with_stops = []
Game_without_stops = []
Starting_value_index = 0
for i in range(len(df["Performance"])):
    print(df["Performance"][i])
    try:
        df["Performance"][i] = float(df["Performance"][i])
        Game_with_stops.append(float(df["Performance"][i]))
        print(type(df["Performance"][i]))
    except:
        print(i)
        Starting_value_index = i+1
        print(Starting_value_index)
        break
End_value_index= len(df["Performance"]) -1
for i in range(Starting_value_index,End_value_index):
    print(i)
    Game_without_stops.append(df["Performance"][i])

for i in range(len(Game_without_stops)):
    print(Game_without_stops[i])
    print(type(Game_without_stops[i]))
print(Game_without_stops)
print(Starting_value_index)
print(End_value_index)
plt.plot(Game_with_stops, label= "Game with stops")
plt.plot(Game_without_stops, label= "Game without stops")
plt.legend()
plt.show()

Game_with_stops.pop()
Game_with_stops.pop()
Game_without_stops.pop()
Game_without_stops.pop()
print(Game_with_stops[-1])
print(Game_with_stops[-2])
print(Game_without_stops[-1])
print(Game_without_stops[-2])

Total_area_Game_with_stops = 0
for i in range(len(Game_with_stops)):
    if i-1>0:
        Total_area_Game_with_stops = Total_area_Game_with_stops + ((Game_with_stops[i-1] + Game_with_stops[i])*(Game_with_stops[i] - Game_with_stops[i-1]))/2
        print(i)
        print(Total_area_Game_with_stops)
    else:
        pass
print(Total_area_Game_with_stops)

total_area1 = lib.intergral(Game_with_stops,0.0133)
total_area2 = lib.intergral(Game_without_stops,0.0133)
print(total_area1[-1])
print(total_area2[-1])
