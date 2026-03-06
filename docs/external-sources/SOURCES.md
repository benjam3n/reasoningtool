# Navigation Source Snapshots

These files are local snapshots used by the `where-am-i` pager labels.

- Dictionary upstream (immutable release): `https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2`
- Emoji upstream (immutable version): `https://unicode.org/Public/emoji/15.1/emoji-test.txt`

Snapshot date: 2026-03-06

Files:
- `navigation-dictionary-a.txt` (A-Z letter buckets used by pager labels)
- `navigation-emoji-standard.txt` (major emoji categories used by pager labels)

Pager rules:
- Page `N` uses dictionary letter `(N-1) mod 26` and cycles within that letter bucket.
- Page `N` uses emoji category `(N-1) mod category_count` and cycles within that category.
