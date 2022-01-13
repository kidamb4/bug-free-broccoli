from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = coeffs

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""

        a0 = self.coeffs[0] + other.coeffs[0]
        a1 = self.coeffs[1] + other.coeffs[1]
        a2 = self.coeffs[2] + other.coeffs[2]

        return Poly2(a0,a1,a2)

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""

        a0 = self.coeffs[0] - other.coeffs[0]
        a1 = self.coeffs[1] - other.coeffs[1]
        a2 = self.coeffs[2] - other.coeffs[2]

        return Poly2(a0,a1,a2)

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        def sign(a): 
            if (a<0):
                return "-"
            return "+"

        a,b,c= self.coeffs[2],self.coeffs[1],self.coeffs[0]
        sa,sb,sc = sign(a),sign(b),sign(c)

        return f" {sa}{abs(a)}X^2 {sb}{abs(b)}X {sc}{abs(c)}"

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        a,b,c= self.coeffs[2],self.coeffs[1],self.coeffs[0]

        delta = b**2 - 4*a*c

        if delta < 0:
            x0 = f" {-b/(2*a)} + {sqrt(delta)/(2*a)}"
            x1 = f" {-b/(2*a)} - {sqrt(delta)/(2*a)}"

            x = (x0,x1)

        elif delta == 0:
            x = -b/(2*a)

        else :
            x0 = (-b + sqrt(delta))/(2*a)
            x1 = (-b - sqrt(delta))/(2*a)

            x = (x0,x1)
        
        return x 

    def __val(self, x): #__ privée
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        a,b,c = self.coeffs[2],self.coeffs[1],self.coeffs[0]
        return a*(x**2) + b*x + c

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""

        lsp = list(range(0,20,2))  # absicces
        f_lsp = list(self.__val(k) for k in lsp) # ordonnées 


        axes = plt.gca() # création des axes
        axes.grid(True) # ajout de la grille en fond 
        axes.set_xlabel('Abscisses') # écriture des noms au niveau des l'absicce
        axes.set_ylabel('Ordonnées') # écriture des noms au niveau de l'ordonnée

        plt.scatter(lsp,f_lsp,marker = "x",color = "green") # tracé
        
        plt.title(self.__str__())
        plt.show() # affichage de l'image



if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
    
    # p4 = Poly2(*[1,0,1])
    # print(p4.val(5))