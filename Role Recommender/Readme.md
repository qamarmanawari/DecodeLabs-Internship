# Tech Stack Recommender

A lightweight Python tool that recommends the most relevant job roles based on your current skills using **TF-IDF vectorization** and **cosine similarity**.

---

## Features

- Loads job roles and required skills from a CSV file
- Converts skill sets into TF-IDF vectors
- Accepts user skills via CLI (min 3, max 10)
- Ranks job roles by similarity match percentage
- Clean, ranked output with visual match bars

---

## Requirements

- Python 3.7+
- pandas
- scikit-learn

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

## Dataset Format

Create a file named `raw_skills.csv` in the project folder with the following columns:

```csv
job_role,skills
Data Scientist,"Python, Machine Learning, Statistics, SQL"
DevOps Engineer,"AWS, Docker, Kubernetes, CI/CD, Linux"
Frontend Developer,"JavaScript, React, HTML, CSS, Git"
```

> `skills` must be comma-separated inside quotes.

---

## Usage

```bash
python recommender.py
```

Then enter your skills when prompted:

```
> Python, Cloud, Automation
```

---

## How It Works

1. **Load** – Reads and validates `raw_skills.csv`
2. **Vectorize** – Applies `TfidfVectorizer` (comma-split tokens)
3. **Input** – Collects and cleans user skills
4. **Score** – Computes cosine similarity between user and each job role
5. **Rank** – Sorts and returns top 3 matches
6. **Display** – Shows role, match %, and skills

---

## Configuration

Edit these constants at the top of the script:

| Variable     | Default          | Description                    |
|--------------|------------------|--------------------------------|
| `CSV_FILE`   | `raw_skills.csv` | Input dataset path             |
| `MIN_SKILLS` | `3`              | Minimum skills required        |
| `MAX_SKILLS` | `10`             | Maximum skills recommended     |
| `TOP_N`      | `3`              | Number of results to display   |

---

## Example Output

```
==================================================
  TOP RECOMMENDED CAREER PATHS
==================================================
Your skills: Python, Cloud, Automation
--------------------------------------------------

1. DevOps Engineer
   Match : 72.4%  ██████████████
   Skills: AWS, Docker, Kubernetes, CI/CD, Linux

2. Data Scientist
   Match : 45.1%  █████████
   Skills: Python, Machine Learning, Statistics, SQL
```

---

## Notes

- Skill matching is **keyword-based** (not semantic). Use standard skill names.
- Duplicate skills are automatically removed.
- If no match is found, check spellings or expand the dataset.
