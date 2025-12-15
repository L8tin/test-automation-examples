from python_scripts.common_imports import *
from python_scripts.ui_test_data import *

# Loop Lookups for necessary values
def loop_vars(var_needed: str, var_type: str):
    print(f"[ui_common][loop_vars] var_needed={var_needed}")
    print(f"[ui_common][loop_vars] var_type={var_type}")

    try:
        variable_set = VAR_TYPES[var_type]
    except KeyError:
        raise ValueError(f"[ui_common][loop_vars]Unknown var_type: {var_type}")

    try:
        return variable_set[var_needed]
    except KeyError:
        raise ValueError(
            f"[ui_common][loop_vars] Key '{var_needed}' not found in '{var_type}'"
        )

# Other helper functions
def get_chicago_time():
    print("[ui_common][get_chicago_time]")
    native_dt = datetime.now(timezone('America/Chicago'))
    localFormat="%m%d%Y"
    curr_time = native_dt.strftime(localFormat)
    return(curr_time)

