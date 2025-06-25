import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.set_page_config(page_title="Data Viewer", layout="wide")
    st.title("Data Viewer")
    st.sidebar.header("File Upload")

    uploaded_file = st.sidebar.file_uploader("Upload your data file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("File uploaded successfully.")

            st.subheader("Data Preview")
            st.dataframe(data.head())

            st.subheader("Dataset Summary")
            st.write("Shape:", data.shape)
            st.write("Columns:", list(data.columns))
            st.write("Missing Values:", data.isnull().sum())

            st.subheader("Descriptive Statistics")
            st.write(data.describe())

        except Exception as e:
            st.error(f"Error loading file: {e}")
    else:
        st.info("Please upload a CSV or Excel file to begin.")

if __name__ == "__main__":
    main()