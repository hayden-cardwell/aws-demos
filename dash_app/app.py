from flask import Flask
import dash
from layout import get_layout

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname="/",
    external_stylesheets=[
        "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/flatly/bootstrap.min.css"
    ],
)

app.layout = get_layout()

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
