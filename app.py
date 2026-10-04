"""Event Check-in: a small standard-library-only teaching project."""
import csv  # noqa: F401 -- available for the round-three CSV task
import io  # noqa: F401 -- available for the round-three CSV task
import json


TICKET_TYPES = ("standard", "vip", "student")


def registration_count(attendees):
    """Existing working behavior; preserve it while adding features."""
    return len(attendees)


def ticket_counts(attendees):
    """C1: Count ticket types. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement C1: Count ticket types")


def checked_in_names(attendees):
    """C2: List checked-in names. See TASKS.md for the complete contract."""
    return sorted(
        (attendee['name'] for attendee in attendees if attendee['checked_in']),
        key=str.casefold,
    )


def find_attendees(attendees, query):
    """C3: Search the guest list. See TASKS.md for the complete contract."""
    needle = query.strip().casefold()
    return [attendee for attendee in attendees if needle in attendee['name'].casefold()]


def check_in(attendees, name):
    """C4: Fix check-in without mutation. See TASKS.md for the complete contract."""
    for attendee in attendees:
        if attendee['name'] == name:
            attendee['checked_in'] = True
    return attendees


def remaining_capacity(capacity, attendees):
    """C5: Fix remaining capacity. See TASKS.md for the complete contract."""
    if capacity < 0:
        raise ValueError("capacity must not be negative")
    return max(capacity - registration_count(attendees), 0)


def normalize_ticket(label):
    """C6: Fix ticket normalization. See TASKS.md for the complete contract."""
    normalized = label.strip().casefold()
    if normalized not in TICKET_TYPES:
        raise ValueError(f"unknown ticket type: {label!r}")
    return normalized


def door_report(attendees):
    """C7: Build the door report. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement C7: Build the door report")


def guest_list(attendees, ticket):
    """C8: Build a ticket-specific guest list. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement C8: Build a ticket-specific guest list")


def to_csv(attendees):
    """C9: Export the guest list to CSV. See TASKS.md for the complete contract."""
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["name", "ticket", "checked_in"])
    for attendee in attendees:
        writer.writerow([attendee["name"], attendee["ticket"], 1 if attendee["checked_in"] else 0])
    return buffer.getvalue()


if __name__ == "__main__":
    example = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]
    print(json.dumps(example, indent=2))
    print("registration_count:", registration_count(example))
