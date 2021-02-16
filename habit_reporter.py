import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from config import Config
from utils.file_util import FileUtil


class HabitReporter:
    def __init__(self):
        self.config = Config()
        self.config.read_config()

    def make_habit_report_figs(self):
        labels: [str] = self.config.get_labels()
        data_dic = {}
        for label in labels:
            data_dic[label] = {}
        file_paths: [str] = FileUtil.get_recursive_file_paths(self.config.get_base_dir())
        for file_path in file_paths:
            lines = FileUtil.read_lines(file_path)
            for line in lines:
                for label in labels:
                    if label in line:
                        value = HabitReporter.extract_value_float(line)
                        if value is None:
                            continue
                        data_dic[label][HabitReporter.extract_date(file_path)] = value
        figs = []
        for label in labels:
            sorted_tuple = sorted(data_dic[label].items(), key=lambda x:x[0])
            x = [t[0] for t in sorted_tuple]
            y = [t[1] for t in sorted_tuple]
            fig = go.Figure(data=[go.Scatter(x=x, y=y)], layout_title_text=label)
            figs.append(dcc.Graph(id=label, figure=fig))
        return figs

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
    figs = habit_reporter.make_habit_report_figs()
    app = dash.Dash()
    app.layout = html.Div(children=[
        html.H1(children='Daily Report Dashboard'),
        *figs
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
