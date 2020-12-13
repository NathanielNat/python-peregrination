from animals import bat
from animals import dolphin
from animals import goat 
from animals import crocodile
from animals import cobra 
from animals import frog 
from animals import eagle 
from animals import ostrich 
from animals import penguin 

def main():
    bat_object = bat.Bat()
    goat_object = goat.Goat()
    dolphin_object = dolphin.Dolphin()
    

    frog_object = frog.Frog()
    crocodile_object = crocodile.Crocodile()
    cobra_object = cobra.Cobra()
    
    eagle_object = eagle.Eagle()
    penguin_object = penguin.Penguin()
    ostrict_ostrict = ostrich.Ostrict()

    print(f'{goat_object.birth_method()}')
    print(f'{goat_object.skin_covering()}')
    print(f'{frog_object.skin_covering()}')

if __name__ == "__main__":
    main()


# ModuleNotFoundError: No module named 'animals.aves'; 'animals' is not a package