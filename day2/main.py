def parse_into_ranges(input: str) -> list[tuple[int, int]]:
    for curr_range in input.split(","):
        left, right = map(int, curr_range.split("-"))
        yield (left, right)


def find_invalid_ids(range_start: int, range_end: int) -> list[int]:
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


with open("test.txt", "r") as infile:
    ranges = parse_into_ranges(infile.read())
    invalid_id_collection = []
    for range_start, range_end in ranges:
        # print(range_start, range_end)
        new_invalid_ids = find_invalid_ids(range_start, range_end)
        invalid_id_collection.extend(new_invalid_ids)
    print(
        f"[TEST] Found {len(invalid_id_collection)} invalid IDs with a total sum of {sum(invalid_id_collection)}"
    )

with open("input.txt", "r") as infile:
    ranges = parse_into_ranges(infile.read())
    invalid_id_collection = []
    for range_start, range_end in ranges:
        # print(range_start, range_end)
        new_invalid_ids = find_invalid_ids(range_start, range_end)
        invalid_id_collection.extend(new_invalid_ids)
    print(
        f"[PART 1] Found {len(invalid_id_collection)} invalid IDs with a total sum of {sum(invalid_id_collection)}"
    )
