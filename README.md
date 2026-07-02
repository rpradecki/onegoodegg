# A Good Egg — demo site

A single-page marketing site (concept demo) served through Streamlit.

## Files
- `a-good-egg.html` — the site itself (self-contained: HTML + CSS + JS)
- `streamlit_app.py` — Streamlit wrapper that renders the HTML
- `requirements.txt` — Python dependencies

## Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Community Cloud (via GitHub)

1. Create a new GitHub repo and upload these three files to the repo root:
   `a-good-egg.html`, `streamlit_app.py`, `requirements.txt`.
   - Web UI: on the repo page, **Add file → Upload files**, drag all three in, **Commit**.
   - Or CLI:
     ```bash
     git init
     git add a-good-egg.html streamlit_app.py requirements.txt README.md
     git commit -m "A Good Egg demo site"
     git branch -M main
     git remote add origin https://github.com/<you>/<repo>.git
     git push -u origin main
     ```
2. Go to https://share.streamlit.io and sign in with GitHub.
3. **Create app → Deploy a public app from GitHub.**
4. Pick your repo, branch `main`, and set **Main file path** to `streamlit_app.py`.
5. **Deploy.** You'll get a public URL like `https://<name>.streamlit.app`.

## Notes
- The page renders inside an iframe. If the bottom gets cut off, raise the
  `height=5200` value in `streamlit_app.py`; if there's too much empty space,
  lower it.
- Any edit pushed to the `main` branch redeploys automatically.
