from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft
from matplotlib import text

# Colors.
action_color = {"ec": "#f89406"}
faded_color = {"ec": "#dddddd"}


# Instantiate the PGM.
pgm = daft.PGM([6.3, 5.55], origin=[0.3, 0.3])

# Hierarchical parameters.
#pgm.add_node(daft.Node("theta_prior", r"$blah$", 5, 1, fixed=True))
#pgm.add_node(daft.Node("alpha", r"$\alpha_k$", 1, 1, fixed=True))


# Latent variable.
pgm.add_node(daft.Node("x_old", r"$(p_0,p_1)$", 1, 3, fixed=True))
pgm.add_node(daft.Node("z_old", r"$p(\mathbf{z})$", 1, 2, fixed=True))
pgm.add_node(daft.Node("x", r"$x$", 3, 3))
pgm.add_node(daft.Node("z", r"$\mathbf{z}$", 3, 2))
pgm.add_node(daft.Node("payoff", r"$\Gamma$", 4, 4))

# Yes, this is a stupid way to add more txt, but I don't see how to otherwise!!
pgm.add_node(daft.Node("q1", r'\texttt{"serious" action}', 4, 5.5,plot_params={"ec": "none"}))
pgm.add_node(daft.Node("q2", r'\texttt{payoff}', 4.75, 4,plot_params={"ec": "none"}))
pgm.add_node(daft.Node("q3", r'\texttt{sensory}', 2, 1.6,plot_params={"ec": "none"}))
pgm.add_node(daft.Node("q4", r'\texttt{action}', 2, 1.4,plot_params={"ec": "none"}))

# Data.
AFTER=True
pgm.add_node(daft.Node("y", r"$\mathbf{y}$", 3, 1, observed=AFTER))
pgm.add_node(daft.Node("sensor_action", r"$a$", 2, 1, plot_params=action_color, observed=AFTER))
pgm.add_node(daft.Node("actual_action", r"$b$", 4, 5, plot_params=action_color, observed=False))

# Add in the edges.
pgm.add_edge("x_old", "x")
pgm.add_edge("z_old", "z")
pgm.add_edge("x", "z")
pgm.add_edge("z", "y")
pgm.add_edge("actual_action", "payoff")
pgm.add_edge("sensor_action", "y")
pgm.add_edge("x", "payoff")

# And a plate.
# pgm.add_plate(daft.Plate([0.5, 0.5, 3, 1], label=r"$k = 1, \cdots, K$",shift=-0.1))

# Render and save.
pgm.render()
FILENAME = "change_hider_PGM"
#pgm.figure.savefig(FILENAME+".pdf")
pgm.figure.savefig(FILENAME+".png", dpi=150)
print "Wrote image to ",FILENAME
