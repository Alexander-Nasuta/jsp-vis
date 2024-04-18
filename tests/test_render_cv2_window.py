import sys

import pytest


@pytest.mark.skipif(sys.platform == 'linux',
                    reason="the Github Actions runner is configured to run on Linux. "
                           "The runner does not have a UI, so the test will fail. ")
def test_render_cv2_window(custom_jsp_instance_df, custom_jsp_n_machines):
    from jsp_vis.cv2_window import render_gantt_in_window

    render_gantt_in_window(
        df=custom_jsp_instance_df,
        n_machines=custom_jsp_n_machines,
        wait=1 # time in ms that the `cv2`-window is open.
        # wait=None # ''None'' will keep the window open till a keyboard occurs.
    )

@pytest.mark.skipif(sys.platform == 'linux',
                    reason="the Github Actions runner is configured to run on Linux. "
                           "The runner does not have a UI, so the test will fail. ")
def test_render_cv2_window(ft06_df, ft06_n_machines):
    from jsp_vis.cv2_window import render_gantt_in_window

    render_gantt_in_window(
        df=ft06_df,
        n_machines=ft06_n_machines,
        wait=1 # time in ms that the `cv2`-window is open.
        # wait=None # ''None'' will keep the window open till a keyboard occurs.
    )