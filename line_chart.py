import dash
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

import dash_core_components as dcc


class LineChart:
    def __init__(self):
        pass

    @staticmethod
    def make_line_chart(x, y, layout_title_text) -> go.Figure:
        return go.Figure(data=[go.Scatter(x=x, y=y)], layout_title_text=layout_title_text)


def main():
    line_chart = LineChart()
    x = np.arange(50)
    y = np.random.randint(100, size=(50,))
    fig = line_chart.make_line_chart(x, y, "Line Chart")
    app = dash.Dash()
    app.layout = html.Div(children=[
        dcc.Graph(id="lineChart", figure=fig)
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
