# Project Progress Tracker

## Functionality

| Area | Status | Notes |
|---|---|---|
| Task 1: `NearEarthObject.__init__` | In progress | Constructor logic added; remove starter markers/comments before submission. |
| Task 1: `NearEarthObject.fullname` | In progress | Should return `designation` or `designation (name)`. |
| Task 1: `NearEarthObject.__str__` | Pending | Must match README human-readable format. |
| Task 1: `CloseApproach.__init__` | Pending | Parse `_designation`, `time`, `distance`, `velocity`; set `neo=None`. |
| Task 1: `CloseApproach.time_str` | Pending | Use `datetime_to_str(self.time)`. |
| Task 1: `CloseApproach.__str__` | Pending | Must match README format. |
| Task 2a: `load_neos` / `load_approaches` | Pending | In `extract.py`. |
| Task 2b: `NEODatabase` linking + lookups | Pending | In `database.py`. |
| Task 3a: `create_filters` | Pending | In `filters.py`. |
| Task 3b: `query` stream | Pending | In `database.py`. |
| Task 3c: `limit` | Pending | In `filters.py`. |
| Task 4: `write_to_json` / `write_to_csv` | Pending | In `write.py`. |

## Style

| Area | Status | Notes |
|---|---|---|
| No starter markers (`# TODO`) | In progress | Must be fully removed before submit. |
| PEP 8 / PEP 257 | In progress | Keep docstrings and comments clean. |
| No debug prints/extraneous code | In progress | Final cleanup pass needed. |

## Final Checks Before Submission

- Remove all `# TODO` and starter comments.
- Remove temporary debug prints and ad-hoc test code.
- Run the test suite and fix failing tests.
- Remove generated output files created during Task 4.
- Add `EXTENSIONS.md` only if optional/standout features were implemented.
