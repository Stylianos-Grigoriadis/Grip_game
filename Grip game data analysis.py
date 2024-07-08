import pandas as pd
import numpy as np
import kineticstoolkit as ktk
import matplotlib.pyplot as plt

#Apo katw exw tis treis leitourgies
#grip_paris.print_statistical_values()
#grip_paris.create_plot_sets()
#grip_paris.export_combined_df() #kanei export ola ta set ena csv

class grip_game:
    def __init__(self, filename):
        self.df= pd.read_csv(filename, skiprows=2)
        self.split_dfs=[]
        self.combined_df=[]
        self.repetition_indices=[]
        self.time = []
        self.target =[]
        self.target_no_dupl=[]
        self.performance=[]
        self.time_series_dict={}
        # Create the necessary lists for analysis
        self.time_series_dict = {}
        self.spatial_error_list = []
        self.sum_list = {}
        self.max_list = {}
        self.min_list = {}
        self.mean_list = {}

        self.create_dataframe()
        self.data_analysis()

    def create_dataframe(self):

        # find and split the dataframe in Sets
        self.repetition_indices = self.df[self.df['Time'] == 'Device: K-Grip'].index
        print(len(self.repetition_indices))
        self.split_dfs = [self.df.iloc[start:end] for start, end in
                     zip([0] + self.repetition_indices.tolist(), self.repetition_indices.tolist() + [len(self.df)])]

    def data_analysis(self):

        for i in range(len(self.repetition_indices) + 1):
            # Turn them from strings to numeric values
            self.df = self.split_dfs[i].iloc[2:-1].reset_index(drop=True)
            self.df = self.df.replace('-', np.nan)
            self.df = self.df.astype(float)
            # print(self.df)

            # Separate the dataframes
            self.time = self.df["Time"]
            self.target = self.df["Target"]
            self.performance = self.df["Performance"]

            self.find_remove_duplicates(i)

            # Turn them to arrays
            time = np.array(self.time)
            target = np.array(self.target_no_dupl)
            performance = np.array(self.performance)

            # Use Kinetics tooltik for easier plotting
            self.time_series_dict[f"set_{i}"] = ktk.TimeSeries()
            self.time_series_dict[f"set_{i}"].time = time
            self.time_series_dict[f"set_{i}"].data["Target"] = target
            self.time_series_dict[f"set_{i}"].data["Performance"] = performance

            self.statistical_data(i)

    def find_remove_duplicates(self,i):
        i+=1
        self.target_dupl = self.target.duplicated()
        self.target_no_dupl = self.target.mask(self.target_dupl)

        count_non_nan_1 = self.target.notna().sum()
        count_non_nan_2 = self.target_no_dupl.notna().sum()
        print(f"With duplicates: Targets in set_{i}=", count_non_nan_1)
        print(f"Without duplicates: Targets in set_{i}=", count_non_nan_2)

    def statistical_data(self,i):
        # Extract Statistical data
        self.sum_list[f"set_{i+1}"] = np.sum(self.performance)
        self.min_list[f"set_{i+1}"] = np.min(self.performance)
        self.max_list[f"set_{i+1}"] = np.max(self.performance)
        self.mean_list[f"set_{i+1}"] = np.mean(self.performance)

    def create_plot_sets(self):
        self.time_series_dict[f"set_{0}"].plot(["Target"], "d-g")
        self.time_series_dict[f"set_{0}"].plot(["Performance"], "r")
        plt.title(f"set_{1}")
        plt.show()
        # Plot each set as a subplot
        # Calculate the grid for the subplots
        self.divide = len(self.repetition_indices)//3
        print(self.divide)
        self.remainder = len(self.repetition_indices)//3
        print(self.remainder)
        if self.remainder != 0:
            self.rows =  self.divide+1
        else:
            self.rows = self.divide
        print(self.rows)
        print(self.repetition_indices)
        print(range(len(self.repetition_indices) + 1))
        for i in range(len(self.repetition_indices) + 1):
            print(i)
            plt.subplot(self.rows, 3, i+1)
            self.time_series_dict[f"set_{i}"].plot(["Target"], "d-g")
            self.time_series_dict[f"set_{i}"].plot(["Performance"], "r")
            plt.title(f"set_{i + 1}")
        #plt.tight_layout()
        plt.show()

    def print_statistical_values(self):
        # print statistical values
        print("Sum of Performance:")
        for key, value in self.sum_list.items():
            print(f"{key}: {value}")
        print("\nMin of Performance:")
        for key, value in self.min_list.items():
            print(f"{key}: {value}")
        print("\nMax of Performance:")
        for key, value in self.max_list.items():
            print(f"{key}: {value}")
        print("\nMean of Performance:")
        for key, value in self.mean_list.items():
            print(f"{key}: {value}")

    def compbined_dfs(self):
        for idx, df in enumerate(self.split_dfs):
            if idx == 0:
             self.combined_df = df.copy()
            else:
                df=df.reset_index()
                df=df.drop(["index"],axis=1)
                # Rename columns to avoid conflicts
                df.columns = [col + f"_{idx}" for col in df.columns]
                self.combined_df = pd.concat([self.combined_df, df], axis=1)

    def export_combined_df(self):
        self.compbined_dfs()
        # print combinded_df
        print("combined_df")
        print(self.combined_df)
        # Write the combined DataFrame to a CSV file
        self.combined_df.to_csv("combined_dfs.csv", index=True)


# grip_paris=grip_game(r'G:\My Drive\Εργαστήριον\Operation Doctora\Specific Aims\Grip game\Pilot study 3\Αλλαγή στο Upper Perc 50% (1).csv')

#oi leitourgies
# grip_paris.create_dataframe()


grip_paris=grip_game(r'G:\Το Drive μου\Εργαστήριον\Operation Doctora\Specific Aims\Grip game\Pilot study 3\Rigid Αλλαγή στο Upper Perc 50% (1).csv')
grip_paris.compbined_dfs()
grip_paris.create_plot_sets()
grip_paris.export_combined_df()
# print(grip_paris.combined_df)
# print(grip_paris.repetition_indices)


# #grip_paris.export_combined_df() #kanei export ola ta set ena csv
# dfnew = pd.read_csv(r'G:\My Drive\Εργαστήριον\Operation Doctora\Specific Aims\Grip game\Pilot study 3\grip_strength_Grig_Styl___17Apr24_11_27_48.csv', skiprows=2)
# print(dfnew)
# plt.plot(dfnew["Target"], "d-g")
# plt.plot(dfnew["Performance"], "r")
# plt.show()

