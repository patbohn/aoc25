import numpy as np
from functools import cache


def parse_into_ranges(input: str) -> list[tuple[int, int]]:
    for curr_range in input.split(","):
        left, right = map(int, curr_range.split("-"))
        yield (left, right)


def find_invalid_ids_part1(range_start: int, range_end: int) -> list[int]:
    invalid_ids = []
    for i in range(range_start, range_end + 1):
        i_str = str(i)
        len_i = len(i_str)
        if (len_i == 0) or ((len_i % 2) != 0):
            continue
        # print(f"{i_str=} {len_i=} {len_i//2=}")
        num_digits = len(set(i_str))
        if num_digits > (len_i // 2):
            continue
        if i_str[: len_i // 2] == i_str[len_i // 2 :]:
            invalid_ids.append(i)
    return invalid_ids


@cache
def get_divisors(num: int) -> list[int]:
    divisors = []
    for i in range(1, int(np.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return divisors


def find_invalid_ids_part2(range_start: int, range_end: int) -> list[int]:
    invalid_ids = []
    # print(f"Starting range {range_start=} to {range_end=}")
    for i in range(range_start, range_end + 1):
        i_str = str(i)
        len_i = len(i_str)
        if len_i == 0:
            continue
        # print(f"{i_str=} {len_i=} {len_i//2=}")
        num_digits = len(set(i_str))

        if num_digits > (len_i // 2):
            continue  # couldn't repeat at least once

        # possible repeat patterns are all divisibles, e.g. for len_i 9 with 3 digits = 3
        # for len_i 8 with 2 digits: 2, 4

        divisors = get_divisors(len_i)
        # print(f"{i=} {len_i=} {divisors=}")
        for divisor in divisors:
            if divisor < num_digits:
                continue
            if divisor == len_i:
                continue
            repeat_unit = i_str[:divisor]
            # print(f"{i=} {divisor=} {repeat_unit=}")
            test_results = []
            for j in range(1, (len_i // divisor)):
                test_sequence = i_str[j * divisor : (j + 1) * divisor]
                # print(f"{test_sequence=}")
                test_results.append(test_sequence == repeat_unit)
            if all(test_results):
                invalid_ids.append(i)
                # print(f"Found invalid id: {i}")
                break
    # print(f"Invalid IDs found in range: {invalid_ids}")
    return invalid_ids


with open("test.txt", "r") as infile:
    ranges = parse_into_ranges(infile.read())
    invalid_id_collection = []
    for range_start, range_end in ranges:
        # print(range_start, range_end)
        new_invalid_ids = find_invalid_ids_part1(range_start, range_end)
        invalid_id_collection.extend(new_invalid_ids)
    print(
        f"[TEST] Found {len(invalid_id_collection)} invalid IDs with a total sum of {sum(invalid_id_collection)}"
    )

with open("input.txt", "r") as infile:
    ranges = parse_into_ranges(infile.read())
    invalid_id_collection = []
    for range_start, range_end in ranges:
        # print(range_start, range_end)
        new_invalid_ids = find_invalid_ids_part1(range_start, range_end)
        invalid_id_collection.extend(new_invalid_ids)
    print(
        f"[PART 1] Found {len(invalid_id_collection)} invalid IDs with a total sum of {sum(invalid_id_collection)}"
    )


with open("test.txt", "r") as infile:
    ranges = parse_into_ranges(infile.read())
    invalid_id_collection = []
    for range_start, range_end in ranges:
        # print(range_start, range_end)
        new_invalid_ids = find_invalid_ids_part2(range_start, range_end)
        invalid_id_collection.extend(new_invalid_ids)
    print(
        f"[TEST PART 2] Found {len(invalid_id_collection)} invalid IDs with a total sum of {sum(invalid_id_collection)}"
    )
    print(f"All invalid IDs: {invalid_id_collection}")

with open("input.txt", "r") as infile:
    ranges = parse_into_ranges(infile.read())
    invalid_id_collection = []
    for range_start, range_end in ranges:
        # print(range_start, range_end)
        new_invalid_ids = find_invalid_ids_part2(range_start, range_end)
        invalid_id_collection.extend(new_invalid_ids)
    print(
        f"[PART 2] Found {len(invalid_id_collection)} invalid IDs with a total sum of {sum(invalid_id_collection)}"
    )
