# Xiaobu Chinese

A phone-friendly app for learning Chinese, covering HSK 1 and HSK 2.

- 42 lessons, about 384 words and phrases
- Pinyin, English meanings and sound for every item
- HSK 2 words come with example sentences
- Everyday sentence lessons (restaurant, shopping, travel, health, home)
- Flashcards and quizzes, including fill-in-the-blank
- A "Grammar made simple" page with 16 patterns
- Progress is saved in the browser

## Files

| File | What it is |
| --- | --- |
| `app.py` | The Streamlit page. It loads `xiaobu.html` and shows it full-screen. |
| `xiaobu.html` | The whole app: lessons, sound, flashcards, quizzes and grammar. |
| `requirements.txt` | Python packages Streamlit needs. |
| `README.md` | This file. |
| `.gitignore` | Tells git to skip temporary files. It is a hidden file. |

## Run on your computer

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Push to GitHub from VS Code

Open this folder itself in VS Code (File > Open Folder), so that `app.py` is at the top level. Then use one of these two ways.

**Way 1: the VS Code buttons**

1. Open the Source Control panel and click **Initialize Repository**.
2. Type a message such as `Add Xiaobu Chinese app`, then click **Commit**.
3. Click **Publish Branch**, sign in to GitHub if asked, and choose a public or private repository.

**Way 2: the terminal** (create an empty repository on GitHub first)

```bash
git init
git add .
git commit -m "Add Xiaobu Chinese app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

## Deploy on Streamlit Community Cloud

1. Make sure the repository has `app.py`, `xiaobu.html` and `requirements.txt` at its top level (not inside a folder).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app** and choose your repository and the `main` branch.
4. Set **Main file path** to `app.py`.
5. Click **Deploy** and wait a few minutes.

## Notes

- Sound uses the voices built into the phone or computer. If a device has no Chinese voice, the app shows a message and everything else still works. On Android, install the Google text-to-speech Chinese voice. On iPhone, Chinese voices are included.
- Progress (learned words and stars) is stored in the browser on each device. It is not shared between devices.
- To change or add lessons, edit the `UNITS` list near the top of the script in `xiaobu.html`. Each word is `[hanzi, pinyin, English]`, and HSK 2 words can add `[example hanzi, example pinyin, example English]` after them.
