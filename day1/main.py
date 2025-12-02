from typing import Literal

test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


class Rotation:
    direction: Literal["L", "R"]
    click_number: int

    def __init__(self, text: str):
        self.direction = text[:1]
        self.click_number = int(text[1:])

    @property
    def rotate(self):
        if self.direction == "L":
            return -self.click_number
        return self.click_number


class Safe:
    max_position: int
    position: int

    def __init__(self, start_position: int, max_position: int = 99):
        self.max_position = max_position
        self.position = start_position

    def rotate(self, rotation: Rotation):
        self.position += rotation.rotate
        if self.position < 0:
            self.position += self.max_position + 1
        while self.position > self.max_position:
            self.position -= self.max_position + 1


def parse_input(text: list[str]) -> list[Rotation]:
    return [Rotation(line.strip()) for line in text if len(line) > 1]


def process_input(test_input: str):
    rotations = parse_input(test_input)
    safe = Safe(start_position=50, max_position=99)
    num_zeros = 0
    for rotation in rotations:
        safe.rotate(rotation)
        # print(
        #     f"Safe is at position {safe.position} after rotating with {rotation.rotate}"
        # )
        if safe.position == 0:
            num_zeros += 1
    return num_zeros


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        result = process_input(input.readlines())
        print(f"The result is {result}")
    # assert process_input(test_input) == 3
