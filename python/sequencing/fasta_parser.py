
def parse_fasta(filepath: str) -> dict[str, str]:
    """Read a FASTA file and return sequence IDs and DNA sequences."""

    sequences = {}
    current_id = None
    current_sequence = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_sequence)

                current_id = line[1:].split()[0]
                current_sequence = []

            else:
                if current_id is None:
                    raise ValueError("Sequence found before FASTA header")

                current_sequence.append(line.upper())

    if current_id is not None:
        sequences[current_id] = "".join(current_sequence)

    return sequences


if __name__ == "__main__":
    result = parse_fasta("data/example/example.fasta")

    for sequence_id, sequence in result.items():
        print(f"{sequence_id}: {sequence}")

