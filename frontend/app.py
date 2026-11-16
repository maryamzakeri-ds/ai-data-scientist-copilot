from dash import Dash
import dash_bootstrap_components as dbc
from layouts import layout
from callbacks import register_callbacks

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = layout

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)