import plotly.graph_objects as go
import numpy as np

def create_earth_choropleth(df):
    fig = go.Figure()

    # Country boundaries + water quality
    fig.add_trace(go.Choropleth(
        locations=df["ISO"],
        z=df["WaterQuality"],
        text=df["Country"],
        colorscale="Blues",
        colorbar_title="Water Quality Index",
        marker_line_color="white",
        marker_line_width=0.5
    ))

    fig.update_layout(
        geo=dict(
            projection_type="orthographic",
            showland=True,
            landcolor="rgb(40, 40, 40)",
            showocean=True,
            oceancolor="rgb(10, 20, 60)",
            showcountries=True,
            countrycolor="white",
            showcoastlines=True,
            coastlinecolor="lightgray"
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig


def add_ocean_currents(fig):
    lats = np.linspace(-60, 60, 12)
    lons = np.linspace(-180, 180, 24)

    for lat in lats:
        fig.add_trace(go.Scattergeo(
            lon=lons,
            lat=[lat] * len(lons),
            mode="lines",
            line=dict(width=1.5, color="cyan"),
            opacity=0.4,
            showlegend=False
        ))

    return fig
