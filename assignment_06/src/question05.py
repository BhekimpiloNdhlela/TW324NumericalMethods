def lorenz_system_solver(h, N, s=10.0, r=28.0, b=8.0/3.0):
    # Need one more for the initial values
    empty_vector  = lambda size   : zeros((size + 1,), dtype=float)
    lorenz_system = lambda x, y, z: (s*(y - x), x*(r -z) - y , x*y - b*z)
    next          = lambda p_old, slope   : p_old + (slope * h) # euler's Method
    x, y, z       = empty_vector(N), empty_vector(N), empty_vector(N)

    x[0], y[0], z[0] = -14.0, -15.0, 20.0
    for i in range(1, N+1):
        dx  , dy  , dz   = lorenz_system(x[i-1], y[i-1], z[i-1])
        x[i], y[i], z[i] = next(x[i-1], dx), next(y[i-1], dy), next(z[i-1], dz)
    return x, y, z

def plot_lorenz_system_solution(x, y, z):
    ax = plt.figure().gca(projection='3d')
    ax.plot(x, y, z, 'co',lw=2.1)
    ax.plot(x, y, z, 'm--',lw=.5)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz System Solution")
    plt.show()

if __name__ == "__main__":
    from numpy import zeros
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    x, y, z = lorenz_system_solver(0.01, 10000)
    plot_lorenz_system_solution(x, y, z)
