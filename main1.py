import enchant
import re

def regardergrammaire(text):
    # Vérification orthographique
    dictionary = enchant.Dict("en_US")
    words = re.findall(r'\b\w+\b', text)
    misspelled_words = [word for word in words if not dictionary.check(word)]

    # Vérification des erreurs grammaticales (exemple simple)
    # Vous pouvez étendre cette partie en utilisant des outils NLP plus avancés
    grammaire_erreur = 0
    # Exemple simple : vérification des phrases commençant par une majuscule et se terminant par un point.
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    for sentence in sentences:
        if not (sentence[0].isupper() and sentence[-1] in ['.', '?']):
            grammaire_erreur += 1

    return misspelled_words, grammaire_erreur

def regardermail(email):
    # Vérification des adresses e-mail suspectes (exemple simple)
    suspicious_patterns = ['support', 'admin', 'security', 'phishing']
    for pattern in suspicious_patterns:
        if pattern in email:
            return True

    return False

# Exemple d'utilisation
email_content = "Bonjour jee suis le mansier"
email_address = "support@phishingsite.com"

misspelled_words, grammaire_erreur = regardergrammaire(email_content)
is_suspicious_email = regardermail(email_address)

print("Mots mal orthographiés:", misspelled_words)
print("Erreurs grammaticales:", grammaire_erreur)
print("Est-ce une adresse e-mail suspecte?", is_suspicious_email)
