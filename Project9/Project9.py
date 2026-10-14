import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
        except PermissionError:
            print("[Error: You don't have permission to this path, move the file to another path]")
        except FileNotFoundError:
            print("[Error: No such file found]")
        except TypeError:
            print("[Error: You can import only '.csv' files]")
        else:
            print("Dataset loaded successfully!")
            self.data = pd.DataFrame(self.data)
        return self.data
    def explore_data(self, option):
        if(self.data is None or self.data.empty):
            print("[Error: Load the dataset first]")
            return        
        if(option == "1"):
            return self.data.head()
        elif(option == "2"):
            return self.data.tail()
        elif(option == "3"):
            columns = self.data.columns.tolist()
            return columns
        elif(option == "4"):
            data_types = self.data.dtypes
            return data_types
        elif(option == "5"):
            df_info = self.data.info()
            return df_info
    def clean_data(self, choice):
        if(self.data is None or self.data.empty):
            print("[Error: Load the dataset first]")
            return
        if(choice == "1"):
            count = self.data.isna().any(axis=1).sum().sum()
            if(count < 1):
                return "\nNo null values found", 0
            else:
                return self.data[self.data.isna().any(axis=1)], self.data.isna().any(axis=1).sum()
        elif(choice == "2"):
            count = self.data.select_dtypes(include="number").isna().sum().sum()
            self.data = self.data.fillna(self.data.mean(numeric_only=True))
            return count
        elif(choice == "3"):
            count = self.data.isna().any(axis=1).sum().sum()
            self.data = self.data.dropna(how="any")
            return count
        elif(choice == "4"):
            value = input("Enter specific value (int/string): ")
            if(value.isnumeric()):
                num_cols = self.data.select_dtypes(include="number").columns
                self.data[num_cols] = self.data[num_cols].fillna(value)
            elif(value.isalpha()):
                alpha_cols = self.data.select_dtypes(exclude="number").columns
                self.data[alpha_cols] = self.data[alpha_cols].fillna(value)
    def methamatical_operations(self):
        pass #Can be considered same as aggregate_functions()
    def combine_data(self):
        pass #Never needed for any given operations
    def split_data(self):
        pass #Never needed for any given operations
    def search_sort_filter(self, choice):
        if(self.data is None or self.data.empty):
            print("[Error: Load the dataset first]")
            return        
        if(choice == "1"):
            cols = []
            col_in = 0
            col_names = input("Enter column names (space-separated): ")
            col_names = col_names.split(" ")
            cols.clear()
            for i in col_names:
                if(i.title() not in self.data.columns):
                    print("[Error: No such column]")
                    break
                cols.append(i.title())
                col_in += 1
            if(col_in > 0):
                return self.data[cols]
            else:
                return
        elif(choice == "2"):
            start_row = int(input("Enter starting row index: "))
            end_row = int(input("Enter ending row index: "))
            if(start_row < 0):
                print("[Error: Starting range can't be negative]")
                return
            elif(end_row > self.data.index[-1]):
                print("[Error: Ending range out of scope]")
            elif(start_row > end_row):
                print("[Error: Inappropriate values]")
            else:
                return self.data.iloc[start_row:end_row]
        elif(choice == "3"):
            col = input("Enter column name: ")
            if(col not in self.data.columns):
                print("[Error: No such column]")
                return
            order = input("Ascending or Descending(a/d): ")
            if(order.lower() == "a" or order.lower() == "ascending"):
                return self.data.sort_values(col)
            elif(order.lower() == "d" or order.lower() == "descending"):
                return self.data.sort_values(col, ascending=False)
            else:
                print("[Error: No such option]")
                return
        elif(choice == "4"):
            col = input("Enter column name:")
            if(col.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            threshold = int(input("Enter a numeric threshold value: "))
            if(threshold > self.data[col.title()].max()):
                print("[Error: Too big threshold]")
                return
            return self.data[self.data[col.title()] >= threshold]        
    def aggregate_functions(self):
        pass #Already done in statistical_analysis by using .describe()
    def statistical_analysis(self):
        if(self.data is None or self.data.empty):
            print("[Error: Load the dataset first]")
            return
        analysis = self.data.describe(include="all").round(2)
        return analysis
    def create_pivot_table(self, x_axis, y_axis, group_column):
        self.pivot_data = self.data.pivot_table(
            index=x_axis,
            columns=group_column,
            values=y_axis,
            aggfunc="sum",
            fill_value=0
        )
    def visualize_data(self, plot):
        if(self.data is None or self.data.empty):
            print("[Error: Load the dataset first]")
            return
        if(plot == "1"):
            print("\n== Bar Plot ==")
            x_axis = input("Enter x-axis column name(recommended: Product): ").strip()
            if(x_axis.title() not in self.data.columns):
                print("[Erro: No such column]")
                return
            y_axis = input("Enter y-axis column name(recommended: Sales): ").strip()
            if(y_axis.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            try:
                sb.barplot(x = x_axis.title(), y = y_axis.title(), data = self.data)
                plt.title(f"Bar Plot for: {x_axis.title()} and {y_axis.title()}")
                plt.xlabel(x_axis.title())
                plt.ylabel(y_axis.title())
                plt.xticks(rotation = 35, ha = "right")
            except TypeError:
                print("[Error: Arguments you have passed may be wrong]")
            except AttributeError:
                print("[Error: No such dataframe]")
            except ValueError:
                print("[Error: Arguments you have passed may be wrong]")
            else:
                plt.show()
                print("Bar plot displayed successfully!")
        elif(plot == "2"):
            print("\n== Line Plot ==")
            x_axis = input("Enter x-axis column name: ").strip()
            if(x_axis.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            y_axis = input("Enter y-axis column name: ").strip()
            if(y_axis.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            try:
                sb.lineplot(x = x_axis.title(), y = y_axis.title(), data = self.data)
                plt.title(f"Line Plot for: {x_axis.title()} and {y_axis.title()}")
                plt.xlabel(x_axis.title())
                plt.ylabel(y_axis.title())
                plt.xticks(rotation = 35, ha = "right")
            except TypeError:
                print("[Error: Arguments you have passed may be wrong]")
            except AttributeError:
                print("[Error: No such dataframe]")
            except ValueError:
                print("[Error: Arguments you have passed may be wrong]")
            else:
                plt.show()
                print("Line plot displayed successfully!")
        elif(plot == "3"):
            print("\n== Scatter Plot ==")
            x_axis = input("Enter x-axis column name(recommended: Sales): ").strip()
            if(x_axis.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            y_axis = input("Enter y-axis column name(recommended: Profit): ").strip()
            if(y_axis.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            try:
                sb.scatterplot(x = x_axis.title(), y = y_axis.title(), data = self.data)
                plt.title(f"Scatter Plot for: {x_axis.title()} and {y_axis.title()}")
                plt.xlabel(x_axis.title())
                plt.ylabel(y_axis.title())
                plt.xticks(rotation = 35, ha = "right")
            except TypeError:
                print("[Error: Arguments you have passed may be wrong]")
            except AttributeError:
                print("[Error: No such dataframe]")
            except ValueError:
                print("[Error: Arguments you have passed may be wrong]")
            else:
                plt.show()
                print("Line plot displayed successfully!")
        elif(plot == "4"):
            print("\n== Pie Chart ==")
            col_name = input("Enter column name(recommended: Region): ").strip()
            if(col_name.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            try:
                values = self.data[col_name.title()].value_counts()
                plt.pie(values, labels=values.index, autopct="%.2f")
                plt.title(f"Pie Plot for: {col_name.title()}")
                plt.legend(fancybox = True, loc = "upper right", shadow = True)
            except TypeError:
                print("[Error: Arguments you have passed may be wrong]")
            except AttributeError:
                print("[Error: No such dataframe]")
            except ValueError:
                print("[Error: Arguments you have passed may be wrong]")
            else:
                plt.show()
                print("Pie Chart displayed successfully!")
        elif(plot == "5"):
            print("\n== Histogram ==")
            col_name = input("Enter column name(recommended: Product): ").strip()
            if(col_name.title() not in self.data.columns):
                print("[Error: No such column]")
                return
            nBins = int(input("Enter number of bins(recommended: 5): "))
            try:
                sb.histplot(x = col_name.title(), data = self.data, bins = nBins)
                plt.title(f"Histogram for: {col_name.title()}")
                plt.xlabel(col_name.title())
                plt.ylabel("Frequency")
                plt.xticks(rotation = 35, ha = "right")
            except TypeError:
                print("[Error: Arguments you have passed may be wrong]")
            except AttributeError:
                print("[Error: No such dataframe]")
            except ValueError:
                print("[Error: Arguments you have passed may be wrong]")
            else:
                plt.show()
                print("Histogram displayed successfully!")
        elif(plot == "6"):
            print("\n== Stack Plot ==")
            x_axis = input("Enter x-axis column name(recommended: Product): ").strip().title()
            if(x_axis not in self.data.columns):
                print("[Error: No such column]")
                return
            y_axis = input("Enter numerical column name(recommended: Sales): ").strip().title()
            if(y_axis not in self.data.columns):
                print("[Error: No such column]")
                return
            group_column = input("Enter grouping column name(recommended: Region): ").strip().title()
            if(group_column not in self.data.columns):
                print("[Error: No such column]")
                return
            try:
                self.create_pivot_table(x_axis, y_axis, group_column)
                if self.pivot_data.empty or self.pivot_data.shape[1] < 2:
                    print("[Error: At least two groups are required]")
                    return
                plt.stackplot(range(len(self.pivot_data.index)),*[self.pivot_data[col] for col in self.pivot_data.columns],labels=self.pivot_data.columns)
                plt.xticks(range(len(self.pivot_data.index)), self.pivot_data.index, rotation=45)
                plt.xlabel(x_axis)
                plt.ylabel(y_axis)
                plt.title(f"Stack Plot for: {y_axis} and {x_axis}")
                plt.legend(title=group_column)
            except TypeError:
                print("[Error: Arguments you have passed may be wrong]")
            except AttributeError:
                print("[Error: No such dataframe]")
            except ValueError:
                print("[Error: Arguments you have passed may be wrong]")
            else:
                plt.show()
                print("Stack plot displayed successfully!")

sda = SalesDataAnalyzer()
x_axis = None
y_axis = None
group_column = None
while True:
    print("\n========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("="*60)
    choice = input("\nEnter your choice: ")
    match choice:
        case "1":
            print("\n== Load Dataset ==")
            path = input("Enter the path of the dataset (CSV file): ")
            DataFrame = sda.load_data(path)
        case "2":
            while True:
                print("\n== Explore Data ==")
                print("1. Display the first 5 rows")
                print("2. Display the last 5 rows")
                print("3. Display column names")
                print("4. Display data types")
                print("5. Display basic info")
                ed_choice = input("Enter your choice: ")
                match ed_choice:
                    case "1":
                        print("\nFirst 5 rows of dataset:")
                        first_rows = sda.explore_data(ed_choice)
                        print(first_rows)
                        break
                    case "2":
                        print("\nLast 5 rows of dataset:")
                        last_rows = sda.explore_data(ed_choice)
                        print(last_rows)
                        break
                    case "3":
                        print("\nColumn names:")
                        col_names = sda.explore_data(ed_choice)
                        for i in col_names:
                            print(f"- {i}")
                        break
                    case "4":
                        print("\nData types:")
                        data_types = sda.explore_data(ed_choice)
                        print(data_types)
                        break
                    case "5":
                        print("\nDataset basic info:")
                        basic_info = sda.explore_data(ed_choice)
                        print(basic_info)
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "3":
            while True:
                print("\n== DataFrame Operations ==")
                print("1. Select specific columns")
                print("2. Select rows range")
                print("3. Sort by columns")
                print("4. Filter by threshold")
                dfo_choice = input("Enter your choice: ")
                match dfo_choice:
                    case "1":
                        result = sda.search_sort_filter(dfo_choice)
                        print(f"\n{result}")
                        break
                    case "2":
                        result = sda.search_sort_filter(dfo_choice)
                        print(f"\n{result}")
                        break
                    case "3":
                        result = sda.search_sort_filter(dfo_choice)
                        print(f"\n{result}")
                        break
                    case "4":
                        result = sda.search_sort_filter(dfo_choice)
                        print(f"\n{result}")
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "4":
            while True:
                print("\n== Handle Missing Data ==")
                print("1. Display rows with missing values")
                print("2. Fill missing values with mean")
                print("3. Drop missing values")
                print("4. Replace missing values with a specific value")
                hmd_choice = input("Enter your choice: ")
                match hmd_choice:
                    case "1":
                        result, count = sda.clean_data(hmd_choice)
                        if count > 0:
                            print("\nNull values:")
                            print(result)                        
                            print(f"\n{count} null values found")
                        else:
                            print(result)
                        break
                    case "2":
                        count = sda.clean_data(hmd_choice)
                        print(f"\n{count} numeric null values filled with mean")
                        break
                    case "3":
                        count = sda.clean_data(hmd_choice)
                        print(f"\n{count} null values dropped")
                        break
                    case "4":
                        sda.clean_data(hmd_choice)
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "5":
            analysis = sda.statistical_analysis()
            print(f"\n{analysis}")
            while True:
                save = input("\nSave descriptive statistics as a file?(y/n): ")
                if(save.lower() == "y" or save.lower() == "yes"):
                    name = input("Enter file name(e.g., statistics.txt): ")
                    try:
                        with open(name, "x") as file:
                            file = file.writelines(analysis.to_string())
                    except FileExistsError:
                        print(f"[Error: File named {name} already exists]")
                    else:
                        print("File created successfully")
                        break
                elif(save.lower() == "n" or save.lower() == "no"):
                    break
                else:
                    print("Invalid choice")
                    continue
        case "6":
            while True:
                print("\n== Data Visualization ==")
                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. Pie Chart")
                print("5. Histogram")
                print("6. Stack Plot")
                dv_choice = input("Enter your choice: ")
                match dv_choice:
                    case "1":
                        sda.visualize_data(dv_choice)
                        break
                    case "2":
                        sda.visualize_data(dv_choice)
                        break
                    case "3":
                        sda.visualize_data(dv_choice)
                        break
                    case "4":
                        sda.visualize_data(dv_choice)
                        break
                    case "5":
                        sda.visualize_data(dv_choice)
                        break
                    case "6":
                        sda.visualize_data(dv_choice)
                        break
                    case _:
                        print("Invalid choice")
                        continue
        case "7":
            print("== Save Visualization ==")
        case "8":
            print("\nExiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice")
            continue