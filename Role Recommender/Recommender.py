# ===================PROJECT 3=================================
# PROJECT 3: Tech Stack Recommender
# DecodeLabs Internship | Batch 2026 | Powered by DecodeLabs
# ============================================================
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# ============================================================
# STEP 0: CONFIGURATION
# ============================================================
CSV_FILE = 'raw_skills.csv'
MIN_SKILLS = 3
MAX_SKILLS = 10
TOP_N = 3


# ============================================================
# STEP 1: DATA LOAD
# ============================================================
def load_dataset(file_path):
    """Load and validate the CSV file."""
    if not os.path.exists(file_path):
        print(f"❌ Error: '{file_path}' not found.")
        print("   Please place the CSV file in the same folder.")
        return None

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ CSV read error: {e}")
        return None

    # Check required columns
    required_cols = ['job_role', 'skills']
    for col in required_cols:
        if col not in df.columns:
            print(f"❌ Column '{col}' is missing in the CSV.")
            return None

    # Drop empty rows
    df = df.dropna(subset=required_cols)
    df = df[df['skills'].str.strip() != '']

    if df.empty:
        print("❌ CSV is empty or all data is missing.")
        return None

    print(f"✅ Dataset loaded: {len(df)} job roles found.")
    return df


# ============================================================
# STEP 2: TF-IDF VECTORIZATION
# ============================================================
def build_vectorizer(df):
    """Convert job role skills into TF-IDF vectors."""
    vectorizer = TfidfVectorizer(
        lowercase=True,
        strip_accents='unicode',
        token_pattern=r'[^,]+'  # Split by comma
    )
    job_vectors = vectorizer.fit_transform(df['skills'])

    vocab_size = len(vectorizer.get_feature_names_out())
    print(f"✅ Vectorization done. Vocabulary size: {vocab_size}")
    return vectorizer, job_vectors


# ============================================================
# STEP 3: USER INPUT
# ============================================================
def get_user_skills():
    """Get minimum 3 skills from user with validation."""
    print("\n" + "=" * 50)
    print("  TECH STACK RECOMMENDER")
    print("=" * 50)
    print(f"Enter your skills (minimum {MIN_SKILLS}, maximum {MAX_SKILLS})")
    print("Separate with commas. Example: Python, Cloud, Automation")
    print("-" * 50)

    while True:
        raw_input_str = input("> ").strip()

        # Empty check
        if not raw_input_str:
            print("❌ Please enter something! At least 3 skills required.")
            continue

        # Split and clean
        skills = [s.strip() for s in raw_input_str.split(',') if s.strip()]

        # Remove duplicates (case-insensitive)
        seen = set()
        unique_skills = []
        for s in skills:
            key = s.lower()
            if key not in seen:
                seen.add(key)
                unique_skills.append(s)

        # Minimum check
        if len(unique_skills) < MIN_SKILLS:
            print(f"❌ Only {len(unique_skills)} skills provided. "
                  f"Minimum {MIN_SKILLS} required!")
            continue

        # Maximum warning (allowed but warning)
        if len(unique_skills) > MAX_SKILLS:
            print(f"⚠️  {len(unique_skills)} skills is too many. "
                  f"Accuracy may drop (recommended: {MIN_SKILLS}-{MAX_SKILLS}).")
            confirm = input("   Continue? (y/n): ").strip().lower()
            if confirm != 'y':
                continue

        return ", ".join(unique_skills)


# ============================================================
# STEP 4: SCORING
# ============================================================
def score_items(user_skills, vectorizer, job_vectors, df):
    """Build user vector and calculate cosine similarity for each job role."""
    user_vector = vectorizer.transform([user_skills])
    similarity_scores = cosine_similarity(user_vector, job_vectors)[0]

    df = df.copy()
    df['similarity_score'] = similarity_scores
    return df


# ============================================================
# STEP 5 & 6: SORTING + FILTERING
# ============================================================
def get_top_n(df, n=TOP_N):
    """Sort descending and return top-N."""
    sorted_df = df.sort_values(by='similarity_score', ascending=False)
    return sorted_df.head(n)


# ============================================================
# STEP 7: OUTPUT
# ============================================================
def display_results(top_df, user_skills):
    """Display results in a clean format."""
    print("\n" + "=" * 50)
    print("  TOP RECOMMENDED CAREER PATHS")
    print("=" * 50)
    print(f"Your skills: {user_skills}")
    print("-" * 50)

    # Check if no match found
    if top_df['similarity_score'].max() == 0:
        print("⚠️  No match found. Please check your skill spellings.")
        return

    for rank, (_, row) in enumerate(top_df.iterrows(), 1):
        match_percent = row['similarity_score'] * 100
        bar = "█" * int(match_percent / 5)  # Visual bar
        print(f"\n{rank}. {row['job_role']}")
        print(f"   Match : {match_percent:.1f}%  {bar}")
        print(f"   Skills: {row['skills']}")

    print("\n" + "=" * 50)


# ============================================================
# MAIN FUNCTION
# ============================================================
def main():
    # Step 1: Load
    df = load_dataset(CSV_FILE)
    if df is None:
        return

    # Step 2: Vectorize
    vectorizer, job_vectors = build_vectorizer(df)

    # Step 3: User input
    user_skills = get_user_skills()

    # Step 4: Score
    scored_df = score_items(user_skills, vectorizer, job_vectors, df)

    # Step 5 & 6: Sort + Filter
    top_df = get_top_n(scored_df, TOP_N)

    # Step 7: Display
    display_results(top_df, user_skills)


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main()