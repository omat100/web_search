# Web Search Engine
<img width="1751" height="958" alt="image" src="https://github.com/user-attachments/assets/ac524fcd-356f-4e26-9847-199b5b203786" />

A lightweight web search tool built with Flask and the DuckDuckGo Search API. Type a query, get results — no tracking, no clutter.

---

## What it does

A minimal search engine interface that takes your query, hits DuckDuckGo under the hood, and renders the top results in a clean UI. Title, URL, and snippet — just what you need.

---

## Features

- **Live search** — queries DuckDuckGo and returns up to 7 results per search
- **Clean results page** — title, clickable URL, and body snippet for each result
- **Persistent search bar** — your query stays in the search bar on the results page
- **Minimal UI** — built with Tailwind CSS, no bloat

---

## Getting started

**Requirements**
```
Python 3.10+
Flask
duckduckgo-search (ddgs)
```

**Install dependencies**
```bash
pip install flask duckduckgo-search
```

**Run**
```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Project structure

```
web_search/
├── app.py           # Flask routes
├── web.py           # DuckDuckGo search logic
└── templates/
    ├── index.html   # Home / search page
    └── search.html  # Results page
```

---

## How it works

1. User submits a query via the search form
2. Flask POSTs it to `/search`
3. `Web.search_from_arrays()` queries DuckDuckGo via `ddgs` and returns title, URL, and snippet for each result
4. Results are rendered in `search.html` using Jinja2 templating

---

## Built with

- [Flask](https://flask.palletsprojects.com/) — web framework
- [duckduckgo-search](https://pypi.org/project/duckduckgo-search/) — search API wrapper
- [Tailwind CSS](https://tailwindcss.com/) — styling

---

## Author

**Om Thakur**  
[github.com/omat100](https://github.com/omat100)
