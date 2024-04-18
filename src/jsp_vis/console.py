import itertools
import shutil

import matplotlib
import numpy as np
import pandas as pd

import logging

log = logging.getLogger(__name__)

CEND = "\33[0m"


def rgb_color_sequence(r: int | float, g: int | float, b: int | float,
                       *, format_type: str = 'foreground') -> str:
    """
    generates a color-codes, that change the color of text in console outputs.

    rgb values must be numbers between 0 and 255 or 0.0 and 1.0.

    :param r:               red value.
    :param g:               green value
    :param b:               blue value

    :param format_type:     specifies weather the foreground-color or the background-color shall be adjusted.
                            valid options: 'foreground','background'
    :return:                a string that contains the color-codes.
    """
    # type: ignore # noqa: F401
    if format_type == 'foreground':
        f = '\033[38;2;{};{};{}m'.format  # font rgb format
    elif format_type == 'background':
        f = '\033[48;2;{};{};{}m'.format  # font background rgb format
    else:
        raise ValueError(f"format {format_type} is not defined. Use 'foreground' or 'background'.")
    rgb = [r, g, b]

    if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
        if min(rgb) < 0 and max(rgb) > 255:
            raise ValueError("rgb values must be numbers between 0 and 255 or 0.0 and 1.0")
        return f(r, g, b)
    if isinstance(r, float) and isinstance(g, float) and isinstance(b, float):
        if min(rgb) < 0 and max(rgb) > 1:
            raise ValueError("rgb values must be numbers between 0 and 255 or 0.0 and 1.0")
        return f(*[int(n * 255) for n in [r, g, b]])


def wrap_with_color_codes(s: object, /, r: int | float, g: int | float, b: int | float, **kwargs) \
        -> str:
    """
    stringify an object and wrap it with console color codes. It adds the color control sequence in front and one
    at the end that resolves the color again.

    rgb values must be numbers between 0 and 255 or 0.0 and 1.0.

    :param s: the object to stringify and wrap
    :param r: red value.
    :param g: green value.
    :param b: blue value.
    :param kwargs: additional argument for the 'DisjunctiveGraphJspVisualizer.rgb_color_sequence'-method.
    :return:
    """
    return f"{rgb_color_sequence(r, g, b, **kwargs)}" \
           f"{s}" \
           f"{CEND}"


def gantt_chart_console(df: pd.DataFrame, n_machines: int, c_map="rainbow") -> None:
    """
    console version of the `gantt_chart_rgb_array`-method. prints a gant chart to the console.
    the parameters need to follow the plotly specification.
    see: https://plotly.com/python/gantt/ or `gantt_chart_rgb_array`

    :param df:      dataframe according to `plotly` specification (https://plotly.com/python/gantt/).

    :return:        a `plotly` gantt chart as rgb array.

    color example

        import numpy as np

        c_map = plt.cm.get_cmap("jet")  # select the desired cmap
        arr = np.linspace(0, 1, 10)  # create a list with numbers from 0 to 1 with n items
        colors = {resource: c_map(val) for resource, val in enumerate(arr)}
    """
    w, h = shutil.get_terminal_size((80, 20))  # enable emulate output in terminal ...

    c_map = matplotlib.colormaps.get_cmap(c_map)  # select the desired cmap
    arr = np.linspace(0, 1, n_machines)  # create a list with numbers from 0 to 1 with n items
    machine_colors = {m_id: c_map(val) for m_id, val in enumerate(arr)}
    colors = {f"Machine {m_id}": (r, g, b) for m_id, (r, g, b, a) in machine_colors.items()}

    if len(df) > 0:
        machines = sorted(df['Resource'].unique())
        jobs = df['Task'].unique()
        jobs.sort()
    else:
        jobs, machines = None, None

    len_prefix = 10
    len_suffix = 15

    x_pixels = w - len_prefix - len_suffix
    x_max = df['Finish'].max() + 1 if len(df) > 0 else x_pixels
    if x_pixels < 0:
        log.warn("terminal window to small")
        return

    x_axis_tick_small = "╤════"
    x_axis_tick_big = "╦════"
    len_tick = len(x_axis_tick_big)
    num_hole_ticks = x_pixels // len_tick
    len_last_tick = x_pixels % len_tick
    x_axis = "".join([
        f"{'':<{len_prefix - 1}}╚",
        *[x_axis_tick_big if i % 5 == 0 else x_axis_tick_small for i in range(num_hole_ticks)],
        "═" * len_last_tick + "╝"
    ])
    x_chart_frame_top = "".join([
        f"{'':<{len_prefix - 1}}╔",
        "═" * x_pixels,
        "╗"
    ])

    x_interval_increment5 = x_max / num_hole_ticks
    x_interval_increment1 = x_max / x_pixels

    x_axis_label = "".join([
        f"{'':<{len_prefix}}",
        *[
            f"{f'{i * x_interval_increment5:.1f}':<5}" if i % 5 == 0 else f"{'':<5}"
            for i in range(num_hole_ticks)
        ]
    ])

    rows = []
    if len(df) > 0:
        for j, m in itertools.zip_longest(jobs, machines):
            matching_tasks = df.loc[df['Task'] == j].iterrows()
            chart_str = [i * x_interval_increment1 for i in range(x_pixels)]
            for _, (_, start, finish, resource) in matching_tasks:
                chart_str = [
                    f"{rgb_color_sequence(*colors[resource])}█"
                    if not isinstance(v, str) and start <= v <= finish else v for v in chart_str
                ]
            prefix = f"{f'{j}':<{len_prefix - 1}}║" if j else f"{'':<{len_prefix - 1}}║"
            colored_block = wrap_with_color_codes("█", *colors[m]) if m else None
            suffix = f"{f'║ {m}':<{len_suffix - 1}}" + f"{colored_block}" if m else f"{f'║':<{len_suffix}}"

            chart_str = [" " if not isinstance(v, str) else v for v in chart_str]
            chart_str = "".join(chart_str)
            rows.append(f"{prefix}{chart_str}{CEND}{suffix}")
    else:
        rows = ["".join([f"{f'':<{len_prefix - 1}}║", " " * x_pixels, "║"])]

    gant_str = "\n".join([
        x_chart_frame_top,
        *rows,
        x_axis,
        x_axis_label
    ])
    print(gant_str)


def graph_console(df: pd.DataFrame, jsp_instance: np.ndarray, c_map="rainbow"):
    w, _ = shutil.get_terminal_size((80, 20))
    _, n_jobs, n_machines = jsp_instance.shape

    len_prefix = 10
    len_suffix = 15

    machine_order = jsp_instance[0]

    if w < 2 * n_jobs + len_prefix + len_suffix:
        log.warning("terminal window to small")
        return

    c_map = matplotlib.colormaps.get_cmap(c_map)  # select the desired cmap
    arr = np.linspace(0, 1, n_machines)  # create a list with numbers from 0 to 1 with n items
    machine_colors = {m_id: c_map(val) for m_id, val in enumerate(arr)}
    colors = {f"Machine {m_id}": (r, g, b) for m_id, (r, g, b, a) in machine_colors.items()}

    machine_strings = [
        f"{m :>{len_suffix - 5}} {wrap_with_color_codes('█', r, g, b)}"
        for m, (r, g, b) in colors.items()
    ]

    def task_is_in_df(job: int, machine: int):
        return any((df['Task'] == f"Job {job}") & (df['Resource'] == f"Machine {machine}"))
        pass

    for j, m_str in itertools.zip_longest(range(n_jobs), machine_strings):
        row = f"Job {j}" if j is not None else ""
        row = f"{row:<{len_prefix}}"
        for task_in_job in range(n_machines):

            if j is not None:
                machine_of_task = machine_order[j][task_in_job]
                node_str = "●" if task_is_in_df(job=j, machine=machine_of_task) else "◯"
                node_str = wrap_with_color_codes(node_str, *colors[f"Machine {machine_of_task}"])
                if task_in_job < n_machines - 1:
                    node_str += "-"
            else:
                node_str = " "
                if task_in_job < n_machines - 1:
                    node_str += " "
            row += node_str
        print("".join([row, " " * 4, m_str if m_str is not None else ""]))
