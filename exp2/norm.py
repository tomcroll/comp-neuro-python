from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#initialize a normal distribution with frozen in mean=-1, std. dev.= 1
rv = norm(loc = 5., scale = 0.5)
rv1 = norm(loc = 7, scale = 1)

x = np.arange(0, 10, .1)

#plot the pdfs of these normal distributions 
plt.plot(x, rv.pdf(x), x, rv1.pdf(x))
plt.show()