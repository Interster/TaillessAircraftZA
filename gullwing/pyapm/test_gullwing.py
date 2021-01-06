#%% Import Dependencies
from IPython.display import display_markdown
from pyapm import panelsystem_from_json
from pyapm.classes import PanelResult
from pyapm.output.msh import panelresult_to_msh
from matplotlib.pyplot import figure

#%% Create Panel System
jsonfilepath = 'gullwing.json'
psys = panelsystem_from_json(jsonfilepath)
display_markdown(psys)

#%% Assemble and Solve
psys.assemble_panels()
psys.assemble_horseshoes()
psys.solve_system()

#%% Panel Result
alpha = 2.0
speed = 50.0
rho = 1.225

pres = PanelResult(f'AoA = {alpha:.1f} degrees', psys)
pres.set_density(rho)
pres.set_state(alpha=alpha, speed=speed)

#%% Solve and Display Panel Result
display_markdown(pres)
display_markdown(pres.surface_loads)

#%% Output MSH File
mshfilepath = psys.name + '.msh'
panelresult_to_msh(pres, mshfilepath)

#%% Coefficient Distribution Plots
axt = psys.plot_strip_twist_distribution()
_ = axt.set_ylabel('Strip Twist [deg]')
_ = axt.set_xlabel('Span-Wise Coordinate - y [m]')
axt = psys.plot_strip_chord_distribution()
_ = axt.set_ylabel('Strip Chord [m]')
_ = axt.set_xlabel('Span-Wise Coordinate - y [m]')
axw = psys.plot_strip_width_distribution()
_ = axw.set_ylabel('Strip Width [m]')
_ = axw.set_xlabel('Span-Wise Coordinate - y [m]')
axd = pres.plot_strip_drag_force_distribution(normalise=True)
_ = axd.set_ylabel('Drag Force Coefficient')
_ = axd.set_xlabel('Span-Wise Coordinate - y')
axs = pres.plot_strip_side_force_distribution(normalise=True)
_ = axs.set_ylabel('Side Force Coefficient')
_ = axs.set_xlabel('Span-Wise Coordinate - y')
axl = pres.plot_strip_lift_force_distribution(normalise=True)
_ = axl.set_ylabel('Lift Force Coefficient')
_ = axl.set_xlabel('Span-Wise Coordinate - y')
