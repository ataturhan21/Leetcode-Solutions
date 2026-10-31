# LeetCode Solutions

My collection of LeetCode solutions in Python, SQL, and JavaScript, organized into directories by problem identifier and title.

Browse the problem directories for their descriptions and available solution files. The submissions follow LeetCode's problem-specific interfaces; they are not a standalone application.

[LeetCode profile](https://leetcode.com/u/ataturhan/)

## Browse by language

- [Python solutions](docs/solutions-python.md)
- [SQL solutions](docs/solutions-sql.md)
- [JavaScript solutions](docs/solutions-javascript.md)

The indexes link directly to the committed solution files. Folder identifiers follow this repository's export naming and may differ from the problem numbers displayed on LeetCode.

## Refresh the indexes

From the repository root with Python 3:

```bash
python3 scripts/build_index.py
python3 scripts/build_index.py --check
```

The generator scans filenames only; it does not import or execute submissions. Commit the updated `docs/solutions-*.md` files when adding or removing solutions.
