# Event Check-in

Manage registration, find attendees, check people in, and prepare a door report.

This is a three-round team exercise. Start with [the student guide](CONTRIBUTING.md), then read your assigned card in [TASKS.md](TASKS.md). Your instructor supplies the author/reviewer schedule.

## Run it

Use Python 3.11 or later. No third-party packages are required.

```sh
python3 app.py
python3 check.py
```

The demo prints sample records and the existing `registration_count` result. Extend the Python functions according to the task cards. The starter has intentionally missing features and round-two bugs; baseline checks pass but final acceptance fails until the team finishes.

## Data model

Each attendee is a dictionary with `name` (unique nonempty string), `ticket` (one of `standard`, `vip`, `student`), and `checked_in` (boolean). Records already use canonical ticket labels. Assume well-formed records. Functions preserve inputs; check-in returns a new list of new dictionaries.

## Test a task

```sh
python3 check.py --task C1
# After implementation and a meaningful student test:
python3 check.py --complete C1
```

Commit `completed/C1.txt` with your code and test. Normal CI checks the baseline, every completed task, and student tests. Do not edit the supplied acceptance tests, runner, task manifest, or workflow.

After all rounds, run `python3 check.py --all` on current `main`. All nine tasks must pass, all nine markers must exist, and the shared release-note line must contain C7, C8 and C9. The final team pass plus individual implementation/review evidence is required for the bonus.
