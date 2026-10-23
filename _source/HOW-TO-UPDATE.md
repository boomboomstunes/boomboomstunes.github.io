# How this site is built

- `build.py` generates every page. Books, playlists, nav and social links are lists at the top of the file.
- `posts.txt` holds all blog posts. Each post starts with a line:
  `=== slug | Title | YYYY-MM-DD | image-file.jpg`
  then the text. Blank line = new paragraph, `## ` = heading, `- ` = bullet.
- Run `python3 build.py`; it writes the site to `out/`. Upload root pages to the repo root, `out/blog/*` to `blog/`.
- Images live in the repo: `img/` (site) and `img/blog/` (blog covers). Book covers for coloring books load from Amazon.
- The folder `_source` is not published (underscore folders are skipped by GitHub Pages).
