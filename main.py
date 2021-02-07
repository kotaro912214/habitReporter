import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import glob

DAILY_REPORT_PATH = '/Users/kotaro-seki/Documents/my-knowledge/report/daily/'
TAG_PATH = './tags.txt'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def main():
    tags = read_data(TAG_PATH)
    data_dic = {}
    date_dic = {}
    for tag in tags:
        data_dic[tag] = []
        date_dic[tag] = []
    file_paths = glob.glob(DAILY_REPORT_PATH + '*')
    file_paths.sort()
    for file_path in file_paths:
        lines = read_data(file_path)
        for line in lines:
            for tag in tags:
                if tag in line:
                    value = extract_value_float(line)
                    date_dic[tag].append(extract_date(file_path))
                    data_dic[tag].append(value)
    graphs = []
    for tag in tags:
        fig = go.Figure(data=[go.Scatter(x=date_dic[tag], y=data_dic[tag])], layout_title_text=tag)
        graphs.append(dcc.Graph(id=tag, figure=fig))

    app.layout = html.Div(children=[
        html.H1(children='Daily Report Dashboard'),
        *graphs
    ])


def read_data(file_path) -> [str]:
    with open(file_path, 'r') as f:
        return list(map(lambda s: s.strip(), f.readlines()))


def extract_value_float(data) -> float:
    strings = data.split()
    float_value = None
    for string in strings:
        if '#' not in string:
            try:
                float_value = float(string)
            except ValueError:
                return float_value
    return float_value


def extract_date(file_path) -> str:
    file_names = file_path.split('/')
    return file_names[-1].split('.')[0]


if __name__ == '__main__':
    main()
    app.run_server(debug=True)
