week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for i in week:
    if i in week[0 : 4]:
        print("Au travail !")
    elif i == week[4]:
        print("Chouette c’est vendredi")
    else:
        print("Repo ce week-end")