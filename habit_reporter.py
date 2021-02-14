import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils.file_util import FileUtil


class HabitReporter:
    def __init__(self):
        pass

    def make_habit_report_figs(self):
        TAG_PATH = './tags.txt'
        DAILY_REPORT_PATH = '/Users/kotaro-seki/Documents/my-knowledge/report/daily'
        tags: [str] = FileUtil.read_lines(TAG_PATH)
        data_dic = {}
        date_dic = {}
        for tag in tags:
            data_dic[tag] = []
            date_dic[tag] = []
        file_paths: [str] = FileUtil.get_recursive_file_paths(DAILY_REPORT_PATH)
        file_paths.sort()
        for file_path in file_paths:
            lines = FileUtil.read_lines(file_path)
            for line in lines:
                for tag in tags:
                    if tag in line:
                        value = HabitReporter.extract_value_float(line)
                        date_dic[tag].append(HabitReporter.extract_date(file_path))
                        data_dic[tag].append(value)
        figs = []
        for tag in tags:
            fig = go.Figure(data=[go.Scatter(x=date_dic[tag], y=data_dic[tag])], layout_title_text=tag)
            figs.append(dcc.Graph(id=tag, figure=fig))
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
