# Static-Site

A static site generator written in Python with no third-party libraries. It turns a folder of Markdown files into a matching folder of HTML pages, using a single HTML template.

I built it to learn how a Markdown parser works from the inside: splitting a document into blocks, then splitting each block into inline text nodes, then rendering a tree of HTML nodes.

## What it supports

- **Blocks:** headings, paragraphs, code blocks, quotes, ordered lists and unordered lists
- **Inline:** bold, italic, inline code, links and images
- **Nested pages:** every `.md` file under `content/` becomes an `.html` file at the same path under `public/`
- **Static files:** everything in `static/` (CSS, images) is copied into `public/`

## How it works

1. `markdown_blocks.py` splits a page into blocks and works out each block's type.
2. `inline_markdown.py` and `textnode.py` split each block's text into typed text nodes.
3. `htmlnode.py` turns those nodes into a tree of HTML nodes and renders it.
4. `generation.py` fills the page's first `#` heading and its HTML into `template.html` and writes the result.

## Running it

Requires Python 3.10 or later.

```bash
./main.sh
```

This builds the site into `public/` and serves it at http://localhost:8888.

## Tests

```bash
./test.sh
```

Unit tests cover the text nodes, HTML nodes, inline delimiters and block parsing.

## Background

Built as a guided project on [Boot.dev](https://www.boot.dev).
