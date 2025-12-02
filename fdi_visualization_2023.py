import pandas as pd\n",
import numpy as np\n",
import plotly.express as px"

df = pd.read_csv("FDI_EconGrowth_Data.csv")
COL_COUNTRY = "country" 
COL_YEAR = "year"
COL_VALUE = "fdi_inflow"
YEAR_TO_PLOT = 2023

df = df[df[COL_YEAR] == YEAR_TO_PLOT].copy()
df[COL_VALUE] = pd.to_numeric(df[COL_VALUE], errors="coerce")
df = df.dropna(subset=[COL_VALUE, COL_COUNTRY]) 

df["fdi_bil"] = df[COL_VALUE]

fig = px.choropleth(
    df,
    locations=COL_COUNTRY, 
    locationmode="country names",
    color="fdi_bil",
    scope="asia",  
    color_continuous_scale="oranges",
    range_color=(max(0, df["fdi_bil"].min()), df["fdi_bil"].max()),
    title="FDI Net Inflow by Country (2023)",
    labels={"fdi_bil": "fdi_inflow"}  
)

fig.update_traces(marker_line_width=0.6, marker_line_color="white")

vmin, vmax = df["fdi_bil"].min(), df["fdi_bil"].max()
tick_step = 10
tick_vals = np.arange(
    np.floor(vmin / tick_step) * tick_step,
    np.ceil(vmax / tick_step) * tick_step + tick_step,
    tick_step
)
fig.update_coloraxes(
    colorbar=dict(
        title="fdi_inflow",
        tickvals=tick_vals,
        ticktext=[f"{int(t)}B" for t in tick_vals]
    )
)

fig.update_layout(
    title_x=0.06,
    margin=dict(l=40, r=220, t=60, b=20),  
)

fig.update_geos(
    showcountries=True,
    showcoastlines=False,
    showland=True, landcolor="rgb(236, 240, 241)",
    showocean=True, oceancolor="rgb(234, 242, 248)"
)

fig.show()
