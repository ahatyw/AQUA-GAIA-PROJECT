import dash
from dash import dcc, html, Input, Output
import plotly.express as px

from src.data.global_data import get_global_water_data
from src.utils.plots import create_earth_choropleth, add_ocean_currents

# Load data
df = get_global_water_data()

# Earth figure
earth_fig = create_earth_choropleth(df)
earth_fig = add_ocean_currents(earth_fig)

# Time-series demo chart
line_fig = px.line(
    x=[2015, 2016, 2017, 2018, 2019, 2020],
    y=[70, 72, 71, 74, 76, 78],
    title="Global Water Quality Trend",
    labels={"x": "Year", "y": "Water Quality Index"},
    template="plotly_dark"
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    style={"backgroundColor": "#0b0f1a", "height": "100vh"},
    children=[

        html.H1(
            "AQUA-GAIA : Global Aquatic Digital Twin",
            style={"textAlign": "center", "color": "white"}
        ),

        html.Div(
            style={"display": "flex", "height": "80vh"},
            children=[

                html.Div(
                    style={"flex": "2"},
                    children=[
                        dcc.Graph(
                            id="earth-map",
                            figure=earth_fig
                        )
                    ]
                ),

                html.Div(
                    style={"flex": "1", "padding": "10px"},
                    children=[
                        html.H3(
                            "Country Water Report",
                            style={"color": "white"}
                        ),
                        html.Div(
                            id="country-report",
                            style={"color": "lightblue", "fontSize": "16px"}
                        ),
                        dcc.Graph(figure=line_fig)
                    ]
                )
            ]
        ),

        html.Footer(
            "Made by Aniket Agarwal | Bachelor of Technology Computer Science | Amity University Punjab",
            style={"textAlign": "center", "color": "gray"}
        )
    ]
)

# Callback for country click
@app.callback(
    Output("country-report", "children"),
    Input("earth-map", "clickData")
)
def update_country_report(clickData):
    if clickData is None:
        return "Click on a country to view water statistics."

    country = clickData["points"][0]["text"]
    row = df[df["Country"] == country].iloc[0]

    return [
        html.P(f"Country: {country}"),
        html.P(f"Water Quality Index: {row['WaterQuality']}"),
        html.P(f"Pollution Level: {row['Pollution']}"),
        html.P(f"Freshwater Availability: {row['FreshwaterAvailability']}")
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
