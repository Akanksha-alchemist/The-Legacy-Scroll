The Legacy Scroll


A Character Matching Engine with Fuzzy Logic -“Every woman carries the echo of legends before her — this scroll merely helps her hear it.”

Overview
The Legacy Scroll is a fusion of data science and storytelling — a tool that lets girls and women discover which iconic figure (from Disney princesses to real-world queens) mirrors their essence the most.
By entering their traits, core motivation, and field of passion, the system reveals their closest match — not just by name, but by spirit.This project was built for learning and creative exploration, aiming to celebrate individuality through intelligent similarity scoring.


---
##  How It Works

1. The dataset (CSV) contains various **characters and their defining traits, motivations, and fields**.
2. The data is processed using **Pandas** into a clean DataFrame.
3. The user provides their own inputs (traits, motivation, field).
4. Using **FuzzyWuzzy’s string matching**, the system calculates a **similarity score** between the user’s input and every character in the dataset.
5. The top result reflects the user’s **closest character resemblance**.

---

##  Tech Stack

*  **Python**
*  **Pandas**
* **FuzzyWuzzy**
*  **Streamlit**
---

##  Features

* Intelligent fuzzy matching for textual similarities
* Clean and minimal Streamlit UI
* Real-time resemblance scoring
* Support for both fictional and real-world characters

---

## 🚀 Installation & Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/Akanksha-alchemist/The-Legacy-Scroll.git
cd The-Legacy-Scroll
pip install -r requirements.txt
streamlit run app.py
```

---

##  Example Use

1. Enter your top 3 traits (e.g., *kind, creative, determined*)
2. Add your core motivation (e.g., *freedom*, *kindness*, *justice*)
3. Choose your field (e.g., *arts*, *science*, *leadership*)
4. The engine reveals the **woman you resonate with most**.

---

##  Behind the Scroll

At its heart, The Legacy Scroll uses **Fuzzy String Matching** to measure how closely words align in meaning and tone — transforming plain text into connections that feel human and meaningful.

---

##  Vision

To build a digital mirror for women and girls — a space that reflects strength, empathy, and legacy through the harmony of **data and identity**.

Future versions may include:

* Machine Learning–based semantic similarity
* Expanded dataset with more real-world heroines
* Interactive visualizations for deeper insights

---

##  Author

**Akanksha (The Alchemist)**

> “Alchemy isn’t turning metal into gold — it’s turning ideas into meaning.”
