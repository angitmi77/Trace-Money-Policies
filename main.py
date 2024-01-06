import streamlit
import streamlit_option_menu
from privacy_policy import privacy_policy_function
from delete_instructions import delete_instructions_function
from terms_conditions import terms_conditions_function
from cookies_policy import cookies_policy_function

streamlit.set_page_config(
    page_title="Trace Admin Policies",
    page_icon=":fleur_de_lis",
    layout="wide"
)


# ------------ App -----------------
# Navigation menu
with streamlit.sidebar:
    streamlit.success(f"* Hi✌️")

    choice = streamlit_option_menu.option_menu(
        menu_title="Menu",
        options=["Politique de confidentialité", "Suppression des données utilisateur",
                 "Termes et conditions d'utilisation", "Politique des cookies"]

    )


if choice == "Politique de confidentialité":
    privacy_policy_function()
elif choice == "Suppression des données utilisateur":
    delete_instructions_function()
elif choice == "Termes et conditions d'utilisation":
    terms_conditions_function()
elif choice == "Politique des cookies":
    cookies_policy_function()






















