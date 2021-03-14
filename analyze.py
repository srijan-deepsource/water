import os

from helper import (
    make_issue,
    prepare_result,
    publish_results
)

# Add your analyzer logic below
def analyze():
    blacklisted_names = ("deepsource", "Deepsource", "deepSource")

    codepath = os.environ.get("CODE_PATH", "/code")

    issues = []
    lines = []

    filepath = os.path.join(codepath, "README.md")
    try:

        with open(
            filepath
        ) as fp:
            lines = fp.readlines()
    except:
        pass

    for idx, line in enumerate(lines):
        lno = idx + 1
        for bad_ds in blacklisted_names:
            if bad_ds in line:
                issues.append(
                    make_issue(
                        "WATER-001",
                        f"Blacklisted word: {bad_ds}",
                        filepath,
                        lno,
                        0
                    )
                )

    results = prepare_result(issues)
    publish_results(results)


if __name__ == "__main__":
    analyze()
