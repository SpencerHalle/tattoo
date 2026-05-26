import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
init_x = 4.0      # Measurement value
init_sigma = 1.5  # Measurement std
init_mu0 = 0.0    # Prior mean
init_sigma0 = 2.0 # Prior std

# Viewing parameters
y_min, y_max = -10, 15
plotting_points = 1000
y_list = np.linspace(y_min, y_max, plotting_points)

def calculate_distributions(x, sigma, mu0, sigma0):
    # Corrected normalization: sigma is outside the square root
    prior = (1 / (sigma0 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y_list - mu0) / sigma0)**2)
    observed = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y_list - x) / sigma)**2)
    
    # Analytical posterior calculation
    post_var = 1 / ((1 / sigma0**2) + (1 / sigma**2))
    post_sigma = np.sqrt(post_var)
    post_mu = post_var * ((mu0 / sigma0**2) + (x / sigma**2))
    
    posterior = (1 / (post_sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y_list - post_mu) / post_sigma)**2)
    
    return prior, observed, posterior

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.35) # Make room for sliders at the bottom

# Initial plot
prior_init, obs_init, post_init = calculate_distributions(init_x, init_sigma, init_mu0, init_sigma0)

l_prior, = ax.plot(y_list, prior_init, label="Prior", color='blue', linewidth=2)
l_obs, = ax.plot(y_list, obs_init, label="Observed", color='orange', linewidth=2)
l_post, = ax.plot(y_list, post_init, label="Posterior", color='green', linewidth=2)

ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax.set_xlim(-6, 10)
ax.legend()

# We leave axis on while tweaking so you can see the scale, 
# but you can toggle this off for the final screenshot/save
# ax.axis('off') 

# Define slider axes [left, bottom, width, height]
ax_x = plt.axes([0.15, 0.20, 0.65, 0.03])
ax_sigma = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_mu0 = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_sigma0 = plt.axes([0.15, 0.05, 0.65, 0.03])

# Create sliders
s_x = Slider(ax_x, 'Obs Value (x)', -6.0, 10.0, valinit=init_x)
s_sigma = Slider(ax_sigma, 'Obs Std', 0.5, 5.0, valinit=init_sigma)
s_mu0 = Slider(ax_mu0, 'Prior Mean', -6.0, 10.0, valinit=init_mu0)
s_sigma0 = Slider(ax_sigma0, 'Prior Std', 0.5, 5.0, valinit=init_sigma0)

# Update function called when sliders change
def update(val):
    pr, ob, po = calculate_distributions(s_x.val, s_sigma.val, s_mu0.val, s_sigma0.val)
    
    l_prior.set_ydata(pr)
    l_obs.set_ydata(ob)
    l_post.set_ydata(po)
    
    # Dynamically adjust y-axis limit based on the highest peak so it doesn't clip
    max_height = max(np.max(pr), np.max(ob), np.max(po))
    ax.set_ylim(-0.02, max_height * 1.1)
    
    fig.canvas.draw_idle()

# Attach update function to sliders
s_x.on_changed(update)
s_sigma.on_changed(update)
s_mu0.on_changed(update)
s_sigma0.on_changed(update)

# Initialize y-axis limits
update(None)

plt.show()
