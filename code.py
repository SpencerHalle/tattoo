"""
So, this tattoo will be a depiction of the prior,
the observation, and the posterior distributions.

I will probably try a couple of iterations of this
just to sort of get it down. I'm doing this 
without ai coding aids, because this feels
imporant and personal to me

I will have this code reviewed before I put this
on my body wrong
"""

import numpy as np
import matplotlib.pyplot as plt

## Defining parameters
x       = 7.70  # My measurement value
sigma   = 2.0  # My measurement std

mu0     = -1.60 # My prior mean
sigma0  = 3.000 # My prior std

## Viewing parameters
y_max = 20
y_min = -20
plotting_points = 1000
plotting_min = -10
plotting_max =  15
plot_y_min = 0
plot_y_max = 0.50

## Actual math
y_list = np.linspace(y_min,y_max,plotting_points) # y is my dimension

prior       = (1 / (sigma0 * np.sqrt(2 * np.pi))) * np.exp(-(mu0 - y_list)**2 / (2 * sigma0**2))
observed    = (1 / (sigma  * np.sqrt(2 * np.pi))) * np.exp(-(x   - y_list)**2 / (2 * sigma **2))

<<<<<<< HEAD

prior_modifier      = 1 / (sigma0 * np.sqrt(2 * np.pi))
observed_modifier   = 1 / (sigma  * np.sqrt(2 * np.pi))
posterior_modifier  = 1 / (posterior_raw.std() * np.sqrt(2 * np.pi))

=======
>>>>>>> fix_posterior

sigma_posterior = np.sqrt(1/((1/sigma0**2)+(1/sigma**2)))
mu_posterior    = sigma_posterior ** 2 * (mu0/sigma0**2 + x/sigma**2) 

posterior   = (1 / (sigma_posterior * np.sqrt(2 * np.pi))) * np.exp(-(mu_posterior   - y_list)**2 / (2 * sigma_posterior **2))

## Plotting

plt.figure(0)
plt.xlim(plotting_min,plotting_max)
plt.ylim(plot_y_min, plot_y_max)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.plot(y_list, prior      ,color='black', linewidth=2, label="Prior")
plt.plot(y_list, observed   ,color='black', linewidth=2, label="Observed")
plt.plot(y_list, posterior  ,color='black', linewidth=4, label="Posterior")
# plt.legend()
plt.tight_layout()
plt.axis('off')
plt.savefig("tattoo.png")

