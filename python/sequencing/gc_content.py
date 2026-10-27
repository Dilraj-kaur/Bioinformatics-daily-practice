
def calculate_gc_content(sequence: str) -> float:
    """
    Calculate GC percentage for a DNA sequence.

    Accepts A, C, G, T (case-insensitive).
    Raises ValueError for empty or invalid sequences.
    """
    sequence = sequence.upper()

    if not sequence:
        raise ValueError("DNA sequence cannot be empty")

    valid_bases = {"A", "C", "G", "T"}

    if not set(sequence).issubset(valid_bases):
        raise ValueError("Sequence contains invalid DNA bases")

    gc_count = sequence.count("G") + sequence.count("C")

    return (gc_count / len(sequence)) * 100


if __name__ == "__main__":
    example = "ATGCGC"
    result = calculate_gc_content(example)
    print(f"GC content: {result:.2f}%")

