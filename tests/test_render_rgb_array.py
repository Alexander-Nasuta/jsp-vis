import numpy as np


def test_rgb_array_custom_jsp_instance(custom_jsp_instance_df, custom_jsp_n_machines):
    from jsp_vis.rgb_array import gantt_chart_rgb_array

    vis = gantt_chart_rgb_array(custom_jsp_instance_df, custom_jsp_n_machines)
    assert type(vis) == type(np.array([]))
    assert vis.shape == (400, 600, 3)


def test_rgb_array_ft06(ft06_df, ft06_n_machines):
    from jsp_vis.rgb_array import gantt_chart_rgb_array

    vis = gantt_chart_rgb_array(ft06_df, ft06_n_machines)
    assert type(vis) == type(np.array([]))
    assert vis.shape == (400, 600, 3)
