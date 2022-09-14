import pylatex, math, random, sympy, numpy
from random import randrange,randint, choice
from sympy import *
from pylatex import Document, LargeText, MediumText, NewPage, Tabular, Alignat
from pylatex.utils import bold

# Wörterbuch der Rechenregeln der Integralrechnung

regeln_Aufgabe = {'1':r'\int x^n\; \mathrm{d}x = \hspace{20em}', \
                  '2':r'\int a\cdot f(x)\; \mathrm{d}x = \hspace{20em}', \
                  '3':r'\int \Big( f(x) + g(x) \Big) \; \mathrm{d}x = \hspace{20em}', \
                  '4':r'\int e^x\; \mathrm{d}x = \hspace{20em}', \
                  '5':r'\int f(ax+b) \; \mathrm{d}x = \hspace{20em}', \
                  '6':r'\int \sin x \; \mathrm{d}x = \hspace{20em}', \
                  '7':r'\int \cos x \; \mathrm{d}x = \hspace{20em}'}
regeln_lösung = {'1':r'\int x^n\; \mathrm{d}x = \frac{1}{n+1}\cdot x^{n+1} + C \quad (1P) \\', \
                 '2':r'\int a\cdot f(x)\; \mathrm{d}x = a\cdot \int f(x)\; \mathrm{d}x = a\cdot F(x) + C \quad \\', \
                 '3':r'\int \Big( f(x) + g(x) \Big) \; \mathrm{d}x = \int f(x)\; \mathrm{d}x + \int g(x) \; \mathrm{d}x \quad (1P) \\', \
                 '4':r'\int e^x\; \mathrm{d}x = e^x + C \quad (1P) \\', \
                 '5':r'\int f(ax+b) \mathrm{d}x = \frac{1}{a} \cdot F(ax+b) + C \quad (1P) \\', \
                 '6':r'\int \sin x \; \mathrm{d}x = -\cos x + C \quad (1P) \\', \
                 '7':r'\int \cos x \; \mathrm{d}x = \sin x + C \quad (1P) \\'}
r = str(random.randint(1,7))

x = symbols('x')

# Definitionen der einzelnen Funktionen

def koeffizienten_funktion(l): # erstellt die Koeffizienten eines Polynoms mit l Gliedern
    koeffizient_all = []
    for i in range(l):
        a = random.choice([-1, 1]) * random.randint(1,5)
        koeffizient_all.append(a)
    return koeffizient_all

def exponenten_funktion(l, g): # exponenten eines Polynoms mit l Gliedern und max Grades g
    exponent_all = []
    for i in range(l):
        b = random.randrange(2, g)
        while b == 0:
            b = random.randrange(2, g)
        exponent_all.append(b)
    exponent_all.sort()
    return exponent_all

def polynom(p, q):          # Polynom mit p: koeffizientenliste und q: Exponentenliste
    a = []
    a.extend(p)
    e = []
    e.extend(q)
    x = symbols('x')
    h = a.pop()*x**q.pop()
    while len(q) > 0:
        h = h + a.pop()*x**q.pop()
    a = random.choice([-1, 1]) * random.randint(1,5)
    f = a * h
    # print(f'Polynomfunktion: + {f}')
    return f

#  Polynom mit n bekannten Nullstellen

'''
n Anzahl der gewünschten Nullstellen
'''

def Nullstellen(n, q):
    nullstellen = []
    a = random.choice([-2, -1, 1, 2])
    nullstellen.append(a)
    b = 2
    while len(nullstellen) < n:
        b = -1*b*(1+random.randint(1,q)*random.choice([1, 1.5])/abs(b))
        nullstellen.append(b)
        nullstellen.sort()
    # print(f'Nullstellen aus Z: {nullstellen}')
    return nullstellen

'''
n Anzahll der Nullstellen aus Z
a Anzahl der doppelten Nullstellen aus R
'''

def Nullstellen_aus_R(n, a):
    nullstellen = []
    for i in range(n):
        b = random.choice([-1, 1]) * random.randint(1,2)
        nullstellen.append(b)
    for i in range(a):
        c = random.randint(7,30)
        c_1 = math.sqrt(c)
        c_2 = -1*math.sqrt(c)
        nullstellen.append(c_1)
        nullstellen.append(c_2)
    nullstellen.sort()
    # print(f'Nullstellen aus R: {nullstellen}')
    return nullstellen

def Funktionsgleichung_allg(p, a):
    k = []
    k = p.copy()
    x = symbols('x')
    h = (x-k.pop())
    while len(k) > 0:
        h = h*(x-k.pop())
    f = expand(h)
    f = a * f
    # print(f'Funktionsgleichung allgemein: {f}')
    return f

def Funktionsgleichung_exp():
    x = symbols('x')
    a = random.choice([-1, 1]) * random.randrange(1, 10, 1)
    b = random.choice([-1, 1]) * random.randrange(1, 20, 1)
    h = exp(a*x+b)
    # print(f'Funktionsgleichung exponentiell: {h}')
    return h

def Integral(p):
    F = integrate(p)
    # print(f'Integral: {F}')
    return F
    

def Integral_berechnen(p, a, b):
    # print(a)
    # print(b)
    F_ab = integrate(p, (x, a, b))
    # print(f'bestimmtes Integral: {F_ab}')
    return F_ab

def Partialbruchzerlegung(p, q):
    nullstellen = []
    nullstellen.extend(p)
    x = symbols('x')
    a = nullstellen.pop()
    while abs(a) > 2:
        nullstellen.append(a)
        a = nullstellen.pop(0)
    h = 1
    while len(nullstellen) > 0:
        h = h*(x-nullstellen.pop())
    f = expand(h)
    f = q*f
    # print(f'Partialbruchzerlegung: {f}')
    return f

def linearfaktor(p):
    x = symbols('x')
    h = (x - p)
    return h

def loesungen(p):
    x = symbols('x')
    nullstellen = []
    nullstellen.extend(p)
    nullstellen.reverse()
    n = 0
    h = f'x_{n} = ' + str(nullstellen.pop())
    while len(nullstellen) > 0:
        n = n + 1
        h =  h + r', \; ' + f'x_{n} = ' + str(nullstellen.pop())
    # print(h)
    return h
        
# Angaben für den Test im pdf-Dokument

Datum = NoEscape(r' \today')
Kurs = 'Grundkurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'

Art = '19. HAK - Integralrechnung '
Teil = ' Gruppe  A'



# Berechnung für die Aufgaben

# Aufgabe 2. a.
koeffizienten_2a = koeffizienten_funktion(1)
exponenten_2a = exponenten_funktion(1, 12)
funktion_2a = polynom(koeffizienten_2a, exponenten_2a)
funktion_2a_str = str(latex(funktion_2a))
integral_2a = Integral(funktion_2a)
Stammfunktion_2a = str(latex(Integral(funktion_2a)))


# Aufgabe 2. b.
koeffizienten_2b = koeffizienten_funktion(3)
exponenten_2b = exponenten_funktion(3, 12)
funktion_2b = polynom(koeffizienten_2b, exponenten_2b)
funktion_2b_str = str(latex(funktion_2b))
integral_2b = Integral(funktion_2b)
Stammfunktion_2b = str(latex(Integral(funktion_2b)))

# Aufgabe 2.c.

funktion_2c = Funktionsgleichung_exp()
Aufgabe_2c = str(latex(funktion_2c))
Ergebnis_2c = str(latex(Integral(funktion_2c)))

# Aufgabe 3.a. (Integral einer Funktion mit Nullstellen im Intervall)

faktor_3a = random.choice([-1, 1]) * random.randint(1, 10)
print('Lösungen Aufgabe 3a:')
print(f'Faktor =  {faktor_3a}')
nullstellen_3a = Nullstellen(3,3)
loesungen_3a = loesungen(nullstellen_3a)
funktion_3a = Funktionsgleichung_allg(nullstellen_3a, faktor_3a)
funktion_3a_str = str(latex(funktion_3a))
integral_3a = Integral(funktion_3a)
n_3a = []
n_3a.extend(nullstellen_3a)
n_3a.sort()
oben = n_3a.pop()
nst_im_intervall_3a = n_3a.pop()
unten = n_3a.pop()
partialbruch_3a = str(latex(apart(funktion_3a/linearfaktor(nst_im_intervall_3a))))
p_von_pqFormel = -1*(oben+unten)
if p_von_pqFormel > 0:
    p_von_pqFormel = '+' + str(p_von_pqFormel)
    print(f' p = {p_von_pqFormel}')
else:
    p_von_pqFormel = str(p_von_pqFormel)
    print(f' p = {p_von_pqFormel}')

q_von_pqFormel = oben*unten
if q_von_pqFormel < 0:
    q_von_pqFormel = '+' + str(-1*q_von_pqFormel)
    print(f' q = {q_von_pqFormel}')
else:
    q_von_pqFormel = str(q_von_pqFormel)
    print(f' q = {q_von_pqFormel}')
oben_3a = round(random.randint(int(nst_im_intervall_3a)+1,int(oben)))
unten_3a = round(random.randint(int(unten),int(nst_im_intervall_3a)-1))
linearfaktor_3a_str = str(latex(linearfaktor(nst_im_intervall_3a)))
obere_Grenze_3a = str(oben_3a)
nst_im_intervall_3a_str = str(nst_im_intervall_3a)
untere_Grenze_3a = str(unten_3a)
Stammfunktion_3a = str(latex(Integral(funktion_3a)))
Flaeche_3a_1 = Integral_berechnen(funktion_3a, unten_3a, nst_im_intervall_3a)
Flaeche_3a_2 = Integral_berechnen(funktion_3a, nst_im_intervall_3a, obere_Grenze_3a)
Flaeche_3a_1_str = str(round(Flaeche_3a_1,2))
Flaeche_3a_2_str = str(round(Flaeche_3a_2,2))
Flaeche_3a_gesamt = str(round(abs(Flaeche_3a_1)+abs(Flaeche_3a_2)))

# Aufgabe 3b (Integral zwischen zwei Funktionen)

faktor_3b_f = random.choice([-1, 1]) * random.randint(1, 10)
faktor_3b_g = random.choice([-1, 1]) * random.randint(1, 10)
nullstellen_3b_f = Nullstellen(3,3)
nullstellen_3b_g = Nullstellen(3,3)
funktion_3b_f = Funktionsgleichung_allg(nullstellen_3b_f, faktor_3b_f)
funktion_3b_f_str = str(latex(funktion_3b_f))
funktion_3b_g = Funktionsgleichung_allg(nullstellen_3b_g, faktor_3b_g)
funktion_3b_g_str = str(latex(funktion_3b_g))
funktion_3b_h = simplify(funktion_3b_f - funktion_3b_g)
funktion_3b_h_str = str(latex(funktion_3b_h))
nullstellen_3b_h = solveset(funktion_3b_h,x)
nst_durch_probieren_3b = [round(x) for x in nullstellen_3b_h if abs(x)/round(abs(x)) == 1 and abs(x) < 6]
n = 1
print('Lösungen Aufgabe 3b:')

while len(nst_durch_probieren_3b) == 0 and n < 1000:
    print(f'Anzahl der Versuche: {n}')
    n = n + 1
    faktor_3b_f = random.choice([-1, 1]) * random.randint(1, 10)
    faktor_3b_g = random.choice([-1, 1]) * random.randint(1, 10)
    nullstellen_3b_f = Nullstellen(3,3)
    nullstellen_3b_g = Nullstellen(3,3)
    funktion_3b_f = Funktionsgleichung_allg(nullstellen_3b_f, faktor_3b_f)
    funktion_3b_f_str = str(latex(funktion_3b_f))
    funktion_3b_g = Funktionsgleichung_allg(nullstellen_3b_g, faktor_3b_g)
    funktion_3b_g_str = str(latex(funktion_3b_g))
    funktion_3b_h = simplify(funktion_3b_f - funktion_3b_g)
    nullstellen_3b_h = solveset(funktion_3b_h,x)
    nst_durch_probieren_3b = [round(x) for x in nullstellen_3b_h if abs(x)/round(abs(x)) == 1 and abs(x) < 6]

print(f'Funktion f(x) = {funktion_3b_f}')
print(f'Funktion g(x) = {funktion_3b_g}')
print(f'Differenzfunktion h(x) = {funktion_3b_h}')
print(f'Schnittstellen der Funktionen f und g: {nullstellen_3b_h}')
print(f'ganzahlige Schnittstellen: {nst_durch_probieren_3b}')

nst_0_3b = nst_durch_probieren_3b.pop()
nst_0_3b_str = str(nst_0_3b)
rst_nst_3b = [x for x in nullstellen_3b_h if x != nst_0_3b]
nst_2_3b = rst_nst_3b.pop()
nst_1_3b = rst_nst_3b.pop()
p_von_pqFormel_3b = -1*(nst_1_3b + nst_2_3b)
if p_von_pqFormel_3b > 0:
    p_von_pqFormel_3b = '+' + str(p_von_pqFormel_3b)
    print(f' p = {p_von_pqFormel_3b}')
else:
    p_von_pqFormel_3b = str(p_von_pqFormel_3b)
    print(f' p = {p_von_pqFormel_3b}')

q_von_pqFormel_3b = nst_2_3b * nst_1_3b
if q_von_pqFormel_3b < 0:
    q_von_pqFormel_3b = '+' + str(-1*q_von_pqFormel_3b)
    print(f' q = {q_von_pqFormel_3b}')
else:
    q_von_pqFormel_3b = str(q_von_pqFormel_3b)
    print(f' q = {q_von_pqFormel_3b}')

partialbruch_3b = str(latex(apart(funktion_3b_h/linearfaktor(nst_0_3b))))
linearfaktor_3b_str = str(latex(linearfaktor(nst_0_3b)))
loesungen_3b = loesungen([x for x in nullstellen_3b_h if x != nst_0_3b])
nst_3b_richtige_reihenfolge = list(nullstellen_3b_h)
nst_2_3b_rr = nst_3b_richtige_reihenfolge.pop()
nst_1_3b_rr = nst_3b_richtige_reihenfolge.pop()
nst_0_3b_rr = nst_3b_richtige_reihenfolge.pop()
nst_2_3b_rr_str = str(nst_2_3b_rr)
nst_1_3b_rr_str = str(nst_1_3b_rr)
nst_0_3b_rr_str = str(nst_0_3b_rr)
Stammfunktion_3b = str(latex(Integral(funktion_3b_h)))
Flaeche_3b_1 = Integral_berechnen(funktion_3b_h, nst_0_3b_rr, nst_1_3b_rr)
Flaeche_3b_2 = Integral_berechnen(funktion_3b_h, nst_1_3b_rr, nst_2_3b_rr)
Flaeche_3b_1_str = str(round(Flaeche_3b_1,2))
Flaeche_3b_2_str = str(round(Flaeche_3b_2,2))
Flaeche_3b_gesamt = str(round(abs(Flaeche_3b_1)+abs(Flaeche_3b_2)))

print(partialbruch_3b)
print(linearfaktor_3b_str)
print(Stammfunktion_3b)
print(Flaeche_3b_1, Flaeche_3b_2)
print(Flaeche_3b_gesamt)


# der Teil in dem die PDF-Datei erzeugt wird

def Hausaufgabenkontrolle():
    geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
                    
# erste Seite

    table1 = Tabular('c|c|c|c|c|c|',row_height=1.5)
    table1.add_hline(2,6)
    table1.add_row(MediumText(bold('Torhorst - Gesamtschule')),'Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:', 'Datum:')
    table1.add_row(MediumText(bold('mit gymnasialer Oberstufe')), Klasse, Fach, Kurs, Lehrer, Datum)
    table1.add_hline(2,6)
    
    doc.append(table1)
    doc.append('\n\n')
    doc.append(LargeText(bold('\n\n ' + Art + ' \n\n')))
   
    doc.append('1. Vervollständige die Rechenregeln für Integrale.')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(regeln_Aufgabe[r])
    
    doc.append('2. Berechne die Stammfunktionen der gegebenen Funktionen.')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(r'a)\quad f(x) =' + funktion_2a_str + r'\qquad b)\quad f(x) = ' + funktion_2b_str + r'\qquad c) \quad f(x) = '+ Aufgabe_2c)
                        
    doc.append(f'3. Berechne die Nullstelle und die Fläche der gegebenen Funktion im Intervall x = {untere_Grenze_3a} und x = {obere_Grenze_3a}.')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                           agn.append(r' \qquad f(x) = ' + funktion_3a_str + r' \hspace{20em}')

    doc.append('4. Berechne die zwischen den beiden Funktionen f und g eingeschlossenen Fläche.')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                           agn.append(r' \qquad f(x) = ' + funktion_3b_f_str + r' \quad und \quad g(x) = ' + funktion_3b_g_str + r' \hspace{20em}')


    doc.append(NewPage())
    doc.append(LargeText(bold(Teil + ' - bearbeitet von:')))

    doc.generate_pdf('HAK 19. Integralrechnung Gruppe A', clean_tex=True)

# Erwartungshorizont

def Erwartungshorizont():
    geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
    doc = Document(geometry_options=geometry_options)

    doc.append(LargeText(bold(f'Lösung für {Art} {Teil} \n\n')))

    doc.append('1. Vervollständige die Rechenregeln für Integrale')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(regeln_lösung[r])

    doc.append('2. Berechne die Stammfunktionen der gegebenen Funktionen')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(r'a) \quad f(x) = ' + funktion_2a_str + '\quad hat \quad F(x) = ' + Stammfunktion_2a + r'+ C \quad (1P) \\')
                            agn.append(r'b) \quad f(x) = ' + funktion_2b_str + '\quad hat \quad F(x) = ' + Stammfunktion_2b + r'+ C \quad (2P) \\')
                            agn.append(r'c) \quad f(x) = ' + Aufgabe_2c + '\quad hat \quad F(x) = ' + Ergebnis_2c + '+ C \quad (2P)')
                            
    doc.append(f'3. Berechne die Nullstelle und die Fläche der gegebenen Funktion im Intervall x = {untere_Grenze_3a} und x = {obere_Grenze_3a}. \n\n')

    doc.append('Nullstellen: durch Probieren ergibt sich die erste Nullstelle bei x = ' + nst_im_intervall_3a_str + ' damit folgt:')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(r'(' + funktion_3a_str + '):(' + linearfaktor_3a_str + ') = ' + partialbruch_3a + r' \quad (3P) \\')
                            agn.append(r'aus \quad ' + partialbruch_3a + r' = 0 \quad folgt \quad x_{1/2} = -\frac{' + p_von_pqFormel + r' }{2} \pm \sqrt[]{ \Big(\frac{' + p_von_pqFormel + r'}{2} \Big)^2' + q_von_pqFormel + r'} = 0 \quad (3P) \\')            
                            agn.append(r' \quad Ergebnisse: \quad ' + loesungen_3a + r' \quad (3P) \\')     

    doc.append('damit ergeben sich folgende Integrale:\n')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(r' \quad \int_ {' + untere_Grenze_3a + r'}^{' + nst_im_intervall_3a_str + r'} \; ' + funktion_3a_str + r' \; \mathrm{d}x \\')
                            agn.append(r' \quad =  \Big[{' + Stammfunktion_3a + r'}\Big]_{' + untere_Grenze_3a + r'}^{' + nst_im_intervall_3a_str + r'} \quad = ' + Flaeche_3a_1_str + r'\quad (3P) \\')
                            agn.append(r' \quad \int_ {' + nst_im_intervall_3a_str + r'}^{' + obere_Grenze_3a + r'} \; ' + funktion_3a_str + r' \; \mathrm{d}x\\')
                            agn.append(r' \quad =  \Big[{' + Stammfunktion_3a + r'}\Big]_{' + nst_im_intervall_3a_str + r'}^{' + obere_Grenze_3a + r'} \quad = ' + Flaeche_3a_2_str + r'\quad (3P) \\')
                            agn.append(r' \quad A_{gesamt} = |' + Flaeche_3a_1_str + r'| + |' + Flaeche_3a_2_str + r'| \quad = ' + Flaeche_3a_gesamt + r' \quad (2P) \\')

    doc.append('4. Berechne die zwischen den beiden Funktionen f und g eingeschlossenen Fläche. \n\n')
    
    doc.append(f'Die Differenzfunktion h(x) der beiden Funktionen f und g lautet: h(x) = {funktion_3b_h_str}')
    doc.append(f'Nullstellen: durch Probieren ergibt sich die erste Nullstelle bei x = {nst_0_3b_str} damit folgt:')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(r'(' + funktion_3b_h_str + '):(' + linearfaktor_3b_str + ') = ' + partialbruch_3b + r' \quad (3P) \\')
                            agn.append(r'aus \quad ' + partialbruch_3b + r' = 0 \quad folgt \quad (1P) \\')
                            agn.append(r' \quad x_{1/2} = -\frac{' + p_von_pqFormel_3b + r' }{2} \pm \sqrt[]{ \Big(\frac{' + p_von_pqFormel_3b + r'}{2} \Big)^2' + q_von_pqFormel_3b + r'} = 0 \quad (2P) \\') 
                            agn.append(r' \quad Ergebnisse: \quad ' + loesungen_3b + r' \quad (3P) \\')     

    doc.append('damit ergeben sich folgende Integrale:\n')
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
                            agn.append(r' \quad \int_ {' + nst_0_3b_rr_str + r'}^{' + nst_1_3b_rr_str + r'} \; ' + funktion_3b_h_str + r' \; \mathrm{d}x \\')
                            agn.append(r' \quad =  \Big[{' + Stammfunktion_3b + r'}\Big]_{' + nst_0_3b_rr_str + r'}^{' + nst_1_3b_rr_str + r'} \quad = ' + Flaeche_3b_1_str + r'\quad (3P) \\')
                            agn.append(r' \quad \int_ {' + nst_1_3b_rr_str + r'}^{' + nst_2_3b_rr_str + r'} \; ' + funktion_3b_h_str + r' \; \mathrm{d}x\\')
                            agn.append(r' \quad =  \Big[{' + Stammfunktion_3b + r'}\Big]_{' + nst_1_3b_rr_str + r'}^{' + nst_2_3b_rr_str + r'} \quad = ' + Flaeche_3b_2_str + r'\quad (3P) \\')
                            agn.append(r' \quad A_{gesamt} = |' + Flaeche_3b_1_str + r'| + |' + Flaeche_3b_2_str + r'| \quad = ' + Flaeche_3b_gesamt + r' \quad (2P) \\')
                   

                        
    doc.generate_pdf('HAK 19. Integralrechnung Gruppe A Lsg', clean_tex=True)

# Druck der Seiten

Hausaufgabenkontrolle()
Erwartungshorizont()
