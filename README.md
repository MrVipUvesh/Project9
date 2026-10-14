# Sales Data Analyzer

## Overview

**Sales Data Analyzer** is a Python-based data analysis and visualization project designed to work with CSV datasets. It uses Pandas for data manipulation, NumPy-style tabular analysis through Pandas, Matplotlib for plotting, and Seaborn for statistical visualizations.

The program provides a menu-driven interface that allows users to load datasets, explore their structure, perform DataFrame operations, handle missing values, generate descriptive statistics, and visualize relationships between different columns.

It is designed as a practical project for learning data analysis, data cleaning, statistical summaries, and visualization using Python.

## Features

### 1. Load Dataset
- Load datasets from CSV files using `pandas.read_csv()`.
- Display a success message after loading a dataset.
- Handle common file-loading errors, including missing files and permission issues.
- Store the loaded dataset in a Pandas DataFrame for further operations.

### 2. Explore Data
Explore the structure and contents of a loaded dataset through the following options:

- **Display the first five rows:** View the beginning of the dataset using `head()`.
- **Display the last five rows:** View the ending of the dataset using `tail()`.
- **Display column names:** Retrieve all column names as a list.
- **Display data types:** Identify the data type of each column.
- **Display basic information:** Show information about the DataFrame, including column data types and non-null counts.

### 3. Perform DataFrame Operations
Perform common operations on the loaded dataset without manually modifying the source CSV file.

- **Select specific columns:** Display only the columns entered by the user.
- **Select a row range:** Retrieve a range of rows using integer-based indexing.
- **Sort by a column:** Sort the dataset in ascending or descending order.
- **Filter by threshold:** Select rows where a specified column contains values greater than or equal to a numeric threshold.

These operations return a DataFrame or a selected portion of the data for inspection.

### 4. Handle Missing Data
Identify and manage missing values in the dataset.

- **Display rows with missing values:** Find and display rows containing one or more null values.
- **Fill missing numeric values with the mean:** Replace missing values using the mean of the corresponding numeric columns.
- **Drop rows with missing values:** Remove rows containing at least one missing value from the in-memory DataFrame.
- **Replace missing values with a specific value:** Enter a numeric or alphabetic value to fill missing values in selected column types.

Data-cleaning operations modify the DataFrame held in memory where applicable. The original CSV file is not automatically overwritten.

### 5. Generate Descriptive Statistics
Generate a descriptive statistical summary using:

    self.data.describe(include="all").round(2)

The summary can include:
- Count of non-null values
- Mean
- Standard deviation
- Minimum and maximum values
- Quartiles
- Unique-value counts for categorical columns
- Most frequent values and their frequencies, where applicable

Numeric statistics are rounded to two decimal places.

The program also allows users to save the displayed descriptive statistics to a text file. It creates a new file using exclusive creation mode (`"x"`) and reports an error if a file with the same name already exists.

### 6. Data Visualization
Create six types of plots using Seaborn and Matplotlib.

#### Bar Plot
Compare values across categories.

- Recommended columns: `Product` and `Sales`
- Useful for comparing sales across products or other categories.

#### Line Plot
Visualize changes or trends between two variables.

- Suitable for time-based or sequential data.
- Example: Date versus Sales.

#### Scatter Plot
Examine the relationship between two variables.

- Recommended columns: `Sales` and `Profit`
- Useful for identifying patterns, clusters, and potential outliers.

#### Pie Chart
Display the frequency distribution of values in a categorical column.

- Recommended column: `Region`
- Uses `value_counts()` to calculate the frequency of each category.
- Displays category labels and percentage annotations.

#### Histogram
Visualize the distribution of values in a column.

- Allows the user to specify the number of bins.
- Displays frequency on the y-axis.
- Useful for understanding how numerical observations are distributed.

#### Stack Plot
Compare cumulative values across categories and groups.

- Recommended columns: `Product`, `Sales`, and `Region`
- Creates a pivot table using `pivot_table()`.
- Aggregates sales using `sum`.
- Uses regions as groups and products as the x-axis categories.
- Requires at least two groups for the plot to be displayed.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | CSV loading, DataFrame operations, data cleaning, and statistical analysis |
| Matplotlib | Plot rendering, labels, titles, legends, and figure display |
| Seaborn | Statistical plots, including bar, line, scatter, and histogram plots |
| CSV | Dataset input format |

## Requirements

- Python 3.10 or later, because the program uses `match-case` statements.
- Pandas
- Matplotlib
- Seaborn

## Installation

### 1. Install Python

Install Python 3.10 or later if it is not already installed.

### 2. Install the required libraries

Open a terminal or command prompt and run:

    pip install pandas matplotlib seaborn

### 3. Create the project file

Save the program in a Python file, for example:

    sales_data_analyzer.py

### 4. Prepare a CSV dataset

Create or obtain a CSV file containing the data you want to analyze.

Example dataset:

    Product,Sales,Profit,Region
    Laptop,50000,8000,North
    Mobile,30000,5000,South
    Tablet,20000,3000,East
    Laptop,45000,7000,West
    Mobile,35000,6000,North
    Tablet,25000,4000,South

This sample dataset can be used to try several of the available operations and plots. For the stack plot, use a dataset with at least two distinct groups in the selected grouping column.

### 5. Run the program

Navigate to the directory containing the Python file and run:

    python sales_data_analyzer.py

## Main Menu

When the program starts, it displays the following menu:

    ========== Data Analysis & Visualization Program ==========
    Please select an option:
    1. Load Dataset
    2. Explore Data
    3. Perform DataFrame Operations
    4. Handle Missing Data
    5. Generate Descriptive Statistics
    6. Data Visualization
    7. Save Visualization
    8. Exit

Select an option by entering its corresponding number.

**Important:** Load a dataset before selecting an option that requires data. Otherwise, the program displays an error message.

## Usage Guide

### Step 1: Load a dataset

Choose option `1` and enter the path to your CSV file.

Example:

    Enter the path of the dataset (CSV file): sales.csv

After the dataset is loaded, the program stores it in `self.data`.

### Step 2: Explore the dataset

Choose option `2` and select one of the five exploration options.

For example, selecting option `1` displays the first five rows, while option `4` displays the data type of each column.

### Step 3: Perform DataFrame operations

Choose option `3`.

To select columns, enter their names separated by spaces.

Example:

    Enter column names (space-separated): Product Sales

To sort the dataset, enter a column name and choose ascending or descending order.

To filter numeric data, select the threshold option, enter a numeric column, and provide a threshold value. The program returns rows whose values are greater than or equal to that threshold.

### Step 4: Handle missing values

Choose option `4`.

For example, select the mean-filling option to replace missing numeric values with their respective column means.

The program reports the number of missing numeric values it counted before filling them.

### Step 5: Generate statistics

Choose option `5` to display a descriptive summary.

The program then asks whether you want to save the summary to a file.

Example:

    Save descriptive statistics as a file?(y/n): y
    Enter file name(e.g., statistics.txt): statistics.txt

The output is written to the specified new text file if that filename does not already exist.

### Step 6: Visualize data

Choose option `6` and select a plot type.

For example, to generate a bar plot:

    Enter your choice: 1
    Enter x-axis column name(recommended: Product): Product
    Enter y-axis column name(recommended: Sales): Sales

The program displays the plot in a Matplotlib window.

For other plots, enter the appropriate column names and any additional input requested by the program.

### Step 7: Exit

Choose option `8` to terminate the program.

## Class and Method Overview

The program is organized around the `SalesDataAnalyzer` class.

| Method | Purpose |
|---|---|
| `__init__()` | Initializes `self.data` as `None`. |
| `load_data(file_path)` | Loads a CSV file into a Pandas DataFrame and handles selected file-loading errors. |
| `explore_data(option)` | Displays or returns dataset previews, column names, data types, or basic information. |
| `clean_data(choice)` | Displays missing-value rows, fills missing numeric values, drops incomplete rows, or attempts to fill missing values with a user-specified value. |
| `methamatical_operations()` | Placeholder for mathematical operations; currently contains no implementation. |
| `combine_data()` | Placeholder for combining datasets; currently contains no implementation. |
| `split_data()` | Placeholder for splitting datasets; currently contains no implementation. |
| `search_sort_filter(choice)` | Selects columns or rows, sorts data, and filters rows by a numeric threshold. |
| `aggregate_functions()` | Placeholder; the program currently uses descriptive statistics instead. |
| `statistical_analysis()` | Generates descriptive statistics using `describe(include="all")` and rounds the result to two decimal places. |
| `create_pivot_table(x_axis, y_axis, group_column)` | Creates a pivot table by grouping data and summing the selected numeric values. |
| `visualize_data(plot)` | Creates one of six supported plots based on the selected option. |

## Important Functions and Methods Used

| Function or method | Purpose |
|---|---|
| `pd.read_csv()` | Reads a CSV file into a DataFrame. |
| `pd.DataFrame()` | Creates a DataFrame. |
| `.head()` | Returns the first five rows by default. |
| `.tail()` | Returns the last five rows by default. |
| `.columns.tolist()` | Converts column names into a list. |
| `.dtypes` | Retrieves column data types. |
| `.info()` | Displays DataFrame structure and non-null counts. |
| `.isna()` | Identifies missing values. |
| `.select_dtypes()` | Selects columns based on data type. |
| `.fillna()` | Fills missing values. |
| `.dropna()` | Removes rows or columns containing missing values, depending on its arguments. |
| `.sort_values()` | Sorts rows using a selected column. |
| `.iloc[]` | Selects rows using integer positions. |
| `.describe()` | Generates descriptive statistics. |
| `.pivot_table()` | Summarizes data across selected categories. |
| `.value_counts()` | Counts occurrences of unique values. |
| `.to_string()` | Converts a tabular result into text. |
| `sb.barplot()` | Creates a bar plot. |
| `sb.lineplot()` | Creates a line plot. |
| `sb.scatterplot()` | Creates a scatter plot. |
| `sb.histplot()` | Creates a histogram. |
| `plt.pie()` | Creates a pie chart. |
| `plt.stackplot()` | Creates a stacked area plot. |
| `plt.title()` | Sets the plot title. |
| `plt.xlabel()` / `plt.ylabel()` | Sets axis labels. |
| `plt.xticks()` | Adjusts x-axis tick labels. |
| `plt.legend()` | Displays a legend. |
| `plt.show()` | Displays the plot. |

## Project Structure

    Sales-Data-Analyzer/
    ├── sales_data_analyzer.py
    ├── sales.csv
    └── README.md

- `sales_data_analyzer.py`: Contains the class, menu system, and analysis operations.
- `sales.csv`: Example input dataset; use your own CSV file if preferred.
- `README.md`: Project documentation.

The CSV file is an example dataset and is not required to have this exact filename.

## Data Handling and Limitations

- The program works with CSV datasets and expects the user to enter valid column names.
- Several column inputs are normalized using `.title()`. This may not match every possible column naming convention, especially names containing abbreviations, mixed capitalization, or special characters.
- The threshold filter expects a numeric column and an integer threshold.
- The row-range operation uses `iloc`, whose ending position is exclusive. For example, `iloc[0:5]` returns positions 0 through 4.
- Filling missing numeric values with the mean does not fill missing values in non-numeric columns.
- The custom replacement option accepts numeric-looking or alphabetic input. Its current implementation may not handle decimal numbers, negative numbers, or mixed alphanumeric values as intended.
- The visualization functions depend on the selected columns having appropriate data types. For example, scatter plots generally require numeric values, while a histogram is most meaningful for numerical data.
- The stack plot requires at least two groups in the selected grouping column.
- Descriptive statistics are saved to a text file. The visualization-saving menu option is displayed, but saving plots has not yet been implemented.
- Mathematical operations, dataset combination, dataset splitting, and the separate aggregate-functions method are currently placeholders.
- The program does not automatically save changes made during data cleaning back to the original CSV file.
- Error handling covers selected cases but does not guarantee that every invalid input or incompatible dataset will be handled gracefully.

## Learning Objectives

This project provides practical experience with:

- Python classes and object-oriented programming
- Functions, methods, conditionals, loops, and `match-case`
- Exception handling
- CSV file loading
- Pandas DataFrame manipulation
- Missing-value detection and treatment
- Sorting, filtering, and row selection
- Descriptive statistics
- Pivot tables and grouped summaries
- Data visualization with Seaborn and Matplotlib
- Saving statistical output to a text file
- Building menu-driven command-line applications

## Future Improvements

Possible improvements include:

- Implementing the visualization-saving option using `plt.savefig()`.
- Completing the mathematical operations and dataset combination/splitting methods.
- Improving column-name validation to support exact names without relying on `.title()`.
- Supporting decimal and negative numeric thresholds.
- Adding stronger validation for numeric columns and histogram bin counts.
- Improving handling of invalid input and empty datasets.
- Adding options to export cleaned datasets to CSV.
- Supporting more plots, such as box plots, heatmaps, and grouped bar plots.
- Adding automated tests for data loading, cleaning, filtering, and plotting.

## Conclusion

Sales Data Analyzer is a menu-driven Python project for exploring, cleaning, summarizing, and visualizing CSV data. It brings together Pandas, Seaborn, and Matplotlib in one application and provides a practical foundation for learning data analysis workflows.

The current version includes dataset exploration, missing-value handling, DataFrame operations, descriptive statistics, and six visualization options. Some menu options remain placeholders, providing clear opportunities for future development.
