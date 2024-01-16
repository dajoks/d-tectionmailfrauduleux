import enchant
import re

def regardergrammaire(text):
    # Vérification des erreurs grammaticales
    grammaire_erreur = 0
    # Vérification des phrases commençant par une majuscule et se terminant par un point.
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    for sentence in sentences:
        if not (sentence[0].isupper() and sentence[-1] in ['.', '?']):
            grammaire_erreur += 1

    return grammaire_erreur

def regardermail(email):
    # Vérification des adresses e-mail suspectes
    mailsuspicieux = ['codebanquaire', 'phishing', 'paiement', 'azerty', 'qwerty']
    return any(pattern in email for pattern in mailsuspicieux)

def demande_paiement(text):
    motspaiement = ['demande de paiement', 'code bancaire', 'crise financière', 'emprunt', 'dette', 'retrait', 'gains',
                 'gagner', 'loto', 'paiement']
    return any(mot in text.lower() for mot in motspaiement)

# Exemple d'utilisation
email_texte = input("Rentrez ici le texte de votre mail : ")
email = input("Ici mettez l'expéditeur du mail : ")

grammaire_erreur = regardergrammaire(email_texte)
mailsuspect = regardermail(email)
demande_paiement_texte = demande_paiement(email_texte)
demande_paiement_mail = demande_paiement(email)

virustotal = "https://www.virustotal.com/gui/home/url"

if grammaire_erreur != 0:
    print(f"Il y a {grammaire_erreur} erreurs de grammaire")

if grammaire_erreur > 3 or mailsuspect or demande_paiement_texte or demande_paiement_mail:
    print(f"Ce mail est suspect. Veuillez faire preuve de prudence. S'il y a un lien dans le mail, copiez-collez le lien sur le site {virustotal} pour une analyse approfondie.")
else:
    print(f"Ce mail est correct. Mais faites quand même attention s'il y a un lien dans le mail. Copiez-collez le lien sur le site {virustotal} pour une analyse approfondie.")
