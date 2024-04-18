

<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
   <!--
  <a href="https://cybernetics-lab.de/">
    <img src="https://github.com/Alexander-Nasuta/graph-jsp-env/raw/master/resources/readme_images/logo.png" alt="Logo" height="80">
  </a>
   -->

  <h1 align="center">
     Job Shop Scheduling Problem Visualisations
  </h1>

   
   <a>
    <img src="https://raw.githubusercontent.com/Alexander-Nasuta/jsp-vis/main/resources/ft06_console.gif" alt="Logo" height="180">
  </a>


</div>


- **Github**: https://github.com/Alexander-Nasuta/jsp-vis

- **PyPi**: https://pypi.org/project/jsp-vis/


# About The Project
Ths project provides visualisation for the Job Shop Scheduling Problem (JSP).
This is focused on Gantt charts. The input date for the visualisation is inspired by [plotly's Gantt chart api](https://plotly.com/python/gantt/). 
`jsp-vis` is a standalone package and in designed to be used in combination with a JSP-reinforcement learning environments that follow the [Gymnasium Environment](https://gymnasium.farama.org/) standard.
The render function of the environment can be used to render the Gantt chart.
Typically the render function can implement different modes like `human`, `rgb_array` or `ansi` rendering.
The `jsp-vis` package offers three different visualisations: console visualisation, rgb_array visualisation and window visualisation.
The window visualisation is essentially only rendering the rgb_array visualisation in a window using OpenCV.
The console visualisation might be used for the `asni` mode of a render function, the rgb_array visualisation for the `rgb_array` mode and the window visualisation for the `human` mode.

# Installation

Install the package with pip:
```
   pip install todo
```

# Minimal Working Example: console visualisation

```python
from jsp_vis.console import gantt_chart_console
import pandas as pd

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

gantt_chart_console(df, num_of_machines)
```
The code above will render the following Gantt chart in the console:

![](https://raw.githubusercontent.com/Alexander-Nasuta/jsp-vis/main/resources/example_console.png)

# Minimal Working Example: console visualisation

```python
from jsp_vis.cv2_window import render_gantt_in_window
import pandas as pd

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
        wait=2000 # time in ms that the `cv2`-window is open.
        # wait=None # ''None'' will keep the window open till a keyboard occurs.
    )
```

The code above will render the following Gantt chart in the console:

![](https://raw.githubusercontent.com/Alexander-Nasuta/jsp-vis/main/resources/example_window.png)


# More Examples
For more examples you can have a look at the test files in the `tests` directory.
Every visualisation has its own test file and is tested on two different jsp instances defined in the `conftest.py`.

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- MARKDOWN LINKS & IMAGES todo: add Github, Linked in etc.-->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[screenshot]: resources/readme_images/screenshot.png


