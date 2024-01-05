import streamlit


def delete_instructions_function():
    with streamlit.container():
        streamlit.subheader("Instruction de suppression des données de Trace Money")
        streamlit.write("---")
        streamlit.write("##")
        streamlit.write("""
        
        Instructions de suppression des données pour Trace Money :

Trace Money n'est qu'une application web et nous ne sauvegardons pas vos données personnelles sur notre serveur. 
Conformément aux règles de la plateforme Facebook, nous devons fournir à l'utilisateur une URL de rappel pour la 
suppression des données ou une URL d'instructions pour la suppression des données. Si vous souhaitez supprimer vos 
activités pour Trace Money, suivez ces instructions :

    Allez dans les paramètres et la confidentialité de votre compte Facebook. Cliquez sur " Paramètres ".
    Ensuite, allez dans "Apps et sites web" et vous verrez toutes les activités de vos Apps.
    Sélectionnez la case d'option pour Trace Money.
    Cliquez sur le bouton "Supprimer".

Si vous souhaitez supprimer les données de votre compte utilisateur, vous devez nous demander de supprimer votre compte. 
Si votre compte d'utilisateur Trace Money n'est plus nécessaire à l'avenir, veuillez envoyer votre demande, 
accompagnée de l'adresse électronique de votre compte, à l'adresse suivante tresortamini@gmail.com 
Votre compte sera supprimé et toutes les données ne seront plus sauvegardées.
        
        
        """)


