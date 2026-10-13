while True:
    print("========== Data Analysis & Visualization Program ==========")
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
        case "2":
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            ed_choice = ("Enter your choice: ")
            match ed_choice:
                case _:
                    print("Invalid choice")
                    continue
        case "3":
            pass
        case "4":
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop missing values")
            print("4. Replace missing values with a specific value")
            hmd_choice = input("Enter your choice: ")
            match hmd_choice:
                case _:
                    print("Invalid choice")
                    continue
        case "5":
            pass
        case "6":
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            dv_choice = input("Enter your choice: ")
            match dv_choice:
                case _:
                    print("Invalid choice")
                    continue
        case "7":
            print("== Save Visualization ==")
        case "8":
            print("\nExiting the program. Goodbye!")
        case _:
            print("Invalid choice")
            continue