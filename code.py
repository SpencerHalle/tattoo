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
x       = 7.63  # My measurement value
sigma   = 1.5  # My measurement std

mu0     = -1.92 # My prior mean
sigma0  = 1.893 # My prior std

## Viewing parameters
y_max = 20
y_min = -20
plotting_points = 1000
plotting_min = -10
plotting_max =  15

## Actual math
y_list = np.linspace(y_min,y_max,plotting_points) # y is my dimension

prior_raw       = np.exp(-(mu0 - y_list)**2 / (2 * sigma0**2))
observed_raw    = np.exp(-(x   - y_list)**2 / (2 * sigma **2))
posterior_raw   = np.exp(-.5*((y_list - mu0)**2 / sigma0**2 + (y_list - x)**2 / sigma**2))

prior_modifier      = 1 / np.sqrt(2 * np.pi * sigma0 ** 2)
observed_modifier   = 1 / np.sqrt(2 * np.pi * sigma  ** 2)
posterior_modifier  = 1 / np.sqrt(2 * np.pi * posterior_raw.std() ** 2) # Definitely wrong

prior       = prior_raw     * prior_modifier
observed    = observed_raw  * observed_modifier
posterior   = posterior_raw * posterior_modifier

## Plotting

plt.figure(0)
plt.xlim(plotting_min,plotting_max)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.plot(y_list, prior      ,label="Prior")
plt.plot(y_list, observed   ,label="Observed")
plt.plot(y_list, posterior  ,label="Posterior")
# plt.legend()
plt.tight_layout()
plt.axis('off')
plt.savefig("tattoo.png")

