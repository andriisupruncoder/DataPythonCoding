import numpy as np 
import matplotlib.pyplot as plt 

# to generate the x values
x = np.linspace(-5, 5, 400)

f_x = np.sin(x) + x**2

# Create the plot with a pink background
plt.figure(figsize=(8, 6))
# Plot the function
plt.plot(x, f_x, label='$f(x) = \sin(x) + x^2$', color='blue')
# Set the plot background color to pink
plt.fill_between(x, f_x, color='pink', alpha=0.5)
# Set the axis labels
plt.xlabel('x')
plt.ylabel('f(x)')
# Set the title
plt.title('Plot of $f(x) = \sin(x) + x^2$ with Pink Background')
plt.legend()
plt.grid(True)
plt.show()