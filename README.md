# Lab 3 - Developing software unit tests

Completed implementations and pytest tests for all five exercises. See [worksheet answers](LAB3_ANSWERS.md) for the Git commands, Table 3 requirement mapping, assumptions, and written responses.

## Run

```powershell
git submodule update --init --recursive
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The existing local environment can run `.venv/Scripts/python.exe -m pytest -q`.

Verified: **59 tests passed**, including the Lab 2 calculations and BMI. VS Code pytest discovery is enabled in `.vscode/settings.json`; pytest.ini includes both `test_*.py` and `Test_*.py`.

## Git status

All exercise code is committed locally. Local tags:

- Lab 3: `Lab3_v1.0` (requirement tests before sorting fixes), `Lab3_v2.0` (sorting fixes), `Lab3_v4.0` (fruit prices), `Lab3_v5.0` (employee queries).
- Lab 2: `Lab2_v3.0` (temperature calculations and tests).

Published successfully to `Yan-HaoNan`:

- [Lab 3 repository](https://github.com/Yan-HaoNan/Lab3)
- [Lab 2 release Lab2_v3.0](https://github.com/Yan-HaoNan/Lab2/releases/tag/Lab2_v3.0)
- [Lab 3 release Lab3_v4.0](https://github.com/Yan-HaoNan/Lab3/releases/tag/Lab3_v4.0)
- [Lab 3 release Lab3_v5.0](https://github.com/Yan-HaoNan/Lab3/releases/tag/Lab3_v5.0)

The Lab 2 master branch and Lab2_v3.0 tag are pushed. The Lab 3 master branch and Lab3_v1.0, Lab3_v2.0, Lab3_v4.0, and Lab3_v5.0 tags are pushed. Release tags mark their exercise implementation commits; the master branch also includes the worksheet answers and publication record.
