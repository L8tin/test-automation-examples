from scripts.pipeline_scripts import configuration
from common import common_imports

def assert_text_matches(result: str, expected: str):
    """
    params: result and Expected Strings - Verification helper for UI text comparisons
    """
    print("[ui_verifications][assert_text_matches]")

    words_that_matter = result.split(".")[0]

    print(f"[ui_verifications] Comparing |{words_that_matter}| to |{expected}|")

    assert words_that_matter == expected
