from pathlib import Path
import pandas as pd

from functions import (view_dataset, dataset_info, remove_duplicates, replace_missing_val, sort_by_column, export_csv)

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "data" / "Employee.csv"

df = pd.read_csv(csv_path)

while True:

    print("\nCSV ORGANIZER")
    print("1. View Dataset")
    print("2. Dataset Information")
    print("3. Remove Duplicates")
    print("4. Fill Missing Values")
    print("5. Sort by Column")
    print("6. Export Cleaned CSV")
    print("7. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":
        df = view_dataset(df)
        print("\nCurrent Dataset:")
        print(df)


    elif choice == "2":
        info = dataset_info(df)

        print("\nDataset Information:")
        print("Rows:", info["Rows"])
        print("Columns:", info["Columns"])

        print("\nColumn Names:")
        print(info["Column Names"])

        print("\nData Types:")
        print(info["Data Types"])


    elif choice == "3":
        df = remove_duplicates(df)

        print("\nDuplicate rows removed successfully!")
        print(df)


    elif choice == "4":
        value = input("\nEnter the value to replace missing values: ")

        df = replace_missing_val(df, value)

        print("\nMissing values filled successfully!")
        print(df)


    elif choice == "5":

        print("\nChoose a column to sort:")

        columns = list(df.columns)

        for i, column in enumerate(columns, start=1):
            print(f"{i}. {column}")

        column_choice = int(input("\nEnter your choice: "))

        if 1 <= column_choice <= len(columns):

            selected_column = columns[column_choice - 1]

            print("\nSorting Order:")
            print("1. Ascending")
            print("2. Descending")

            order = input("Enter choice: ")

            if order == "1":
                ascending = True

            elif order == "2":
                ascending = False

            else:
                print("Invalid order!")
                continue


            df = sort_by_column(
                df,
                selected_column,
                ascending
            )

            print("\nSorted Dataset:")
            print(df)

        else:
            print("Invalid column choice!")


    elif choice == "6":

        output_folder = BASE_DIR / "output"
        output_folder.mkdir(exist_ok=True)

        output_path = output_folder / "cleaned_employee.csv"

        export_csv(df, output_path)

        print("\nFile exported successfully!")
        print(f"Location: {output_path}")


    elif choice == "7":
        print("Goodbye!")
        break


    else:
        print("Invalid choice!")