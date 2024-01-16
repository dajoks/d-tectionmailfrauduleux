import enchant
import re


def regardergrammaire(text):
    #Vérification des erreurs grammaticales
    grammaire_erreur = 0
    #vérification des phrases commençant par une majuscule et se terminant par un point.
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    for sentence in sentences:
        if not (sentence[0].isupper() and sentence[-1] in ['.', '?']):
            grammaire_erreur += 1

    return grammaire_erreur

def regardermail(email):
    # Vérification des adresses e-mail suspectes
    mailsuspicieux = ['codebanquaire', 'phishing', 'paiement', 'azerty', 'qwerty']
    for pattern in mailsuspicieux:
        if pattern in email:
            return True

    return False

def demande_paiement(text):
    motspaiement = ['demande de paiement', 'code banquaire', 'crise financière', 'emprunt', 'dette', 'retrait', 'gains',
                 'gagner', 'loto', 'paiement']
    return any(mot in text.lower() for mot in motspaiement)

# Exemple d'utilisation
email_texte = "Bonjour jee suIs les homme qyfvbqyv"
email = "support@karim.com"

grammaire_erreur = regardergrammaire(email_texte)
mailsuspect = regardermail(email)
contient_demande_paiement = demande_paiement(email_texte)

virustotal = "https://www.virustotal.com/gui/home/url"

if grammaire_erreur != 0:
    print("Il y a " + str(grammaire_erreur) + " erreurs de grammaire")

if grammaire_erreur > 3 or int(mailsuspect) or contient_demande_paiement:
    print("Ce mail est suspect. Veuillez faire preuve de prudence. S'il y a un lien dans le mail. Copiez-collez le lien sur le site " + virustotal + " pour une analyse approfondie.")
else:
    print("Ce mail est correct. Mais faites quand même attention s'il y a un lien dans le mail. Copiez-collez le lien sur le site " + virustotal + " pour une analyse approfondie.")
