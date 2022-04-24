class ConsentPicture:

            
    global consent
    consent = []

    def __init__(self):
        return

    def createConsent():
        print("***********************************************************************************")
        print("****************************       Consentement       *****************************")
        print("***********************************************************************************")
        print("Dans le cadre de l'utilisation par 'You can use it', dont le siège est situé à l'UQC et ses prestataires techniques \n  à utiliser les images provenant d'image de caméra de sécurité dans le cadre de notre projet d'étude.")

        print("Conformément aux dispositions relatives au droit à l’image, j’accepte que les captations où j’apparais soient utilisées,\n exploitées et diffusées par 'You can use it' dans le cadre de ses activités auprès de ses différents publics, notamment sur des systèmes de diffusion live streaming, \n de vidéo conférence, des plateformes de streaming vidéo permettant le replay, ainsi que sous toute forme et sur tous supports connus et inconnus à ce jour, dans le monde entier, pour une durée de 2 ans, intégralement ou par extraits.")

        print("(Si l’intervenant est amené à présenter des slides) Je déclare disposer des droits de propriété intellectuelle sur les éléments \n et supports que je présenterai lors de mon intervention, ainsi que de l’autorisation de ma structure pour les diffuser. J’autorise 'You can use it' et \n ses prestataires techniques à intégrer les éléments présentés dans la vidéo diffusée.")

        print("'You can do it' s’interdit expressément de procéder à une exploitation des enregistrements susceptible de porter atteinte à la vie \n privée ou à la réputation, à la dignité ou à l’intégrité de ma personne.")
        print("Je garantis n’être lié(e) par aucun accord avec un tiers, de quelque nature que ce soit, ayant pour objet ou pour effet de limiter ou \n empêcher la mise en œuvre de la présente autorisation.")

        print("La présente autorisation d’exploitation de mon droit à l’image est consentie à titre gratuit.")
        consent.append(input("J'autorise ? (oui / non) :"))
        print("Je soussigné(e) ")
        consent.append(input("Nom :"))
        consent.append(input("prénom :"))
        consent.append(input("Demeurant :"))
        consent.append(input("Société / Entité (le cas échéant) :"))
        consent.append(input("Fait à ") )
        consent.append(input("le "))

        return consent

