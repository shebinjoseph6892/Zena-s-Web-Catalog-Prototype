# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

st.title("Zena's Amazing Athleisure Catalog")

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("zenas_athleisure_db.products.catalog_for_website").select(
    col("COLOR_OR_STYLE"),
    col("PRICE"),
    col("FILE_NAME"),
    col("FILE_URL"),
    col("SIZE_LIST"),
    col("UPSELL_PRODUCT_DESC")
)

pd_df = my_dataframe.to_pandas()

color_list = pd_df["COLOR_OR_STYLE"].tolist()
selected_color = st.selectbox("Pick a sweatsuit color or style:", color_list)

if selected_color:
    row = pd_df.loc[pd_df["COLOR_OR_STYLE"] == selected_color].iloc[0]

    st.image(row["FILE_URL"], caption=f"Our warm, comfortable, {selected_color} sweatsuit!", use_container_width=True)

