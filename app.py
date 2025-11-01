
import pandas as pd
from fuzzywuzzy import fuzz
import streamlit as st
import os
import base64
from PIL import Image


file_path = "princes.csv"

image_path = os.path.join(os.path.dirname(__file__),"princess_girl.jpeg")


try:
    df = pd.read_csv(file_path,encoding= "utf-8"
                     ,quotechar='"',engine='python')
    print("sucessfully done")
except FileNotFoundError:
    print(f"could not found {file_path}")
#
def calculate_matchingscore(row,user_trait, user_motivation, user_field):
    WEIGHT_TRAIT = 0.40
    WEIGHT_MOTIVATION = 0.35
    WEIGHT_FIELD = 0.25

    trait_score = fuzz.token_set_ratio(user_trait, row['Top 3 Character Traits (Simple)'])
    motivation_score = fuzz.token_set_ratio(user_motivation , row['Core Motivation / Conflict'])
    field_score = fuzz.token_set_ratio(user_field, row['Primary Field / Focus'])

    final_score = (
        (trait_score *WEIGHT_TRAIT) +
        (motivation_score * WEIGHT_MOTIVATION) +
        (field_score * WEIGHT_FIELD)
    )

    return final_score


# streamlit section
st.set_page_config(page_title="Vibe Check.AI", layout="centered")

with open(image_path, "rb") as f:
    encoded_string = base64.b64encode(f.read()).decode()


st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: 28%;
        background-repeat: no-repeat;
        background-position:  90% center;
        background-color: #F6DCE2;
    }}
    *, h1, h2, h3, h4, h5, h6, p, span, div {{
        color: #4B0082;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# 3️⃣ Content
st.header("Vibe Check.AI")
st.subheader("Check your vibe ✨")

if "page" not in st.session_state:
    st.session_state.page = "home"

# 4️⃣ Home page
if st.session_state.page == "home":
    if st.button("✨ Start the Quiz"):
        st.session_state.page = "quiz"
        st.rerun()

# 5️⃣ Quiz page
elif st.session_state.page == "quiz":
    st.title("Vibe Check.AI: Personality Matcher")

    user_trait = st.text_input("Primary trait (e.g. Ambitious, Creative, Kind)")
    user_motivation = st.text_input("Core motivation (e.g. achieving financial success)")
    user_field = st.text_input("Field of interest (e.g. science, law)")

    if st.button("Find my match"):
        st.success("Results..............")
        df['Final_Match_Score'] = df.apply(
            lambda row: calculate_matchingscore(
                row, user_trait, user_motivation, user_field
            ),
            axis=1
        )

        best_match = df.sort_values(by='Final_Match_Score', ascending=False).iloc[0]
        score = round(best_match['Final_Match_Score'], 1)

        print("\n" + "=" * 50)
        st.header(f"👑 Your Best Match is: {best_match['Name'].upper()}!")
        print(f"Similarity Score: {score}/100")
        print("-" * 50)
        st.subheader(f"Goal Resemblance: {best_match['Core Motivation / Conflict']}")
        st.subheader(f"Your Quote: \"{best_match['Famous Quote']}\"")
        print("=" * 50)

# taking users input
# st.title("Vibe Check.AI: Who Are You, Really?")
# st.markdown("We're clocking your **main character energy**. Let's see who you got.")
# user_trait = st.text_input("Primary trait(eg -Ambitious, Creative, Kind)")
# user_motivation = st.text_input("Core motivation (eg-achieving financial success)")
# user_field = st.text_input("Field of interest(eg science/law)")
#
# if st.button("Find my match") and user_trait and user_motivation and user_field:
# # with st.spinner("Analyzing your inner strength..."):
#     df['Final_Match_Score'] = df.apply(
#         lambda row: calculate_matchingscore(
#             row, user_trait, user_motivation, user_field
#         ),
#         axis=1
#     )
#
#     best_match = df.sort_values(by='Final_Match_Score', ascending=False).iloc[0]
#     score = round(best_match['Final_Match_Score'], 1)
#
#     print("\n" + "=" * 50)
#     st.header(f"👑 Your Best Match is: {best_match['Name'].upper()}!")
#     print(f"Similarity Score: {score}/100")
#     print("-" * 50)
#     st.subheader(f"Goal Resemblance: {best_match['Core Motivation / Conflict']}")
#     st.subheader(f"Your Quote: \"{best_match['Famous Quote']}\"")
#     print("=" * 50)
#
