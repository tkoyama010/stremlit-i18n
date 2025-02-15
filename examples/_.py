import streamlit as st
import json
import os
from gettext import translation, NullTranslations

class StreamlitI18n:
    def __init__(self, lang: str = "en", locale_dir: str = "locales"):
        self.lang = lang
        self.locale_dir = locale_dir
        self.translator = self._load_translator()

    def _load_translator(self):
        try:
            return translation("messages", localedir=self.locale_dir, languages=[self.lang])
        except FileNotFoundError:
            return NullTranslations()

    def set_language(self, lang: str):
        self.lang = lang
        self.translator = self._load_translator()

    def t(self, key: str):
        return self.translator.gettext(key)

@st.cache_resouce
def _():
    i18n = StreamlitI18n(lang=lang)
  　return i18n.t


def main():
    st.title("Streamlit i18n Example")
    
    # 言語選択
    lang = st.sidebar.selectbox("Select Language", ["en", "ja", "fr"])
    
    st.header(_("welcome"))
    st.write(_("description"))

if __name__ == "__main__":
    main()
