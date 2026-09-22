import sys

def main() :
    valance = [
      { "atomic_number": 1, "name": "Hydro", "symbol": "H", "atomic_mass": 1, "valences": ["I"] },
      { "atomic_number": 2, "name": "Heli", "symbol": "He", "atomic_mass": 4, "valences": [] },
      { "atomic_number": 3, "name": "Lithi", "symbol": "Li", "atomic_mass": 7, "valences": ["I"] },
      { "atomic_number": 4, "name": "Beryli", "symbol": "Be", "atomic_mass": 9, "valences": ["II"] },
      { "atomic_number": 5, "name": "Bor", "symbol": "B", "atomic_mass": 11, "valences": ["III"] },
      { "atomic_number": 6, "name": "Carbon", "symbol": "C", "atomic_mass": 12, "valences": ["II", "IV"] },
      { "atomic_number": 7, "name": "Nitơ", "symbol": "N", "atomic_mass": 14, "valences": ["I", "II", "III", "IV", "V"] },
      { "atomic_number": 8, "name": "Oxy", "symbol": "O", "atomic_mass": 16, "valences": ["II"] },
      { "atomic_number": 9, "name": "Fluor", "symbol": "F", "atomic_mass": 19, "valences": ["I"] },
      { "atomic_number": 10, "name": "Neon", "symbol": "Ne", "atomic_mass": 20, "valences": [] },
      { "atomic_number": 11, "name": "Natri", "symbol": "Na", "atomic_mass": 23, "valences": ["I"] },
      { "atomic_number": 12, "name": "Magnesi", "symbol": "Mg", "atomic_mass": 24, "valences": ["II"] },
      { "atomic_number": 13, "name": "Nhôm", "symbol": "Al", "atomic_mass": 27, "valences": ["III"] },
      { "atomic_number": 14, "name": "Silic", "symbol": "Si", "atomic_mass": 28, "valences": ["IV"] },
      { "atomic_number": 15, "name": "Phosphor", "symbol": "P", "atomic_mass": 31, "valences": ["III", "V"] },
      { "atomic_number": 16, "name": "Lưu huỳnh", "symbol": "S", "atomic_mass": 32, "valences": ["II", "IV", "VI"] },
      { "atomic_number": 17, "name": "Chlor", "symbol": "Cl", "atomic_mass": 35.5, "valences": ["I", "II", "III", "IV", "V", "VII"] },
      { "atomic_number": 18, "name": "Argon", "symbol": "Ar", "atomic_mass": 40, "valences": [] },
      { "atomic_number": 19, "name": "Kali", "symbol": "K", "atomic_mass": 39, "valences": ["I"] },
      { "atomic_number": 20, "name": "Calci", "symbol": "Ca", "atomic_mass": 40, "valences": ["II"] },
      { "atomic_number": 21, "name": "Scandi", "symbol": "Sc", "atomic_mass": 45, "valences": ["III"] },
      { "atomic_number": 22, "name": "Titani", "symbol": "Ti", "atomic_mass": 48, "valences": ["II", "III", "IV"] },
      { "atomic_number": 23, "name": "Vanadi", "symbol": "V", "atomic_mass": 51, "valences": ["II", "III", "IV", "V"] },
      { "atomic_number": 24, "name": "Chromi", "symbol": "Cr", "atomic_mass": 52, "valences": ["II", "III", "IV", "VI"] },
      { "atomic_number": 25, "name": "Mangan", "symbol": "Mn", "atomic_mass": 55, "valences": ["II", "IV", "VII"] },
      { "atomic_number": 26, "name": "Sắt", "symbol": "Fe", "atomic_mass": 56, "valences": ["II", "III"] },
      { "atomic_number": 27, "name": "Cobalt", "symbol": "Co", "atomic_mass": 58.9, "valences": ["II"] },
      { "atomic_number": 28, "name": "Nickel", "symbol": "Ni", "atomic_mass": 58.7, "valences": ["II", "III", "IV"] },
      { "atomic_number": 29, "name": "Đồng", "symbol": "Cu", "atomic_mass": 64, "valences": ["I", "II"] },
      { "atomic_number": 30, "name": "Kẽm", "symbol": "Zn", "atomic_mass": 65, "valences": ["II"] },
      { "atomic_number": 31, "name": "Gali", "symbol": "Ga", "atomic_mass": 70, "valences": ["III"] },
      { "atomic_number": 32, "name": "Germani", "symbol": "Ge", "atomic_mass": 73, "valences": ["II", "IV"] },
      { "atomic_number": 33, "name": "Arsenic", "symbol": "As", "atomic_mass": 75, "valences": ["III", "V"] },
      { "atomic_number": 34, "name": "Seleni", "symbol": "Se", "atomic_mass": 79, "valences": ["II", "IV", "VI"] },
      { "atomic_number": 35, "name": "Brom", "symbol": "Br", "atomic_mass": 80, "valences": ["I", "II", "III", "IV", "V", "VI", "VII"] },
      { "atomic_number": 36, "name": "Krypton", "symbol": "Kr", "atomic_mass": 84, "valences": [] },
      { "atomic_number": 37, "name": "Rubidi", "symbol": "Rb", "atomic_mass": 85.5, "valences": ["I"] },
      { "atomic_number": 38, "name": "Stronti", "symbol": "Sr", "atomic_mass": 88, "valences": ["II"] },
      { "atomic_number": 39, "name": "Ytri", "symbol": "Y", "atomic_mass": 89, "valences": ["III"] },
      { "atomic_number": 40, "name": "Zirconi", "symbol": "Zr", "atomic_mass": 91, "valences": ["IV"] },
      { "atomic_number": 41, "name": "Niobi", "symbol": "Nb", "atomic_mass": 93, "valences": ["V"] },
      { "atomic_number": 42, "name": "Molybden", "symbol": "Mo", "atomic_mass": 96, "valences": ["II", "III", "IV", "VI"] },
      { "atomic_number": 43, "name": "Techneti", "symbol": "Tc", "atomic_mass": 99, "valences": ["III", "IV", "VII"] },
      { "atomic_number": 44, "name": "Rutheni", "symbol": "Ru", "atomic_mass": 101, "valences": ["II", "III", "IV"] },
      { "atomic_number": 45, "name": "Rhodi", "symbol": "Rh", "atomic_mass": 103, "valences": ["II", "III", "IV"] },
      { "atomic_number": 46, "name": "Paladi", "symbol": "Pd", "atomic_mass": 106, "valences": ["II", "IV"] },
      { "atomic_number": 47, "name": "Bạc", "symbol": "Ag", "atomic_mass": 108, "valences": ["I"] },
      { "atomic_number": 48, "name": "Cadmi", "symbol": "Cd", "atomic_mass": 112, "valences": ["II"] },
      { "atomic_number": 49, "name": "Indi", "symbol": "In", "atomic_mass": 114, "valences": ["I", "III"] },
      { "atomic_number": 50, "name": "Thiếc", "symbol": "Sn", "atomic_mass": 119, "valences": ["II", "IV"] },
      { "atomic_number": 51, "name": "Antimon", "symbol": "Sb", "atomic_mass": 122, "valences": ["III", "V"] },
      { "atomic_number": 52, "name": "Teluri", "symbol": "Te", "atomic_mass": 128, "valences": ["II", "IV", "VII"] },
      { "atomic_number": 53, "name": "Iod", "symbol": "I", "atomic_mass": 127, "valences": ["I", "III", "V", "VII"] },
      { "atomic_number": 54, "name": "Xenon", "symbol": "Xe", "atomic_mass": 131, "valences": [] },
      { "atomic_number": 55, "name": "Caesi", "symbol": "Cs", "atomic_mass": 133, "valences": ["I"] },
      { "atomic_number": 56, "name": "Bari", "symbol": "Ba", "atomic_mass": 137, "valences": ["II"] },
      { "atomic_number": 57, "name": "Lanthan", "symbol": "La", "atomic_mass": 139, "valences": ["III"] },
      { "atomic_number": 58, "name": "Ceri", "symbol": "Ce", "atomic_mass": 140, "valences": ["III", "IV"] },
      { "atomic_number": 59, "name": "Praseodymi", "symbol": "Pr", "atomic_mass": 141, "valences": ["III", "IV"] },
      { "atomic_number": 60, "name": "Neodymi", "symbol": "Nd", "atomic_mass": 144, "valences": ["II", "III", "IV"] },
      { "atomic_number": 61, "name": "Promethi", "symbol": "Pm", "atomic_mass": 145, "valences": ["III"] },
      { "atomic_number": 62, "name": "Samari", "symbol": "Sm", "atomic_mass": 150, "valences": ["II", "III"] },
      { "atomic_number": 63, "name": "Europi", "symbol": "Eu", "atomic_mass": 152, "valences": ["II", "III"] },
      { "atomic_number": 64, "name": "Gadolini", "symbol": "Gd", "atomic_mass": 157, "valences": ["III"] },
      { "atomic_number": 65, "name": "Terbi", "symbol": "Tb", "atomic_mass": 159, "valences": ["III", "IV"] },
      { "atomic_number": 66, "name": "Dysprosi", "symbol": "Dy", "atomic_mass": 162.5, "valences": ["III", "IV"] },
      { "atomic_number": 67, "name": "Holmi", "symbol": "Ho", "atomic_mass": 165, "valences": ["III"] },
      { "atomic_number": 68, "name": "Erbi", "symbol": "Er", "atomic_mass": 167, "valences": ["III"] },
      { "atomic_number": 69, "name": "Thuli", "symbol": "Tm", "atomic_mass": 169, "valences": ["III"] },
      { "atomic_number": 70, "name": "Ytterbi", "symbol": "Yb", "atomic_mass": 173, "valences": ["II", "III"] },
      { "atomic_number": 71, "name": "Luteti", "symbol": "Lu", "atomic_mass": 175, "valences": ["III"] },
      { "atomic_number": 72, "name": "Hafni", "symbol": "Hf", "atomic_mass": 178, "valences": ["IV"] },
      { "atomic_number": 73, "name": "Tantal", "symbol": "Ta", "atomic_mass": 181, "valences": ["V"] },
      { "atomic_number": 74, "name": "Wolfram", "symbol": "W", "atomic_mass": 184, "valences": ["II", "VI"] },
      { "atomic_number": 75, "name": "Rheni", "symbol": "Re", "atomic_mass": 186, "valences": ["III", "IV", "VII"] },
      { "atomic_number": 76, "name": "Osmi", "symbol": "Os", "atomic_mass": 190, "valences": ["II", "III", "IV", "VI"] },
      { "atomic_number": 77, "name": "Iridi", "symbol": "Ir", "atomic_mass": 192, "valences": ["II", "III", "IV"] },
      { "atomic_number": 78, "name": "Platin", "symbol": "Pt", "atomic_mass": 195, "valences": ["II", "IV"] },
      { "atomic_number": 79, "name": "Vàng", "symbol": "Au", "atomic_mass": 197, "valences": ["I", "II", "III"] },
      { "atomic_number": 80, "name": "Thủy ngân", "symbol": "Hg", "atomic_mass": 201, "valences": ["I", "II"] },
      { "atomic_number": 81, "name": "Thali", "symbol": "Tl", "atomic_mass": 204, "valences": ["I", "III"] },
      { "atomic_number": 82, "name": "Chì", "symbol": "Pb", "atomic_mass": 207, "valences": ["II", "IV"] },
      { "atomic_number": 83, "name": "Bismuth", "symbol": "Bi", "atomic_mass": 209, "valences": ["III", "V"] },
      { "atomic_number": 84, "name": "Poloni", "symbol": "Po", "atomic_mass": 209, "valences": ["II", "IV", "VI"] },
      { "atomic_number": 85, "name": "Astatin", "symbol": "At", "atomic_mass": 210, "valences": ["I", "III", "V", "VII"] },
      { "atomic_number": 86, "name": "Radon", "symbol": "Rn", "atomic_mass": 222, "valences": ["II", "IV"] },
      { "atomic_number": 87, "name": "Franci", "symbol": "Fr", "atomic_mass": 223, "valences": ["I"] },
      { "atomic_number": 88, "name": "Radi", "symbol": "Ra", "atomic_mass": 226, "valences": ["II"] },
      { "atomic_number": 89, "name": "Actini", "symbol": "Ac", "atomic_mass": 227, "valences": ["III"] },
      { "atomic_number": 90, "name": "Thori", "symbol": "Th", "atomic_mass": 232, "valences": ["IV"] },
      { "atomic_number": 91, "name": "Protactini", "symbol": "Pa", "atomic_mass": 231, "valences": ["IV", "V"] },
      { "atomic_number": 92, "name": "Urani", "symbol": "U", "atomic_mass": 238, "valences": ["IV", "VI"] },
      { "atomic_number": 93, "name": "Neptuni", "symbol": "Np", "atomic_mass": 237, "valences": ["IV", "V", "VI"] },
      { "atomic_number": 94, "name": "Plutoni", "symbol": "Pu", "atomic_mass": 244, "valences": ["IV", "V", "VI"] },
      { "atomic_number": 95, "name": "Americi", "symbol": "Am", "atomic_mass": 243, "valences": ["IV", "V", "VI"] },{ "atomic_number": 96, "name": "Curi", "symbol": "Cm", "atomic_mass": 247, "valences": ["III"] },{ "atomic_number": 97, "name": "Berkeli", "symbol": "Bk", "atomic_mass": 247, "valences": ["III", "IV"] },{ "atomic_number": 98, "name": "Californi", "symbol": "Cf", "atomic_mass": 251, "valences": ["III"] },{ "atomic_number": 99, "name": "Einsteini", "symbol": "Es", "atomic_mass": 252, "valences": ["III"] },{ "atomic_number": 100, "name": "Fermi", "symbol": "Fm", "atomic_mass": 257, "valences": ["III"] },{ "atomic_number": 101, "name": "Mendelevi", "symbol": "Md", "atomic_mass": 258, "valences": ["II", "III"] },{ "atomic_number": 102, "name": "Nobeli", "symbol": "No", "atomic_mass": 259, "valences": ["II", "III"] },{ "atomic_number": 103, "name": "Lawrenci", "symbol": "Lr", "atomic_mass": 262, "valences": ["III"] },{ "atomic_number": 104, "name": "Rutherfordi", "symbol": "Rf", "atomic_mass": 267, "valences": ["IV"] },{ "atomic_number": 105, "name": "Dubni", "symbol": "Db", "atomic_mass": 268, "valences": ["V"] },{ "atomic_number": 106, "name": "Seaborgi", "symbol": "Sg", "atomic_mass": 269, "valences": ["VI"] },{ "atomic_number": 107, "name": "Bohri", "symbol": "Bh", "atomic_mass": 270, "valences": ["VII"] },{ "atomic_number": 108, "name": "Hassi", "symbol": "Hs", "atomic_mass": 269, "valences": ["VIII"] },{ "atomic_number": 109, "name": "Meitneri", "symbol": "Mt", "atomic_mass": 278, "valences": ["II", "III", "IV"] },{ "atomic_number": 110, "name": "Darmstadti", "symbol": "Ds", "atomic_mass": 281, "valences": ["II", "IV"] },{ "atomic_number": 111, "name": "Roentgeni", "symbol": "Rg", "atomic_mass": 282, "valences": ["I"] },{ "atomic_number": 112, "name": "Copernici", "symbol": "Cn", "atomic_mass": 285, "valences": ["II"] },{ "atomic_number": 113, "name": "Nihoni", "symbol": "Nh", "atomic_mass": 286, "valences": ["I", "III"] },{ "atomic_number": 114, "name": "Flerovi", "symbol": "Fl", "atomic_mass": 289, "valences": ["II", "IV"] },{ "atomic_number": 115, "name": "Moscovi", "symbol": "Mc", "atomic_mass": 290, "valences": ["III", "V"] },{ "atomic_number": 116, "name": "Livermori", "symbol": "Lv", "atomic_mass": 293, "valences": ["II", "IV", "VII"] },{ "atomic_number": 117, "name": "Tennessine", "symbol": "Ts", "atomic_mass": 294, "valences": ["I", "III", "V", "VII"] },{ "atomic_number": 118, "name": "Oganesson", "symbol": "Og", "atomic_mass": 294, "valences": ["II", "IV"] }]
    import random
    a = int(input("up to how many elements do you wish to memorize? : ")) 
    a = [i for i in range(0, a)]
    print(a)
    while len(a) != 0 :
        l = random.randint(0,len(a)-1)
        m = a[l]
        get = valance[m]
        answers = list(input(f'what are the valances of {get["symbol"]}? : ').split())
        if get["valences"] == answers :
            print('good girl~')
        else :
            print(f'you got it wrong but that\'s okay, here is one clue. It\'s the element {get["name"]} and of atomic number {get["atomic_number"]} :3 now it is? : ')
            answers = list(input(f'what are the valances of {get["symbol"]}').split())
            if get["valences"] == answers :
                print('good girl~')
            else :
                print('Bad girl >:( youre getting punishment >:3')
        a.pop(l)
if __name__ == '__main__':
    main()
    