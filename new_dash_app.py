import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

data = pd.read_csv("archive/combined_stocks.csv")
data["year"] = pd.to_datetime(data["year"], format="%Y")
data.sort_values("year", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Stock Analytics: Understand Your Stocks!"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="", className="header-emoji"),
                html.H1(
                    children="Stock Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of stock prices"
                    " between 2012 and 2021",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Stock", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": region, "value": region}
                                for region in np.sort(data.SC_NAME.unique())
                            ],
                            value="ABB LTD.",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    Output("price-chart", "figure"),
    [
        Input("region-filter", "value"),
    ],
)
def update_charts(region):
    mask = (
        (data.SC_NAME.str.contains(region))
    )
    filtered_data = data.loc[mask, :]
    avg = round(filtered_data['CLOSE'].mean(), 2)
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["year"],
                "y": filtered_data["CLOSE"],
                "type": "lines",
                "hovertemplate": "₹%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": f"{region} stock price of last 10 years.    Average price ₹ {avg}",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "₹", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    return price_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)
