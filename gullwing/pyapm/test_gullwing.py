#%% Import Dependencies
from IPython.display import display_markdown
from pyapm import panelsystem_from_json
from pyapm.classes import PanelResult
from pyapm.output.msh import panelresult_to_msh
from matplotlib.pyplot import figure

#%% Create Panel System
jsonfilepath = 'gullwing.json'
psys = panelsystem_from_json(jsonfilepath)

#%% Assemble and Solve
psys.assemble_panels()
psys.assemble_horseshoes()
psys.solve_system()

#%% Panel Result
alpha = 0.0
speed = 82.02815
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

#%% Plot Panel Drag
ypos = []
drag = []
yfrc = []
lift = []
srfc = psys.srfcs[0]
for strp in srfc.strps:
    pnl = strp.pnls[0]
    grdy = [grd.y for grd in pnl.grds]
    miny = min(grdy)
    maxy = max(grdy)
    rngy = maxy-miny
    dragval = 0.0
    yfrcval = 0.0
    liftval = 0.0
    for pnl in strp.pnls:
        dragval += pres.nfres.nffrc[pnl.ind, 0]*pres.acs.dirx
        yfrcval += pres.nfres.nffrc[pnl.ind, 0]*pres.acs.diry
        liftval += pres.nfres.nffrc[pnl.ind, 0]*pres.acs.dirz
    drag.append(dragval/rngy)
    yfrc.append(yfrcval/rngy)
    lift.append(liftval/rngy)
    ypos.append(pnl.pnto.y)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.plot(ypos, drag)
ax.set_xlim(-2.2, 0.0)
ax.set_ylabel('Induced Drag Distribution [N/m]')
_ = ax.grid(True)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.plot(ypos, yfrc)
ax.set_xlim(-2.2, 0.0)
ax.set_ylabel('Y Force Distribution [N/m]')
_ = ax.grid(True)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.plot(ypos, lift)
ax.set_xlim(-2.2, 0.0)
ax.set_ylabel('Lift Distribution [N/m]')
_ = ax.grid(True)
