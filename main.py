import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import os
import glob


class HabitReporter:
    def __init__(self):
        pass

    def show_habit_reporter(self):
        TAG_PATH = './tags.txt'
        tags = HabitReporter.read_data(TAG_PATH)
        data_dic = {}
        date_dic = {}
        for tag in tags:
            data_dic[tag] = []
            date_dic[tag] = []
        file_paths = HabitReporter.get_file_paths()
        file_paths.sort()
        for file_path in file_paths:
            lines = HabitReporter.read_data(file_path)
            for line in lines:
                for tag in tags:
                    if tag in line:
                        value = HabitReporter.extract_value_float(line)
                        date_dic[tag].append(HabitReporter.extract_date(file_path))
                        data_dic[tag].append(value)
        graphs = []
        for tag in tags:
            fig = go.Figure(data=[go.Scatter(x=date_dic[tag], y=data_dic[tag])], layout_title_text=tag)
            graphs.append(dcc.Graph(id=tag, figure=fig))
        app = dash.Dash()
        app.layout = html.Div(children=[
            html.H1(children='Daily Report Dashboard'),
            *graphs
        ])
        app.run_server(debug=True)


    @staticmethod
    def get_file_paths() -> [str]:
        file_paths = []
        DAILY_REPORT_PATH = '/Users/kotaro-seki/Documents/my-knowledge/report/daily/'
        unknown_paths = glob.glob(DAILY_REPORT_PATH + '*')
        while len(unknown_paths) > 0:
            for i, unknown_path in enumerate(unknown_paths):
                if os.path.isdir(unknown_path):
                    unknown_paths += glob.glob(unknown_path + '/*')
                else:
                    file_paths.append(unknown_path)
                unknown_paths = unknown_paths[:i] + unknown_paths[i + 1:]
        return file_paths

    @staticmethod
    def read_data(file_path) -> [str]:
        with open(file_path, 'r') as f:
            return list(map(lambda s: s.strip(), f.readlines()))

    @staticmethod
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

    @staticmethod
    def extract_date(file_path) -> str:
        file_names = file_path.split('/')
        return file_names[-1].split('.')[0]


def main():
    habit_reporter = HabitReporter()
    habit_reporter.show_habit_reporter()


if __name__ == '__main__':
    main()
