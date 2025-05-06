import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.title("This is Exploratory Data Analysis for our dataset !")



# Mappings
site_map = {1: "Staten Island", 2: "MRV", 3: "Midtown", 4: "Harlem", 5: "SI RUMC"}
ethnicity_map = {
    0: "Not Hispanic or Latino", 1: "Hispanic or Latino", 2: "Decline to specify", 3: "Unknown"
}
race_map = {
    0: "White/Caucasian", 1: "Black/African American", 2: "Hispanic", 3: "Asian", 4: "Indian",
    5: "Native American Indian", 6: "American Indian/Alaskan Native", 7: "Native Hawaiian/Other Pacific Islander",
    8: "Two or more races", 9: "Other race", 10: "Unknown", 11: "Choose not to specify"
}
scan_location_map = {1: "Staten Island", 2: "RUBIC", 3: "CBIC", 4: "CUNY"}

Barratt_Barratt_Edu={3: "Less than 7th grade", 6: "Junior high/Middle school (9th grade)", 9: "Partial high school (10th or 11th grade)",
                       12: "High school graduate", 15: "Partial college (at least one year)", 18: "College education", 21: "Graduate degree"}


# Apply mapping


# Plotting function
def prep_bar_chart(series):
    return series.value_counts().rename_axis('Category').reset_index(name='Count').set_index('Category')
# Individual charts






def Eda_data(repository):
  df= pd.read_excel(repository,engine='openpyxl')
  st.subheader("The Dataset")
  df
  st.subheader("The shape of the dataset is: ")
  df.shape
  description=df.describe()
  st.subheader("Description of Dataset: ")
  description
  df2=pd.DataFrame()
  df2['Basic_Demos_Study_Site'] = df['Basic_Demos_Study_Site'].map(site_map)
  df2['PreInt_Demos_Fam_Child_Ethnicity'] = df['PreInt_Demos_Fam_Child_Ethnicity'].map(ethnicity_map)
  df2['PreInt_Demos_Fam_Child_Race'] = df['PreInt_Demos_Fam_Child_Race'].map(race_map)
  df2['MRI_Track_Scan_Location'] = df['MRI_Track_Scan_Location'].map(scan_location_map)
  df2['Barratt_Barratt_P1_Edu']=df['Barratt_Barratt_P1_Edu'].map(Barratt_Barratt_Edu)
  df2['Barratt_Barratt_P2_Edu']=df['Barratt_Barratt_P2_Edu'].map(Barratt_Barratt_Edu)
  st.subheader('Study Site Distribution')
  st.bar_chart(prep_bar_chart(df2['Basic_Demos_Study_Site']))

  st.subheader('Child Ethnicity Distribution')
  st.bar_chart(prep_bar_chart(df2['PreInt_Demos_Fam_Child_Ethnicity']))

  st.subheader('Child Race Distribution')
  st.bar_chart(prep_bar_chart(df2['PreInt_Demos_Fam_Child_Race']))

  st.subheader('MRI Scan Location Distribution')
  st.bar_chart(prep_bar_chart(df2['MRI_Track_Scan_Location']))

  st.subheader('Parent 1 Education')
  st.bar_chart(prep_bar_chart(df2['Barratt_Barratt_P1_Edu']))

  st.subheader('Parent 2 Education')
  st.bar_chart(prep_bar_chart(df2['Barratt_Barratt_P2_Edu']))

  st.subheader("Corrlation matrix")
  df1 = df.iloc[:, 1:]  # Exclude first column if needed
  correlation_matrix = df1.corr()

# Plot using matplotlib and seaborn
  fig, ax = plt.subplots(figsize=(8, 6))
  sns.heatmap(correlation_matrix, cmap='coolwarm', center=0, linewidths=0.5, ax=ax)
  ax.set_title('Correlation Matrix Heatmap')

# Display in Streamlit
  st.pyplot(fig)



option = st.selectbox(
    "Select",
    ("Training Data", "Test Data"),
    index=None,
    placeholder="Select dataset...",
)


if option=="Test Data":
   Eda_data('dataset/TEST_CATEGORICAL.xlsx')
if option=="Training Data":
   Eda_data('dataset/TRAIN_CATEGORICAL_METADATA.xlsx')
else:
   st.error("None had been selected")
