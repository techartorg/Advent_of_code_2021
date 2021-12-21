from copy import copy
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, List, Set


def _count_paths(rooms: DefaultDict[str, List], current_room: str, visited_rooms: Set[str], num_valid_paths: int) -> int:
    if current_room.lower() == 'end':
        return num_valid_paths + 1

    if current_room.islower() and current_room in visited_rooms:
        return num_valid_paths

    visited_rooms.add(current_room)
    for r in rooms.get(current_room, '' ):
        num_valid_paths = _count_paths(rooms, r, copy(visited_rooms), num_valid_paths)

    return num_valid_paths


def _count_paths_2( rooms: DefaultDict[str, List], current_room: str, visited_rooms: DefaultDict[str, int], num_visited_rooms: int) -> int:
    if current_room.lower() == "end":
        return num_visited_rooms + 1        
    elif current_room.islower() and visited_rooms.get(current_room):
        if current_room.lower() == "start":
            return num_visited_rooms
        elif any(r.islower() and visited_rooms.get(r, 0) > 1 for r in visited_rooms):
            return num_visited_rooms

    visited_rooms[current_room] += 1
    for r in rooms.get(current_room, []):
        num_visited_rooms = _count_paths_2(rooms, r, visited_rooms.copy(), num_visited_rooms)
    return num_visited_rooms


def part_1(data: List[List[str]]) -> None:
    rooms = defaultdict(list)
    for r1, r2 in data:
        rooms[r1].append(r2)
        rooms[r2].append(r1)

    print(_count_paths(rooms, "start", set(), 0))


def part_2(data: List[List[str]]) -> None:
    rooms = defaultdict(list)
    for r1, r2 in data:
        rooms[r1].append(r2)
        rooms[r2].append(r1)

    print(_count_paths_2(rooms, "start", defaultdict(int), 0))


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_12_input.txt"
    data = [x.strip().split('-') for x in filepath.read_text().splitlines()]
    part_1(data)
    part_2(data)
