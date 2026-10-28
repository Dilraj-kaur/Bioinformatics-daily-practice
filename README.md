# Bioinformatics Daily Practice

A collection of Python-based bioinformatics exercises focused on developing reliable, reproducible, and well-documented computational biology workflows.

This repository supports my continued professional development in bioinformatics, with particular emphasis on genomic data analysis, software validation, automated testing, and clinical bioinformatics best practices.

## Project 1: DNA GC Content Calculator

### Day 1 — Implementing a DNA GC Content Calculator

**Objective:** Develop a Python function to calculate the GC content of a DNA sequence.

**File:** `python/sequencing/gc_content.py`

**Implementation:**
- Developed a reusable Python function, `calculate_gc_content()`.
- Calculated GC percentage using the proportion of guanine (G) and cytosine (C) bases in a DNA sequence.
- Implemented case-insensitive sequence handling.
- Added input validation for empty sequences and invalid nucleotide characters.
- Used Python exceptions to provide informative error messages.

**Formula:**

GC Content (%) = ((G + C) / Total DNA bases) × 100

**Example:**

Input: `ATGCGC`

Output: `66.67%`

**Key learning:** Python functions, string manipulation, input validation, exception handling, and Git version control.

### Day 2 — Automated Unit Testing with pytest

**Objective:** Validate the GC content calculator using automated unit tests.

**File:** `tests/test_gc_content.py`

**Implementation:**

Developed six unit tests covering:

1. Standard DNA sequence with 50% GC content.
2. DNA sequence containing 100% GC content.
3. DNA sequence containing 0% GC content.
4. Lowercase DNA sequence handling.
5. Empty sequence error handling.
6. Invalid nucleotide error handling.

**Testing command:**

```bash
python3 -m pytest -q
```

**Validation result:**

6 tests passed.

**Key learning:** Unit testing, assertions, exception testing, edge-case validation, and reproducible software testing.

### Relevance to Clinical Bioinformatics

GC content is a fundamental sequence characteristic relevant to genomic data analysis, sequencing assay design, and quality assessment.

This exercise demonstrates foundational practices for developing reliable bioinformatics software:

- Input validation to prevent unexpected sequence data from producing misleading results.
- Automated testing to check expected program behaviour.
- Version control to maintain a traceable development history.
- Documentation to support reproducibility and code review.

These practices provide a foundation for more complex clinical bioinformatics workflows, where software quality, validation, and traceability are particularly important.

## Technology Stack

- Python
- pytest
- Git and GitHub

## Future Development

Planned exercises include FASTA file parsing, sequence statistics, genomic variant processing, and further testing and documentation improvements.
