import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

def main(): #entry point
    st.title("This is my streamlit app for ecommerce")
    st.sidebar.title("Uploading Zone")
    uploaded_file  = st.sidebar.file_uploader("Upload your file here", type = [ 'csv','xlsx'])

    if uploaded_file is not None:
        try :
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:     
                data = pd.read_excel(uploaded_file)
            st.sidebar.success("File Uploaded successfully")
            st.subheader("data overview")
            st.dataframe(data.head())
            st.subheader("Basic information of data")
            st.write("shape of the data", data.shape)
            st.write("Columns in my data",data.columns)
            st.write("Missing value" , data.isnull().sum())
            st.subheader("I will show you the stats of the data")
            st.write(data.describe())
        except Exception as e:
            print("it will handle if things go wrong",e)
    else:
        pass

if __name__ == "__main__":
  main()    
