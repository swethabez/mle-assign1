import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Add and resize an image to the top of the app
img_fuel = Image.open("../img/fuel_efficiency.png")
st.image(img_fuel, width=700)

st.markdown("<h1 style='text-align: center; color: black;'>Fuel Efficiency</h1>", unsafe_allow_html=True)

# Import train dataset to DataFrame
train_df = pd.read_csv("../dat/train.csv")
model_results_df = pd.read_csv("../dat/model_results.csv")
shap_df = pd.read_csv("../dat/shap_values.csv")
# Create sidebar for user selection
with st.sidebar:
    # Add FB logo
    st.image("https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" )    

    # Available models for selection

    # YOUR CODE GOES HERE!
    models = ["DNN", "TPOT"]

    # Add model select boxes
    model1_select = st.selectbox(
        "Choose Model 1:",
        (models)
    )
    
    # Remove selected model 1 from model list
    # App refreshes with every selection change.
    models.remove(model1_select)
    
    model2_select = st.selectbox(
        "Choose Model 2:",
        (models)
    )

# Create tabs for separation of tasks
tab1, tab2, tab3 = st.tabs(["🗃 Data", "🔎 Model Results", "🤓 Model Explainability"])

with tab1:    
    # Data Section Header
    st.header("Raw Data")

    # Display first 100 samples of the dateframe
    st.dataframe(train_df.head(100))

    st.header("Correlations")

    # Heatmap
    corr = train_df.corr()
    fig = px.imshow(corr)
    st.write(fig)

with tab2:    
    
    # YOUR CODE GOES HERE!

    # Columns for side-by-side model comparison
    col1, col2 = st.columns(2)

    st.header(model1_select)
    model1_results = model_results_df[model_results_df["Model"] == model1_select]
    st.dataframe(model1_results)

    st.header(model2_select)
    model2_results = model_results_df[model_results_df["Model"] == model2_select]
    st.dataframe(model2_results)

    # Build the confusion matrix for the first model.




with tab3: 
    # YOUR CODE GOES HERE!
        # Use columns to separate visualizations for models
        # Include plots for local and global explanability!
    col1, col2 = st.columns(2)

    with col1:
        st.header(model1_select)

        model1_shap_df = shap_df[shap_df["Model"] == model1_select]
        st.dataframe(model1_shap_df)

    # Build confusion matrix for second model
    with col2:
        st.header(model2_select)

        model2_shap_df = shap_df[shap_df["Model"] == model2_select]
        st.dataframe(model2_shap_df)

    
