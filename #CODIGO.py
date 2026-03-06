
import math

def calcular_caso(nombre,d,Ma,Mm,Ta,Tm,Sut,Sy,Se,Kf,Kfs):

    sigma_a = Kf*(32*Ma)/(math.pi*d**3)
    sigma_m = Kf*(32*Mm)/(math.pi*d**3)
    tau_a   = Kfs*(16*Ta)/(math.pi*d**3)
    tau_m   = Kfs*(16*Tm)/(math.pi*d**3)

    sigma_a_p = math.sqrt(sigma_a**2 + 3*tau_a**2)
    sigma_m_p = math.sqrt(sigma_m**2 + 3*tau_m**2)

    sigma_max = math.sqrt((sigma_m+sigma_a)**2 + 3*(tau_m+tau_a)**2)

    ny = Sy/sigma_max

    n_goodman   = 1/((sigma_a_p/Se)+(sigma_m_p/Sut))
    n_soderberg = 1/((sigma_a_p/Se)+(sigma_m_p/Sy))
    n_asme      = 1/math.sqrt((sigma_a_p/Se)**2+(sigma_m_p/Sy)**2)

    A = sigma_a_p/Se
    B = sigma_m_p/Sut
    n_gerber = (-A+math.sqrt(A**2+4*B**2))/(2*B**2)

    return [
        nombre,
        sigma_a, sigma_m,
        tau_a, tau_m,
        sigma_a_p, sigma_m_p,
        sigma_max,
        ny,
        n_goodman,
        n_soderberg,
        n_gerber,
        n_asme
    ]


def imprimir_tabla(resultados):

    encabezados = [
        "Caso",
        "sigma_a",
        "sigma_m",
        "tau_a",
        "tau_m",
        "sigma_a'",
        "sigma_m'",
        "sigma_max'",
        "n_y",
        "Goodman",
        "Soderberg",
        "Gerber",
        "ASME"
    ]

    ancho = 12

    print("="*160)
    for h in encabezados:
        print(f"{h:<{ancho}}", end="")
    print()
    print("="*160)

    for fila in resultados:
        for i,v in enumerate(fila):
            if i == 0:
                print(f"{v:<{ancho}}", end="")
            else:
                print(f"{v:<{ancho}.3f}", end="")
        print()

    print("="*160)


print("\nSOLUCIÓN DISEÑO DE EJES\n")

resultados = []


# ----- CASO 1 -----
q=0.85
q_c=0.88
Kt=1.68
Kts=1.48

Kf=1+q*(Kt-1)
Kfs=1+q_c*(Kts-1)

resultados.append(
    calcular_caso(
        "CASO1",
        1.10,1260,0,0,1100,
        105000,82000,30000,
        Kf,Kfs
    )
)


# ----- CASO 2 -----
resultados.append(
    calcular_caso(
        "CASO2",
        1.10,1260,0,0,1100,
        105000,82000,30000,
        Kf,Kfs
    )
)


# ----- CASO 3 -----
resultados.append(
    calcular_caso(
        "CASO3",
        0.10,70,55,45,35,
        700e6,560e6,210e6,
        2.2,1.8
    )
)


imprimir_tabla(resultados)
