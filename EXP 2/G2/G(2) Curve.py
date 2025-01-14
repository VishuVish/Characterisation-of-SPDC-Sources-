import matplotlib.pyplot as plt

file_path = 'G2Functions_with-delay.txt'
x_values = []
y_values = []

with open(file_path, 'r') as file:
    for _ in range(19):
        next(file)
    for line in file:
        x, y = line.split(";")
        x_values.append(float(x.strip()))
        y_values.append(float(y.strip()))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values,linestyle='-', color='blue', markersize=0.1)
plt.xlabel('Time delay (ns)', fontsize=14)
plt.xlim(-6.5*10**(-9),6.5*10**(-9))
plt.ylabel('g^{(2)}(τ)', fontsize=14)
plt.title('Second-order Correlation Function with Delay', fontsize=16)
plt.grid(True)
plt.show()
