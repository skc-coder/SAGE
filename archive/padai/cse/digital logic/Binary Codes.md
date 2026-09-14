## Overview
- Digital codes represent data (numbers, text, images) in binary form.
- Different codes serve various purposes: error detection, efficiency, simplicity.

## Types of Codes
- **Binary codes**: Fundamental representation of data.
- **Weighted codes**: Each bit has a weight (e.g., 8421).
- **Non-weighted codes**: No positional weights (e.g., Gray code).
- **Error detection codes**: Include parity bits.

## BCD (8421)
- Binary-Coded Decimal.
- Each decimal digit represented by 4 bits.
- **Benefit**: Easy decimal-to-binary conversion.
- **Drawback**: Not suitable for arithmetic operations.

## ASCII
- American Standard Code for Information Interchange.
- 7-bit code for characters/text.
- Standard for text representation.

## Self-Complementary Codes
- A code where the 9's complement of the decimal equivalent is found by taking the 1's complement of the code.
- For weight self-complementary codes: sum of weights = 9.

Example: excess 3 code (BCD + 3 code)
[[Gray Code]]

## Error correcting codes
[[hamming codes]]