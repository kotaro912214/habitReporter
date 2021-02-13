import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go


def main():
    fig = display_year()
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(id='heatmap-test', figure=fig)
    ])
    app.run_server(debug=True)


def display_year():
    year = datetime.date.today().year
    data = np.random.randint(2, size=(365,))

    d1 = datetime.date(year, 1, 1)
    d2 = datetime.date(year, 12, 31)

    delta = d2 - d1

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_positions = (np.cumsum(month_days) - 15) / 7

    dates_in_year = [d1 + datetime.timedelta(i) for i in
                     range(delta.days + 1)]
    # gives me a list with datetimes for each day a year
    weekdays_in_year = [i.weekday() for i in
                        dates_in_year]
    # gives [0,1,2,3,4,5,6,0,1,2,3,4,5,6,…] (ticktext in xaxis dict translates this to weekdays

    week_number_of_dates = []
    for date in dates_in_year:
        week_number = date.strftime("%V")
        if week_number == "53" and date.month == 1:
            week_number = "00"
        week_number_of_dates.append(week_number)

    text = [str(i) for i in
            dates_in_year]
    # gives something like list of strings like ‘2018-01-25’ for each date. Used in data trace to make good hovertext.
    # 4cc417 green #347c17 dark green
    # color_scale = [[False, '#eeeeee'], [True, '#76cf63']]
    color_scale = [
        [0, '#eee'],
        [0.5, '#666'],
        [1.0, '#000']
    ]
    # color_scale = [
    #     [0, "rgb(235, 237, 240)"],
    #     [0.1, "rgb(240, 255, 244)"],
    #
    #     [0.1, "rgb(220, 255, 228)"],
    #     [0.2, "rgb(220, 255, 228)"],
    #
    #     [0.2, "rgb(190, 245, 203)"],
    #     [0.3, "rgb(190, 245, 203)"],
    #
    #     [0.3, "rgb(133, 232, 157)"],
    #     [0.4, "rgb(133, 232, 157)"],
    #
    #     [0.4, "rgb(52, 208, 88)"],
    #     [0.5, "rgb(52, 208, 88)"],
    #
    #     [0.5, "rgb(40, 167, 69)"],
    #     [0.6, "rgb(40, 167, 69)"],
    #
    #     [0.6, "rgb(34, 134, 58)"],
    #     [0.7, "rgb(34, 134, 58)"],
    #
    #     [0.7, "rgb(23, 111, 44)"],
    #     [0.8, "rgb(23, 111, 44)"],
    #
    #     [0.8, "rgb(22, 92, 38)"],
    #     [0.9, "rgb(22, 92, 38)"],
    #
    #     [0.9, "rgb(20, 70, 32)"],
    #     [1.0, "rgb(20, 70, 32)"]
    # ]


    # handle end of year

    data = [
        go.Heatmap(
            x=week_number_of_dates,
            y=weekdays_in_year,
            z=data,
            text=text,
            hoverinfo='text',
            xgap=3,
            ygap=3,
            showscale=False,
            colorscale=color_scale
        )
    ]

    layout = go.Layout(
        title='activity chart',
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
    fig = go.Figure(data=data, layout=layout)
    return fig


if __name__ == '__main__':
    main()
