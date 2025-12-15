from python_scripts import ui_test_data
from python_scripts import common_imports

def test_answer(result, expected):
    print("[ui_verifications][test_answer] ")
    wordsthatmatter = result.split('.')
    wordsthatactuallymatter = wordsthatmatter[0]
    print(f"[ui_verifications][test_answer] -| {wordsthatactuallymatter} |")
    assert wordsthatactuallymatter == expected
    # pass
    