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

GitHub pushes and releases are **pending**. The terminal has no available GitHub credentials. The user confirmed `Yan-HaoNan` as the destination account. Lab 3 origin is now `https://github.com/Yan-HaoNan/Lab3.git`; Lab 2 origin is `https://github.com/Yan-HaoNan/Lab2.git`. Repository access remains unverified because terminal Git authentication is unavailable. The connected GitHub account is `HN-YAN-26`.

After confirming the destination and authenticating Git:

```powershell
git -C Lab2 push origin master
git -C Lab2 push origin Lab2_v3.0
git remote set-url origin https://github.com/Yan-HaoNan/Lab3.git
git push -u origin master
git push origin Lab3_v1.0 Lab3_v2.0 Lab3_v4.0 Lab3_v5.0
```

Then create GitHub releases for `Lab2_v3.0`, `Lab3_v4.0`, and `Lab3_v5.0` from their matching tags. A local Git tag is not a published GitHub release.
