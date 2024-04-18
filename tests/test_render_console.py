import pandas as pd

from jsp_vis.console import gantt_chart_console, graph_console


def test_gantt_console(custom_jsp_instance_df, custom_jsp_n_machines):
    gantt_chart_console(pd.DataFrame(custom_jsp_instance_df), custom_jsp_n_machines)


def test_gantt_console_ft06(ft06_df, ft06_n_machines):
    gantt_chart_console(pd.DataFrame(ft06_df), ft06_n_machines)


def test_graph_console(custom_jsp_instance, custom_jsp_instance_df):
    graph_console(
        df=pd.DataFrame(custom_jsp_instance_df),
        jsp_instance=custom_jsp_instance,
    )


def test_graph_console_ft06(ft06, ft06_df):
    graph_console(
        df=pd.DataFrame(ft06_df),
        jsp_instance=ft06,
    )
