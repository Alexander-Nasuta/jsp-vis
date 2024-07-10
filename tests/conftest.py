import pytest


@pytest.fixture(scope="function")
def custom_jsp_instance():
    import numpy as np
    custom_jsp_instance = np.array([
        [
            [0, 1, 2, 3],  # job 0
            [0, 2, 1, 3]  # job 1
        ],
        [
            [11, 3, 3, 12],  # task durations of job 0
            [5, 16, 7, 4]  # task durations of job 1
        ]
    ], dtype=np.int32)  # dtype=np.int32 is necessary for the Rust wrapper
    yield custom_jsp_instance


@pytest.fixture(scope="function")
def custom_jsp_instance_df():
    import pandas as pd
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
    yield pd.DataFrame(df)


@pytest.fixture(scope="function")
def custom_jsp_instance_df_named_resources():
    import pandas as pd
    df = [
        {'Task': 'Job 0', 'Start': 5, 'Finish': 16, 'Resource': 'MyCustomMachine 0'},
        {'Task': 'Job 0', 'Start': 28, 'Finish': 31, 'Resource': 'MyCustomMachine 1'},
        {'Task': 'Job 0', 'Start': 31, 'Finish': 34, 'Resource': 'MyCustomMachine 2'},
        {'Task': 'Job 0', 'Start': 34, 'Finish': 46, 'Resource': 'MyCustomMachine 3'},
        {'Task': 'Job 1', 'Start': 0, 'Finish': 5, 'Resource': 'MyCustomMachine 0'},
        {'Task': 'Job 1', 'Start': 5, 'Finish': 21, 'Resource': 'MyCustomMachine 2'},
        {'Task': 'Job 1', 'Start': 21, 'Finish': 28, 'Resource': 'MyCustomMachine 1'},
        {'Task': 'Job 1', 'Start': 28, 'Finish': 32, 'Resource': 'MyCustomMachine 3'}
    ]
    yield pd.DataFrame(df)


@pytest.fixture(scope="function")
def custom_jsp_n_machines():
    yield 4


@pytest.fixture(scope="function")
def ft06():
    import numpy as np
    ft06 = np.array([[[2, 0, 1, 3, 5, 4],
                      [1, 2, 4, 5, 0, 3],
                      [2, 3, 5, 0, 1, 4],
                      [1, 0, 2, 3, 4, 5],
                      [2, 1, 4, 5, 0, 3],
                      [1, 3, 5, 0, 4, 2]],

                     [[1, 3, 6, 7, 3, 6],
                      [8, 5, 10, 10, 10, 4],
                      [5, 4, 8, 9, 1, 7],
                      [5, 5, 5, 3, 8, 9],
                      [9, 3, 5, 4, 3, 1],
                      [3, 3, 9, 10, 4, 1]]
                     ])
    yield ft06


@pytest.fixture(scope="function")
def ft06_df():
    import pandas as pd
    df_ft06 = [
        {'Task': 'Job 0', 'Start': 19, 'Finish': 20, 'Resource': 'Machine 2'},
        {'Task': 'Job 0', 'Start': 66, 'Finish': 69, 'Resource': 'Machine 0'},
        {'Task': 'Job 0', 'Start': 69, 'Finish': 75, 'Resource': 'Machine 1'},
        {'Task': 'Job 0', 'Start': 75, 'Finish': 82, 'Resource': 'Machine 3'},
        {'Task': 'Job 0', 'Start': 88, 'Finish': 91, 'Resource': 'Machine 5'},
        {'Task': 'Job 0', 'Start': 91, 'Finish': 97, 'Resource': 'Machine 4'},
        {'Task': 'Job 1', 'Start': 3, 'Finish': 11, 'Resource': 'Machine 1'},
        {'Task': 'Job 1', 'Start': 14, 'Finish': 19, 'Resource': 'Machine 2'},
        {'Task': 'Job 1', 'Start': 19, 'Finish': 29, 'Resource': 'Machine 4'},
        {'Task': 'Job 1', 'Start': 29, 'Finish': 39, 'Resource': 'Machine 5'},
        {'Task': 'Job 1', 'Start': 39, 'Finish': 49, 'Resource': 'Machine 0'},
        {'Task': 'Job 1', 'Start': 49, 'Finish': 53, 'Resource': 'Machine 3'},
        {'Task': 'Job 2', 'Start': 0, 'Finish': 5, 'Resource': 'Machine 2'},
        {'Task': 'Job 2', 'Start': 5, 'Finish': 9, 'Resource': 'Machine 3'},
        {'Task': 'Job 2', 'Start': 39, 'Finish': 47, 'Resource': 'Machine 5'},
        {'Task': 'Job 2', 'Start': 54, 'Finish': 63, 'Resource': 'Machine 0'},
        {'Task': 'Job 2', 'Start': 63, 'Finish': 64, 'Resource': 'Machine 1'},
        {'Task': 'Job 2', 'Start': 64, 'Finish': 71, 'Resource': 'Machine 4'},
        {'Task': 'Job 3', 'Start': 11, 'Finish': 16, 'Resource': 'Machine 1'},
        {'Task': 'Job 3', 'Start': 49, 'Finish': 54, 'Resource': 'Machine 0'},
        {'Task': 'Job 3', 'Start': 54, 'Finish': 59, 'Resource': 'Machine 2'},
        {'Task': 'Job 3', 'Start': 59, 'Finish': 62, 'Resource': 'Machine 3'},
        {'Task': 'Job 3', 'Start': 71, 'Finish': 79, 'Resource': 'Machine 4'},
        {'Task': 'Job 3', 'Start': 79, 'Finish': 88, 'Resource': 'Machine 5'},
        {'Task': 'Job 4', 'Start': 5, 'Finish': 14, 'Resource': 'Machine 2'},
        {'Task': 'Job 4', 'Start': 16, 'Finish': 19, 'Resource': 'Machine 1'},
        {'Task': 'Job 4', 'Start': 29, 'Finish': 34, 'Resource': 'Machine 4'},
        {'Task': 'Job 4', 'Start': 47, 'Finish': 51, 'Resource': 'Machine 5'},
        {'Task': 'Job 4', 'Start': 63, 'Finish': 66, 'Resource': 'Machine 0'},
        {'Task': 'Job 4', 'Start': 66, 'Finish': 67, 'Resource': 'Machine 3'},
        {'Task': 'Job 5', 'Start': 0, 'Finish': 3, 'Resource': 'Machine 1'},
        {'Task': 'Job 5', 'Start': 67, 'Finish': 70, 'Resource': 'Machine 3'},
        {'Task': 'Job 5', 'Start': 70, 'Finish': 79, 'Resource': 'Machine 5'},
        {'Task': 'Job 5', 'Start': 79, 'Finish': 89, 'Resource': 'Machine 0'},
        {'Task': 'Job 5', 'Start': 97, 'Finish': 101, 'Resource': 'Machine 4'},
        {'Task': 'Job 5', 'Start': 101, 'Finish': 102, 'Resource': 'Machine 2'}
    ]
    yield pd.DataFrame(df_ft06)


@pytest.fixture(scope="function")
def ft06_n_machines():
    yield 6
