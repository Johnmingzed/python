from cx_Freeze import setup, Executable

setup(
    name="Super Calculator Resistor 3000",
    version="0.1",
    description="Un petit programme de calcul de valeur de résistance \
        permmettant à la fois de définir le code couleur d'une résistance \
        pour une valeur donnée aussi bien que de retrouver ladite valeur \
        à partir du code couleur.\nCe programme se bas sur l'exemple fournis \
        par Gérard SWINNEN dans son cours 'Apprendre à programmer avec Python 3.",
    executables=[Executable("resistance.py")]
)
