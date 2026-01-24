# Copilot Instructions

- **Repository shape:** Coursework workspace; materials live under Modules/. AI-Programming-with-Python contains lesson notebooks and two projects. Intermediate-Python hosts small exercises such as a T9 predictor. Top-level README notes the Colab-first workflow.
- **Notebooks first:** Most work happens in notebooks (Jupyter/Colab). Keep outputs minimal when committing. Follow the lesson folders for topic-specific assets (NumPy, pandas, PyTorch, transformers).
- **Projects:**
  - Project 1 (PCEP/data analysis) summary in [Modules/AI-Programming-with-Python/projects/Project%201%20-%20Data%20Driven%20Approach%20to%20AI%20and%20Python/README.md](Modules/AI-Programming-with-Python/projects/Project%201%20-%20Data%20Driven%20Approach%20to%20AI%20and%20Python/README.md).
  - Project 2 (transformer sentiment model) details in [Modules/AI-Programming-with-Python/projects/Project%202%20-%20Transformers%20for%20Sentiment%20Analysis/README.md](Modules/AI-Programming-with-Python/projects/Project%202%20-%20Transformers%20for%20Sentiment%20Analysis/README.md); model artifact lives at sentiment_model.pth alongside the starter notebook SentimentScope_starter.ipynb.
- **Key exercise (T9 predictor):** Source in [Modules/Intermediate-Python/exercises/t9-predict-text/t9.py](Modules/Intermediate-Python/exercises/t9-predict-text/t9.py) with helper utilities in [Modules/Intermediate-Python/exercises/t9-predict-text/helper.py](Modules/Intermediate-Python/exercises/t9-predict-text/helper.py) and reference solutions in [Modules/Intermediate-Python/exercises/t9-predict-text/gold.py](Modules/Intermediate-Python/exercises/t9-predict-text/gold.py). Training n-gram data is ngrams-10k.txt.
- **T9 algorithm expectations:**
  - `parse_content` should read whitespace-separated `word freq` lines into a dict of word→int.
  - `make_tree` builds a trie where each node maps characters to children and stores terminal entries as `'$<word>' : frequency`.
  - `predict` traverses the trie for a digit string using the keymap in helper.keymap, gathers descendant words, and returns them sorted by frequency (desc).
- **Running T9 locally:** From repo root run `python Modules/Intermediate-Python/exercises/t9-predict-text/t9.py`; during development swap `gold.*` with your own implementations to test. Input must be digits 2–9 (length ≥3).
- **Coding style:** Keep ASCII; prefer clear, small functions as in gold.py; avoid over-engineering—solutions are teaching-oriented. Minimal dependencies beyond standard library for exercises; PyTorch/Hugging Face appear only in Project 2 notebooks.
- **Data/model handling:** Large artifacts (e.g., sentiment_model.pth, ngrams-10k.txt) already tracked—do not rename paths casually. Avoid committing additional derived data or notebook outputs unless necessary for review.
- **Environment:** Default workflow assumes cloud/Colab; no repo-wide requirements file. Install libs ad hoc per notebook (PyTorch, transformers, pandas, numpy, matplotlib). For local runs, use Python 3.10+ and pip install as needed.
- **When adding new code:** Keep lesson code alongside its module folder; mirror existing naming patterns. Provide small, deterministic demos rather than long-running training loops; prefer CPU-friendly settings. Add brief comments only for non-obvious logic.
- **Verification:** For scripts, add quick CLI paths similar to T9 main guard; for notebooks, include a short inference/demo cell rather than full training reruns.
