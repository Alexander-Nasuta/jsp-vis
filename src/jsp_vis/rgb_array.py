import cv2

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.figure_factory as ff


def gantt_chart_rgb_array(df: pd.DataFrame, n_machines: int, *,
                          c_map="rainbow",
                          dpi=80,
                          width=7.5,
                          height=5,
                          show_colorbar=True,
                          index_col='Resource',
                          group_tasks=True,
                          xaxis_type='linear') -> np.ndarray:
    c_map = mpl.colormaps.get_cmap(c_map)  # select the desired cmap
    arr = np.linspace(0, 1, n_machines)  # create a list with numbers from 0 to 1 with n items
    machine_colors = {m_id: c_map(val) for m_id, val in enumerate(arr)}
    colors = {f"Machine {m_id}": (r, g, b) for m_id, (r, g, b, a) in machine_colors.items()}

    plt.figure(dpi=dpi)
    plt.axis("off")
    plt.tight_layout()

    fig = mpl.pyplot.gcf()
    fig.set_size_inches(width, height)

    # Gantt chart
    width, height = fig.canvas.get_width_height()
    if not len(df):
        df = pd.DataFrame([{"Task": "Job 0", "Start": 0, "Finish": 0, "Resource": "Machine 0"}])
    fig = ff.create_gantt(df=df, show_colorbar=show_colorbar, index_col=index_col, group_tasks=group_tasks,
                          colors=colors)
    fig.update_layout(xaxis_type=xaxis_type)

    img_str = fig.to_image(format="jpg", width=width, height=height)

    nparr = np.frombuffer(img_str, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR in OpenCV 3.1
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # clear current frame
    plt.clf()
    plt.close('all')
    return img