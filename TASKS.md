# Event Check-in: task pool

Each attendee is a dictionary with `name` (unique nonempty string), `ticket` (one of `standard`, `vip`, `student`), and `checked_in` (boolean). Records already use canonical ticket labels. Assume well-formed records. Functions preserve inputs; check-in returns a new list of new dictionaries.

All nine tasks are required for final acceptance. Each function lives in `app.py`. Inputs follow the data model above unless a task explicitly asks for validation. Return values are checked for equality; object identity matters only where new dictionaries are required. Reuse requirements are checked by peer review.

For every task: add at least one meaningful test in `tests/test_student_<ID>.py`, run the task checks, create its completion marker, and open a PR. Round two also requires a regression demonstration. Round three also requires the shared release-note edit described in `CONTRIBUTING.md`.

## C1 — Count ticket types

Round 1 · `ticket_counts(attendees)`

Return a dictionary of observed ticket labels and their counts, including attendees not yet checked in. Omit ticket types not present. Empty input returns `{}`.

No earlier task dependency.

Acceptance tests: `tests/test_C1.py`.

Run: `python3 check.py --task C1`; then `python3 check.py --complete C1`.

## C2 — List checked-in names

Round 1 · `checked_in_names(attendees)`

Return the names of attendees whose checked_in value is true, sorted by casefolded name. Preserve original order for equal casefolded names. Empty input returns `[]`.

No earlier task dependency.

Acceptance tests: `tests/test_C2.py`.

Run: `python3 check.py --task C2`; then `python3 check.py --complete C2`.

## C3 — Search the guest list

Round 1 · `find_attendees(attendees, query)`

Strip and casefold the query; match it as a substring of each casefolded name. Preserve input order. Empty or whitespace-only query returns all attendees.

No earlier task dependency.

Acceptance tests: `tests/test_C3.py`.

Run: `python3 check.py --task C3`; then `python3 check.py --complete C3`.

## C4 — Fix check-in without mutation

Round 2 · `check_in(attendees, name)`

Match an exact name and set checked_in true in a new list of new dictionaries, preserving order and other fields. Repeated check-in is allowed and leaves the state true. Raise `KeyError` for an unknown name. Preserve inputs even on failure.

No earlier task dependency.

Acceptance tests: `tests/test_C4.py`.

Run: `python3 check.py --task C4`; then `python3 check.py --complete C4`.

## C5 — Fix remaining capacity

Round 2 · `remaining_capacity(capacity, attendees)`

Return max(capacity minus the number of registered attendees, 0). Every registration consumes a place, even before check-in. Raise `ValueError` for a negative capacity. Assume an integer capacity.

No earlier task dependency.

Acceptance tests: `tests/test_C5.py`.

Run: `python3 check.py --task C5`; then `python3 check.py --complete C5`.

## C6 — Fix ticket normalization

Round 2 · `normalize_ticket(label)`

Strip and casefold a string label. Return it if it is `standard`, `vip`, or `student`; otherwise raise `ValueError`, including for an empty string. Do not invent aliases.

No earlier task dependency.

Acceptance tests: `tests/test_C6.py`.

Run: `python3 check.py --task C6`; then `python3 check.py --complete C6`.

## C7 — Build the door report

Round 3 · `door_report(attendees)`

Reuse `registration_count`, `checked_in_names` and `ticket_counts`. Return exactly `registered`, `checked_in`, `not_arrived` (counts), and `tickets` (ticket counts). Empty input returns three zeros and `{}`.

Depends on: C1, C2, C4.

Acceptance tests: `tests/test_C7.py`.

Run: `python3 check.py --task C7`; then `python3 check.py --complete C7`.

## C8 — Build a ticket-specific guest list

Round 3 · `guest_list(attendees, ticket)`

Normalize the requested ticket with `normalize_ticket`. Return matching attendee records sorted by casefolded name, with stable order for ties. Include both arrived and not-yet-arrived attendees. Unknown ticket labels raise `ValueError` even for an empty list.

Depends on: C6.

Acceptance tests: `tests/test_C8.py`.

Run: `python3 check.py --task C8`; then `python3 check.py --complete C8`.

## C9 — Export the guest list to CSV

Round 3 · `to_csv(attendees)`

Return CSV with header `name,ticket,checked_in`; encode checked_in as 1 or 0. Preserve row order, use LF (`\n`) line endings including a final newline, and quote commas, quotes and embedded newlines with `csv`. Empty input returns the header plus newline.

No earlier task dependency.

Acceptance tests: `tests/test_C9.py`.

Run: `python3 check.py --task C9`; then `python3 check.py --complete C9`.
