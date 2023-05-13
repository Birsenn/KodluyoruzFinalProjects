import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Araba Sigorta Poliçesi", page_icon="🚗")

st.markdown("# 🚗 Araba Sigorta Poliçesi" )
st.sidebar.header("🚗 Araba Sigorta Poliçesi")
st.write(
    """Arabalarına sigorta poliçesi yaptıran müşterilerin kaza yapıp yapmama ihtimalleri üzerinden,
       sigorta şirketinin ödeyebileceği muhtemel baz primlerin tahminlenmesi amaçlanmıştır.
       \nFrekans-Severity methodu ile modelleme kurulmuştur.
       \n**👇Aşağıdaki değerleri değiştirerek muhtemel baz prim hesabı yaptırabilirsiniz.👈**
        
        """
)

# (Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)

st.sidebar.success(f"###  👉 Tahmini Baz Prim: $")  

#############
# Data set ten grafik gösteren, seçilen değerlere göre aynı grafiği güncelleyen bir script
#@st.cache_data
#def get_UN_data():
#    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
#    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
#    return df.set_index("Region")


#try:
#    df = get_UN_data()
#    countries = st.multiselect(
#        "Choose countries", list(df.index), ["China", "United States of America"]
#    )
#    if not countries:
#        st.error("Please select at least one country.")
#    else:
#        data = df.loc[countries]
#        data /= 1000000.0
#        st.write("### Gross Agricultural Production ($B)", data.sort_index())

#        data = data.T.reset_index()
#        data = pd.melt(data, id_vars=["index"]).rename(
#            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#        )
#        chart = (
#            alt.Chart(data)
#            .mark_area(opacity=0.3)
#            .encode(
#                x="year:T",
#                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#                color="Region:N",
#            )
#        )
#        st.altair_chart(chart, use_container_width=True)
#except URLError as e:
#    st.error(
#        """
#        **This demo requires internet access.**
#        Connection error: %s
#    """
#        % e.reason
#    )
 