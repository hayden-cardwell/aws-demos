from dash import html, dcc
import dash_ag_grid as dag
import plotly.express as px
from data import df_grid, df_chart


def get_layout():
    return html.Div(
        [
            html.H1(
                "AWS Resource Dashboard", style={"textAlign": "center", "color": "#333"}
            ),
            html.Div(
                [
                    html.H2("EC2 Instances", style={"color": "#555"}),
                    dag.AgGrid(
                        id="ag-grid",
                        rowData=df_grid.to_dict("records"),
                        columnDefs=[
                            {"headerName": "Instance ID", "field": "Instance ID"},
                            {"headerName": "Instance Type", "field": "Instance Type"},
                            {"headerName": "Region", "field": "Region"},
                            {"headerName": "State", "field": "State"},
                        ],
                        defaultColDef={
                            "sortable": True,
                            "filter": True,
                            "resizable": True,
                        },
                        style={"height": 200, "width": "100%"},
                        className="ag-theme-alpine-dark",
                    ),
                ],
                style={
                    "marginBottom": 40,
                    "padding": "20px",
                    "border": "1px solid #ddd",
                    "borderRadius": "5px",
                },
            ),
            html.Div(
                [
                    html.H2("S3 Bucket Analysis", style={"color": "#555"}),
                    dcc.Graph(
                        id="example-chart",
                        figure=px.scatter(
                            df_chart,
                            x="Number of Objects",
                            y="Total Size (GB)",
                            color="Bucket Name",
                            title="S3 Bucket Object Count vs. Size",
                        ).update_layout(template="plotly_dark"),
                    ),
                ],
                style={
                    "padding": "20px",
                    "border": "1px solid #ddd",
                    "borderRadius": "5px",
                },
            ),
        ],
        style={
            "fontFamily": "Arial, sans-serif",
            "padding": "20px",
            "backgroundColor": "#e9ecef",
        },
    )
