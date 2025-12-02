from typing import Literal


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

    def rotate_with_clicks(self, rotation: Rotation) -> int:
        if rotation.click_number == 0:
            return 0
        start_position = self.position
        self.position += rotation.rotate
        clicks = 0
        if (start_position == 0) and (rotation.direction == "L"):
            clicks -= 1
        while self.position < 0:
            self.position += self.max_position + 1
            clicks += 1
        while self.position > self.max_position:
            self.position -= self.max_position + 1
            clicks += 1
        if (self.position == 0) and (rotation.direction == "L"):
            clicks += 1
        return clicks


def parse_input(text: list[str]) -> list[Rotation]:
    return [Rotation(line.strip()) for line in text if len(line) > 1]


def process_input(test_input: list[str]):
    rotations = parse_input(test_input)
    safe = Safe(start_position=50, max_position=99)
    zero_clicks = 0
    for rotation in rotations:
        zero_clicks += safe.rotate_with_clicks(rotation)
        # print(
        #     f"Safe is at position {safe.position} after rotating with {rotation.rotate}"
        # )
    return zero_clicks


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        result = process_input(input.readlines())
        print(f"The result is {result}")
