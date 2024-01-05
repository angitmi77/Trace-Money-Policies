import streamlit


def cookies_policy_function():
    with streamlit.container():
        streamlit.subheader("Politique des cookies de Trace Money")
        streamlit.write("---")
        streamlit.write("##")
        streamlit.error("Politique sur les cookies non réquises pour une application !")


