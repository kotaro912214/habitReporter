import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

from config import Config
from grass_chart import GrassChart
from line_chart import LineChart
from utils.file_util import FileUtil


class HabitReporter:
    def __init__(self):
        self.config = Config()
        self.config.read_config()

    def make_habit_report_figs(self) -> [dcc.Graph]:
        labels = self.config.get_labels()
        date_value_dic = self.make_date_value_dic()
        figs = []
        for label in labels:
            x = list(date_value_dic[label].keys())
            y = list(date_value_dic[label].values())
            if self.config.is_binary(label):
                z = np.random.randint(10, size=(365,))
                fig = GrassChart.make_glass_fig(z=z, is_binary=True, title=label)
            else:
                fig = LineChart.make_line_chart(x, y, label)
            figs.append(dcc.Graph(id=label, figure=fig))
        return figs

    def make_date_value_dic(self) -> dict:
        labels = self.config.get_labels()
        data_dic = {}
        for label in labels:
            data_dic[label] = {}
        file_paths = FileUtil.get_recursive_file_paths(self.config.get_base_dir())
        file_paths.sort(key=lambda x: x.split("/")[-1])
        for file_path in file_paths:
            lines = FileUtil.read_lines(file_path)
            for line in lines:
                for label in labels:
                    if label not in line:
                        continue
                    value = HabitReporter.extract_value_float(line)
                    if value is None:
                        continue
                    data_dic[label][HabitReporter.extract_date(file_path)] = value
        return data_dic

    @staticmethod
    def extract_value_float(line) -> float:
        strings = line.split()
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
        file_name = file_path.split('/')[-1]
        return file_name.split('.')[0]


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
