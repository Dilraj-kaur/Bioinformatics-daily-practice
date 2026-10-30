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

### Day 3 — FASTA File Parsing

**Objective:** Develop a Python parser to read FASTA-formatted DNA sequences, including multiline sequence records.

**Implementation:**
- Read FASTA files using Python file handling.
- Extract sequence identifiers from FASTA headers.
- Combine multiline sequences into continuous DNA strings.
- Normalise sequence characters to uppercase.
- Store parsed sequences in a dictionary for downstream analysis.

**Files:**
- `python/sequencing/fasta_parser.py`
- `data/example/example.fasta`

**Run:**
```bash
python3 python/sequencing/fasta_parser.py
```

**Clinical bioinformatics relevance:** FASTA parsing is a foundational operation in genomic sequence analysis. Correctly handling sequence records is important for reliable downstream bioinformatics workflows.

**Next improvement:** Add automated tests and validation for malformed headers, duplicate identifiers, and invalid sequence characters.

### Day 4 — FASTA Parser Validation and Automated Testing

**Objective:** Improve the reliability of the FASTA parser through input validation and automated unit testing.

**Implementation:**
- Added validation for missing sequence identifiers.
- Detected duplicate FASTA sequence identifiers.
- Added error handling for empty sequence records.
- Rejected invalid DNA characters outside the accepted A, C, G and T alphabet.
- Preserved support for multiline FASTA sequences and lowercase input.

**Automated testing:**

Created `tests/test_fasta_parser.py` with nine tests covering valid inputs, multiline records, multiple sequences, lowercase characters and malformed FASTA data.

**Validation results:**
- FASTA parser tests: 9 passed
- GC content calculator tests: 6 passed
- **Total: 15 tests passed**

**Command:** `python3 -m pytest -q`

**Clinical bioinformatics relevance:**

Explicit input validation helps prevent silent data loss and unexpected downstream results. Automated tests support reproducibility, traceability and reliable bioinformatics software development.

**Current limitation:** The parser currently supports unambiguous DNA bases (A, C, G and T). Support for IUPAC ambiguity codes and additional FASTA edge cases is planned for future development.
