import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

from utils.date_util import DateUtil


class GrassChart:
    def __init__(self):
        pass

    @staticmethod
    def make_glass_fig(z, is_binary, title):
        dates_in_year = DateUtil.make_dates_in_year()
        weekdays_in_year = [i.weekday() for i in dates_in_year]
        week_number_of_dates = GrassChart.make_week_number_of_dates(dates_in_year)
        text = [str(i) for i in dates_in_year]
        color_scale = [[False, "#EAEDF0"], [True, "#C7E48B"]] if is_binary else [
            [0, "#EAEDF0"],
            [0.2, "#C7E48B"],
            [1.0, "#1D6922"]
        ]

        data = [
            go.Heatmap(
                x=week_number_of_dates,
                y=weekdays_in_year,
                z=z,
                text=text,
                hoverinfo='text',
                xgap=3,
                ygap=3,
                showscale=False,
                colorscale=color_scale,
                zmin=0,
                zmax=1,
                zauto=False
            )
        ]

        layout = GrassChart.make_layout(title)
        fig = go.Figure(data=data, layout=layout)
        return fig

    @staticmethod
    def make_week_number_of_dates(dates_in_year):
        week_number_of_dates = []
        for date in dates_in_year:
            week_number = date.strftime("%V")
            if week_number == "53" and date.month == 1:
                week_number = "00"
            week_number_of_dates.append(week_number)
        return week_number_of_dates

    @staticmethod
    def make_layout(title):
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month_positions = (np.cumsum(month_days) - 15) / 7
        return go.Layout(
            title=title,
            height=250,
            yaxis=dict(
                showline=False, showgrid=False, zeroline=False,
                tickmode='array',
                ticktext=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                tickvals=[0, 1, 2, 3, 4, 5, 6],
                autorange="reversed"
            ),
            xaxis=dict(
                showline=False, showgrid=False, zeroline=False,
                tickmode='array',
                ticktext=month_names,
                tickvals=month_positions
            ),
            font={'size': 10, 'color': '#9e9e9e'},
            plot_bgcolor='#fff',
            margin=dict(t=40),
            showlegend=False
        )


def main():
    z = np.random.randint(10, size=(365,))
    is_binary = False
    title = "Glass Chart"
    glass_chart = GrassChart()
    fig = glass_chart.make_glass_fig(z, is_binary, title)
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(id='heatmap', figure=fig)
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
