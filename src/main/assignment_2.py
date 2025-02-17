import numpy as np

def Neville(x,y,x_value):
    n = len(x)
    
    M = [[0 for _ in range(n)] for _ in range(n)] # Empty 2D array to fit any array with multiple values
    
    for i in range(n):
        M[i][0] = y[i]
    
    for i in range(0,n):
        for j in range(1,i+1):
            term1 = (x_value - x[i - j]) * M[i][j-1]
            term2 = (x_value - x[i]) * M[i-1][j-1]
            
            M[i][j] = (term1 - term2) / (x[i] - x[i-j])
    
    return M[2][2] # 2nd interpolating value


def NewtonForward(x,y,x_value):
    n = len(x)
    N = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        N[i][0] = y[i]
        
    for i in range(1,n):
        for j in range(1,i+1):
                N[i][j] = (N[i][j-1] - N[i-1][j-1]) / (x[i] - x[i-j])
                
                
    # Below is the formula for Newton's Forward Approximations

    h = x[1] - x[0]         # Interval size
    u = (x_value - x[0]) / h   # Calculating u
    approx = y[0] # Initial approximation (y0)
    u_term = 1
    factorial = 1

    for j in range(1, n):
        u_term *= (u - (j - 1))  # u(u-1)(u-2)...
        factorial *= j # Factorial: 1!, 2!, 3!...
        approx += (u_term * N[i][j]) / factorial
        approx += u_term # Adding the term (previous) to approximation
    
    # 1st, 2nd, 3rd degree values with approximating value at x = 7.3
    print(f"{N[1][1]}\n{N[2][2]}\n{N[3][3]}\n\n\nProblem 3: Approximate f(7.3)\n{approx}")

def DivDiff(x,y,y_p):
    n = len(x)
    
    z = [xi for xi in x for _ in (0, 1)] # Duplicates the x value parameter
    # The array (similar to M and N) will duplicate the values inside the matrix due to the presence of 2
    O = [[0 for _ in range(2*n)] for _ in range(2*n)]
    
    for i in range(n):
        # Duplicate x and y values respectively
        O[2*i][0] = y[i]
        O[2*i+1][0] = y[i]
        
        # 3rd column derivatives
        O[2*i+1][1] = y_p[i]
        if (i != 0):
            O[2*i][1] = (O[2*i][0] - O[2*i-1][0]) / (z[2*i] - z[2*i-1])
        
        # Iterate by column, then by row for 4th and 5th column values
    for j in range(2,2*n):
        for i in range(j,2*n):
            O[i][j] = (O[i][j - 1] - O[i - 1][j - 1]) / (z[i] - z[i - j])
                

    for i in range(2 * n):
        DivValues = f"[{z[i]:1e}  " + "  ".join(f"{O[i][j]:1e}" for j in range(2 * n - 2)) + "]" # -2 removes the last 2 columns
        print(DivValues)


def CubicSpline(x_v,y_v):
    
    x = np.array(x_v, dtype=float) # array for x
    y = np.array(y_v, dtype=float) # array for y
    n = len(x) - 1  

    h = np.diff(x)  # Step sizes
    A = np.zeros((n+1, n+1))  # Initialize Matrix A
    B = np.zeros(n+1)  # Initialize Vector B

    # Boundary conditions (top and bottom row are all 0s except 1 in first and last position)
    A[0, 0], A[-1, -1] = 1, 1  

    # Fill in matrix A and vector B
    for i in range(1, n):
        A[i,i-1] = h[i-1]
        A[i,i] = 2 * (h[i-1] + h[i])
        A[i,i+1] = h[i]
        B[i] = (6 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])) / 2

    # Solving vector x
    x = np.linalg.solve(A, B)
    
    for row in A:
        print("["+ " ".join(f"{num:.0f}." for num in row) + "]") # Print the matrix in proper format
        
    print(B)
        
    print(x)

    