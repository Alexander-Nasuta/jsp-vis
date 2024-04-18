from jsp_vis.cv2_window import render_gantt_in_window
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame([
        {'Task': 'Job 0', 'Start': 5, 'Finish': 16, 'Resource': 'Machine 0'},
        {'Task': 'Job 0', 'Start': 28, 'Finish': 31, 'Resource': 'Machine 1'},
        {'Task': 'Job 0', 'Start': 31, 'Finish': 34, 'Resource': 'Machine 2'},
        {'Task': 'Job 0', 'Start': 34, 'Finish': 46, 'Resource': 'Machine 3'},
        {'Task': 'Job 1', 'Start': 0, 'Finish': 5, 'Resource': 'Machine 0'},
        {'Task': 'Job 1', 'Start': 5, 'Finish': 21, 'Resource': 'Machine 2'},
        {'Task': 'Job 1', 'Start': 21, 'Finish': 28, 'Resource': 'Machine 1'},
        {'Task': 'Job 1', 'Start': 28, 'Finish': 32, 'Resource': 'Machine 3'}
    ])
    num_of_machines = 4

    render_gantt_in_window(
        df=df,
        n_machines=num_of_machines,
        wait=None  # time in ms that the `cv2`-window is open.
        # wait=None # ''None'' will keep the window open till a keyboard occurs.
    )