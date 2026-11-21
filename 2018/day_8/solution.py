from pathlib import Path


def tree(data: str) -> tuple[int, int]:
    numbers = iter(map(int, data.split()))

    def node() -> tuple[int, int]:
        child_count = next(numbers)
        meta_count = next(numbers)
        children = [node() for _ in range(child_count)]
        metadata = [next(numbers) for _ in range(meta_count)]

        metadata_sum = sum(child_metadata_sum for child_metadata_sum, _ in children)
        metadata_sum += sum(metadata)

        if child_count == 0:
            node_value = sum(metadata)
        else:
            node_value = sum(
                children[index - 1][1]
                for index in metadata
                if 1 <= index <= child_count
            )

        return metadata_sum, node_value

    return node()


def part1(data: str) -> int:
    return tree(data)[0]


def part2(data: str) -> int:
    return tree(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
