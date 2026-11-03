# LeetCode Solutions

My collection of LeetCode solutions in Python, SQL, and JavaScript, organized into directories by problem identifier and title.

Each problem directory holds the problem description (`README.md`), the solution file, and in some cases a `Notes.md` recording the time taken. The submissions follow LeetCode's problem-specific interfaces; they are not a standalone application.

[LeetCode profile](https://leetcode.com/u/ataturhan/)

## Browse by language

- [Python solutions](docs/solutions-python.md)
- [SQL solutions](docs/solutions-sql.md)
- [JavaScript solutions](docs/solutions-javascript.md)

The indexes link directly to the committed solution files and show the time taken recorded in `Notes.md` where one exists. Folder identifiers follow this repository's export naming and may differ from the problem numbers displayed on LeetCode.

## Refresh the indexes

From the repository root with Python 3 (use `python` instead of `python3` on Windows):

```bash
python3 scripts/build_index.py
python3 scripts/build_index.py --check
python3 -m unittest discover -s tests -v
```

The last command runs the generator's own tests, as CI does.

The generator scans filenames and reads `Notes.md` text; it does not import or execute submissions. Commit the updated `docs/solutions-*.md` files when adding or removing solutions.

## License

[MIT](LICENSE).
