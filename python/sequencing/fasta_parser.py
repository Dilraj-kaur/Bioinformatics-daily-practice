
def parse_fasta(filepath: str) -> dict[str, str]:
    """Read a FASTA file and validate unambiguous DNA sequences."""

    sequences = {}
    current_id = None
    current_sequence = []

    def save_sequence():
        if current_id is None:
            return

        sequence = "".join(current_sequence)

        if not sequence:
            raise ValueError(f"Empty sequence for {current_id}")

        valid_bases = {"A", "C", "G", "T"}

        if not set(sequence).issubset(valid_bases):
            raise ValueError(f"Invalid DNA bases in {current_id}")

        sequences[current_id] = sequence

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                save_sequence()

                parts = line[1:].split()

                if not parts:
                    raise ValueError("FASTA header has no identifier")

                new_id = parts[0]

                if new_id in sequences:
                    raise ValueError(f"Duplicate FASTA ID: {new_id}")

                current_id = new_id
                current_sequence = []

            else:
                if current_id is None:
                    raise ValueError("Sequence found before FASTA header")

                current_sequence.append(line.upper())

    save_sequence()

    return sequences


if __name__ == "__main__":
    result = parse_fasta("data/example/example.fasta")

    for sequence_id, sequence in result.items():
        print(f"{sequence_id}: {sequence}")

