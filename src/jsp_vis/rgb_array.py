import cv2

import pandas as pd
import numpy as np

import matplotlib as mpl
import plotly.graph_objects as go


def _gantt_figure(df: pd.DataFrame, colors: dict, *,
                  index_col: str = 'Resource',
                  show_colorbar: bool = True,
                  group_tasks: bool = True,
                  bar_width: float = 0.2,
                  title: str = "Gantt Chart") -> go.Figure:
    """
    builds a plotly gantt chart.

    this is a re-implementation of `plotly.figure_factory.create_gantt` (with `colors` given as dict),
    which has been removed in plotly 7.

    :param df:              dataframe with the columns `Task`, `Start`, `Finish` and `index_col`.
    :param colors:          maps every value of `index_col` to a rgb tuple with values in [0, 1].
    :param index_col:       the column that determines the color of a bar.
    :param show_colorbar:   whether to show a legend for the values of `index_col`.
    :param group_tasks:     if `True`, all rows with the same `Task` are drawn in the same row of the chart.
    :param bar_width:       half the height of a bar.
    :param title:           the title of the chart.

    :return:                a `plotly` figure.
    """
    for col in ("Task", "Start", "Finish", index_col):
        if col not in df.columns:
            raise ValueError(f"the dataframe has no column '{col}'.")

    records = df.to_dict("records")

    missing = {r[index_col] for r in records} - set(colors)
    if missing:
        raise ValueError(f"no color specified for the following values of '{index_col}': {sorted(missing)}")

    # the order of the rows (bottom to top). tasks that appear first in the dataframe are shown at the top.
    if group_tasks:
        task_names = list(dict.fromkeys(r["Task"] for r in records))[::-1]
    else:
        task_names = [r["Task"] for r in records]

    # one filled scatter trace (consisting of rectangles separated by gaps) per index value
    traces = {}
    for row_idx, r in enumerate(records):
        y = task_names.index(r["Task"]) if group_tasks else row_idx
        x0, x1 = r["Start"], r["Finish"]
        y0, y1 = y - bar_width, y + bar_width
        key = r[index_col]
        trace = traces.setdefault(key, {"x": [], "y": []})
        if trace["x"]:
            # a gap separates the rectangles from each other
            trace["x"].append(trace["x"][-1])
            trace["y"].append(None)
        trace["x"] += [x0, x1, x1, x0]
        trace["y"] += [y0, y0, y1, y1]

    data = []
    for key in sorted(traces):
        r, g, b = colors[key][:3]
        rgb = f"rgb({r * 255:.0f}, {g * 255:.0f}, {b * 255:.0f})"
        data.append(go.Scatter(
            x=traces[key]["x"],
            y=traces[key]["y"],
            mode="none",
            fill="toself",
            fillcolor=rgb,
            hoverinfo="name",
            name=str(key),
            legendgroup=str(key),
        ))
    # invisible markers at the start- and endpoints of the bars (pads the x-axis like the original `create_gantt`)
    for key in sorted(traces):
        xs = [x for x, y in zip(traces[key]["x"], traces[key]["y"]) if y is not None]
        ys = [y for y in traces[key]["y"] if y is not None]
        data.append(go.Scatter(
            x=xs,
            y=ys,
            mode="markers",
            marker=dict(size=1, opacity=0),
            hoverinfo="skip",
            showlegend=False,
            legendgroup=str(key),
        ))

    layout = dict(
        title=title,
        showlegend=show_colorbar,
        hovermode="closest",
        yaxis=dict(
            showgrid=False,
            ticktext=task_names,
            tickvals=list(range(len(task_names))),
            range=[-1, len(task_names) + 1],
            autorange=False,
            zeroline=False,
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
        ),
    )
    return go.Figure(data=data, layout=layout)


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

    # size of the image in pixels
    width, height = int(width * dpi), int(height * dpi)

    # Gantt chart
    if not len(df):
        df = pd.DataFrame([{"Task": "Job 0", "Start": 0, "Finish": 0, "Resource": "Machine 0"}])
    fig = _gantt_figure(df=df, colors=colors, show_colorbar=show_colorbar, index_col=index_col,
                        group_tasks=group_tasks)
    fig.update_layout(xaxis_type=xaxis_type)

    img_str = fig.to_image(format="jpg", width=width, height=height)

    nparr = np.frombuffer(img_str, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR in OpenCV 3.1
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img
