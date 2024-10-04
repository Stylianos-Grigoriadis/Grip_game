import Lib_grip as lb
import matplotlib.pyplot as plt

data_5perc_1,data_5perc_2,data_5perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_5%.csv')
data_20perc_1,data_20perc_2,data_20perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_20%.csv')
data_40perc_1,data_40perc_2,data_40perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_40%.csv')
data_60perc_1,data_60perc_2,data_60perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_60%.csv')
data_80perc_1,data_80perc_2,data_80perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_80%.csv')
print(len(data_5perc_1["Performance"]))
print(len(data_5perc_2["Performance"]))
print(len(data_5perc_3["Performance"]))
Perc_list = [5,20,40,60,80]

SaEn_list_1 = []
SaEn_list_1.append(lb.Ent_Samp(data_5perc_1['Performance'][3000:], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_20perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_40perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_60perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_80perc_1['Performance'], 2, 0.2))

SaEn_list_2 = []
SaEn_list_2.append(lb.Ent_Samp(data_5perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_20perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_40perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_60perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_80perc_2['Performance'], 2, 0.2))

SaEn_list_3 = []
SaEn_list_3.append(lb.Ent_Samp(data_5perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_20perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_40perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_60perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_80perc_3['Performance'], 2, 0.2))

plt.plot(Perc_list,SaEn_list_1, c='k', label='Trial 1')
plt.plot(Perc_list,SaEn_list_2, c='blue', label='Trial 2')
plt.plot(Perc_list,SaEn_list_3, c='red', label='Trial 3')
plt.legend()
plt.show()


