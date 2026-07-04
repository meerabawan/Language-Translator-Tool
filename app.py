import streamlit as st
from deep_translator import GoogleTranslator
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #2196F3;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 180px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# App Title
st.markdown(
    "<h1 style='text-align: center; color: #2196F3;'>🌍 AI Language Translator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center;'>Translate text instantly into multiple languages</h4>",
    unsafe_allow_html=True
)
st.markdown("---")

# User Input
text = st.text_area(
    "📝 Enter your text here:",
    height=100,
    placeholder="Type or paste your text here..."
)

# Character Counter
st.caption(f"Characters entered: {len(text)}")

# Languages Dictionary
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Italian": "it",
    "Russian": "ru",
    "Korean": "ko",
    "Turkish": "tr"
}

# Source Language Dropdown
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "🌐 Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "🎯 Target Language",
        list(languages.keys())
    )

# Translate Button
if st.button("🚀 Translate"):
    
    if text.strip() == "":
        st.warning("Please enter some text to translate.")

    elif source_lang == target_lang:
        st.warning("Source and Target languages cannot be the same.")

    else:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("✅ Translation Completed!")

        st.text_area(
            "📄 Translated Text:",
             translated,
            height=150
        )

# Footer

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Developed by Meerab Awan</p>",
    unsafe_allow_html=True
)