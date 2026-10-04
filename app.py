"""Event Check-in: a small standard-library-only teaching project."""
import csv
import io
import json


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
    raise NotImplementedError("Implement C3: Search the guest list")


def check_in(attendees, name):
    """C4: Fix check-in without mutation. See TASKS.md for the complete contract."""
    updated_attendees = []
    found = False
    for attendee in attendees:
        updated_attendee = dict(attendee)
        if attendee['name'] == name:
            updated_attendee['checked_in'] = True
            found = True
        updated_attendees.append(updated_attendee)
    if not found:
        raise KeyError(name)
    return updated_attendees


def remaining_capacity(capacity, attendees):
    """C5: Fix remaining capacity. See TASKS.md for the complete contract."""
    return capacity - sum(attendee['checked_in'] for attendee in attendees)


def normalize_ticket(label):
    """C6: Fix ticket normalization. See TASKS.md for the complete contract."""
    return label.lower()


def door_report(attendees):
    """C7: Build the door report. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement C7: Build the door report")


def guest_list(attendees, ticket):
    """C8: Build a ticket-specific guest list. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement C8: Build a ticket-specific guest list")


def to_csv(attendees):
    """C9: Export the guest list to CSV. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement C9: Export the guest list to CSV")


if __name__ == "__main__":
    example = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]
    print(json.dumps(example, indent=2))
    print("registration_count:", registration_count(example))
