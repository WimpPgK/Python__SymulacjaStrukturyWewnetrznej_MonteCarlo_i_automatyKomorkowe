import numpy as np
import matplotlib.pyplot as plt


def przepis_relaksacyjny(fi, omega, ro, dx):
    for i in range(1,60):
        for j in range(1,60):
            fi[i][j] = (1-omega)*fi[i][j] + omega/4*(fi[i+1][j] + fi[i-1][j] + fi[i][j+1] + fi[i][j-1] + ro[i][j]*dx**2)


def calka_dzialania(fi, ro, dx):
    a = 0
    for i in range(1,60):
        for j in range(1,60):
            a = a + (0.5*( ((fi[i+1][j]-fi[i-1][j])/(2*dx))**2 + ((fi[i][j+1]-fi[i][j-1])/(2*dx))**2 ) - ro[i][j]*fi[i][j])*dx**2
    return a


def main():
    for w in [1, 1.2, 1.5, 1.9, 1.95, 1.99, 5, 8]:
        omega = w
        fi = np.zeros((61, 61), float)
        ro = np.zeros((61, 61), float)
        dx = 1
        for i in range(20, 41):
            for j in range(20, 41):
                ro[i][j] = 1
        t = 0
        A = []
        T = []

        while t < 1000:
            if t % 100 == 0:
                print(t)
            przepis_relaksacyjny(fi, omega, ro, dx)
            a = calka_dzialania(fi, ro, dx)
            t = t + 1
            A.append(a)
            T.append(t)


        plt.plot(T, A, label = "omega = "+str(omega))
        plt.xlabel("Ilość iteracji")
        plt.ylabel("Wartość całki działania")
        plt.xscale("log")
        plt.legend()
    plt.show()


main()