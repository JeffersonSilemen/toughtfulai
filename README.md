# Package Sorting System

Package classification system based on dimensions and weight.

## Functionality

The `sort()` function classifies packages into three categories:

- **STANDARD**: Normal packages
- **SPECIAL**: Bulky OR heavy packages
- **REJECTED**: Bulky AND heavy packages

### Criteria

- **Bulky**: Any dimension ≥ 150cm OR volume ≥ 1,000,000 cm³
- **Heavy**: Mass ≥ 20kg

## Usage

```bash
python3 main.py        # Run examples
python3 test_main.py   # Run tests
```

## Tests

5 test cases covering all possible scenarios.
