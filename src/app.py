from pathlib import Path
import pandas as pd
import streamlit as st

from functions import (
    dataset_info,
    remove_duplicates,
    replace_missing_val,
    sort_by_column,
    export_csv
)


BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "data" / "Employee.csv"

df = pd.read_csv(csv_path)

st.title("CSV Data Organizer")


choice = st.sidebar.selectbox(
    "Choose Service",
    ["View Dataset", "Dataset Information", "Remove Duplicates", "Fill Missing Values", "Sort by Column", "Export Cleaned CSV"]
)

if choice == "View Dataset":

    st.header("Current Dataset")

    st.dataframe(df)


elif choice == "Dataset Information":

    st.header("Dataset Information")

    info = dataset_info(df)

    st.write("Rows:", info["Rows"])

    st.write("Columns:", info["Columns"])

    st.subheader("Column Names")
    st.write(info["Column Names"])

    st.subheader("Data Types")
    st.write(info["Data Types"])


elif choice == "Remove Duplicates":

    st.header("Remove Duplicate Rows")

    if st.button("Remove Duplicates"):

        df = remove_duplicates(df)

        st.success("Duplicates removed successfully!")

        st.dataframe(df)


elif choice == "Fill Missing Values":

    st.header("Fill Missing Values")

    value = st.text_input(
        "Enter value to replace missing values"
    )

    if st.button("Fill Values"):

        df = replace_missing_val(df, value)

        st.success("Missing values filled!")

        st.dataframe(df)


elif choice == "Sort by Column":

    st.header("Sort Dataset")

    column = st.selectbox(
        "Choose Column",
        df.columns
    )


    order = st.radio(
        "Sorting Order",
        [
            "Ascending",
            "Descending"
        ]
    )


    if st.button("Sort"):

        if order == "Ascending":
            ascending = True
        else:
            ascending = False


        df = sort_by_column(
            df,
            column,
            ascending
        )


        st.success("Dataset sorted!")

        st.dataframe(df)


elif choice == "Export Cleaned CSV":

    st.header("Export Dataset")


    output_folder = BASE_DIR / "output"
    output_folder.mkdir(exist_ok=True)

    output_path = output_folder / "cleaned_employee.csv"


    export_csv(df, output_path)


    st.success("CSV exported successfully!")

    st.write(
        f"Saved at: {output_path}"
    )