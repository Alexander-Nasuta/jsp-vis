import cv2
import signal
import threading


import pandas as pd
import numpy.typing as npt

from jsp_vis.rgb_array import gantt_chart_rgb_array


def handler_stop_signals(*_) -> None:
    """
    closes all `cv2`-windows when the process is killed
    """
    cv2.destroyAllWindows()

if threading.current_thread() is threading.main_thread():
    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)



def render_rgb_array(vis: npt.NDArray, *, window_title: str = "Job Shop Scheduling", wait: int = 1) -> None:
    """
    renders a rgb-array in an `cv2` window.
    the window will remain open for `:param wait:` ms or till the user presses any key.

    :param vis:             the rgb-array to render.
    :param window_title:    the title of the `cv2`-window
    :param wait:            time in ms that the `cv2`-window is open.
                            if `None`, then the window will remain open till a keyboard occurs.

    :return:
    """
    vis = cv2.cvtColor(vis, cv2.COLOR_RGB2BGR)
    cv2.imshow(window_title, vis)
    # https://stackoverflow.com/questions/64061721/opencv-to-close-the-window-on-a-specific-key
    k = cv2.waitKey(wait) & 0xFF
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


def render_gantt_in_window(df: pd.DataFrame, *, n_machines: int, gantt_chart_rgb_array_kwargs: dict | None =None,
                           **render_kwargs: dict) -> None:
    """
    wrapper for the `gantt_chart_rgb_array`- and `render_rgb_array`-methods

    :param df:              parameter for `gantt_chart_rgb_array`
    :param n_machines:          parameter for `gantt_chart_rgb_array`
    :param render_kwargs:   additional parameters for `render_rgb_array`

    :return:                None
    """
    if gantt_chart_rgb_array_kwargs is None:
        gantt_chart_rgb_array_kwargs = {}
    vis = gantt_chart_rgb_array(df=df, n_machines=n_machines, **gantt_chart_rgb_array_kwargs)
    render_rgb_array(vis, **render_kwargs)


if __name__ == '__main__':
    df = [
        {'Task': 'Job 0', 'Start': 5, 'Finish': 16, 'Resource': 'Machine 0'},
        {'Task': 'Job 0', 'Start': 28, 'Finish': 31, 'Resource': 'Machine 1'},
        {'Task': 'Job 0', 'Start': 31, 'Finish': 34, 'Resource': 'Machine 2'},
        {'Task': 'Job 0', 'Start': 34, 'Finish': 46, 'Resource': 'Machine 3'},
        {'Task': 'Job 1', 'Start': 0, 'Finish': 5, 'Resource': 'Machine 0'},
        {'Task': 'Job 1', 'Start': 5, 'Finish': 21, 'Resource': 'Machine 2'},
        {'Task': 'Job 1', 'Start': 21, 'Finish': 28, 'Resource': 'Machine 1'},
        {'Task': 'Job 1', 'Start': 28, 'Finish': 32, 'Resource': 'Machine 3'}
    ]
    render_gantt_in_window(pd.DataFrame(df), n_machines=4, wait=None)
