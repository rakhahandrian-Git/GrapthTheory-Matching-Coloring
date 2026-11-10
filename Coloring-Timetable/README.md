# Coloring Algorithm for Timetable Problem

## Algorithm Explanation

The Welsh-Powell Algorithm is a classic greedy heuristic for graph coloring. In the context of a timetabling problem, **vertices** represent courses that need to be scheduled, **edges** represent conflicts, and **colors** represent available slots.

How it works:

1. Calculate Degrees: Count the number of conflicting neighbors (degree) for each course.
2. Sort Vertices: Order the courses in descending order based on their degree (highest number of conflicts first).
3. Sequential Coloring: Assign the first available color to the first uncolored course in the sorted list. Then, iterate down the list and assign the same color to any non-consecutive course that does not share an edge (conflict) with already colored courses using that color.
4. Repeat: Create a new color timeslot for any remaining uncolored courses and repeat until all courses are scheduled.

---

## Prerequisites

- **Python**: Python 3.8+ (tested on Python 3.12).
- **Dependencies**: **None** (Pure Python standard library modules are enough)

---

## Sample Input Output

_Used with algorith implementation at `implementation.py`_

### Input 1

```
{
    'Math': ['Physics', 'Chemistry'],
    'Physics': ['Math', 'Chemistry', 'Biology'],
    'Chemistry': ['Math', 'Physics'],
    'Biology': ['Physics']
}
```

### Output 1

```
Assigned Exam Timeslots (Colors):
  Physics -> Timeslot 1
  Math -> Timeslot 2
  Chemistry -> Timeslot 3
  Biology -> Timeslot 2
```

### Input 2

```
{
    'Algorithms': ['Databases', 'Operating Systems', 'AI'],
    'Databases': ['Algorithms', 'Networks'],
    'Operating Systems': ['Algorithms', 'Networks', 'AI'],
    'Networks': ['Databases', 'Operating Systems'],
    'AI': ['Algorithms', 'Operating Systems']
}
```

### Output 2

```
Assigned Exam Timeslots (Colors):
  Operating Systems -> Timeslot 1
  Algorithms -> Timeslot 2
  Networks -> Timeslot 1
  Databases -> Timeslot 2
  AI -> Timeslot 3
```

---

## AI Disclosure

- AI Model used: Gemini
- Scope of assistance: Assisted in writing code implementation and sample cases

