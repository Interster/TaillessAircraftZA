# Gull wing planform analysis

In order to establish a baseline for the gull wing planform analysis, it is required to define the baseline geometry.  The following geometry was taken from various sources.

### Geometry

The following geometry is defined:

Inboard dihedral is 3 degrees.

Outboard anhedral is 4 degrees.

Inboard chord is constant at 1100mm.

Outboard chord tapers from 1100mm to 700mm linearly.

There is linear twist from half of semispan to the tip (outboard section) at 3.5 degrees.  The wing is twisted around the trailing edge.

The outboard wing section is swept back at 30 degrees.

The inboard section is swept forward 6 degrees.

![1_PlanformGullwingGeometry](Pictures/1_PlanformGullwingGeometry.png)



![2_Twist](Pictures/2_Twist.png)

### Reynolds numbers

Let us assume the aircraft will have a trim speed of 120kph.  Then the Reynolds number at the root and tip can be calculated as follows:
$$
R_{e_{root}} = \frac{\rho V d}{\mu} = \frac{1 kg/m^3 \cdot 33.3m/s \cdot 1.1m}{1.98 \times 10^{-5}} = 1.85 \cdot 10^6
$$

$$
R_{e_{tip}} = \frac{\rho V d}{\mu} = \frac{1 kg/m^3 \cdot 33.3m/s \cdot 0.7m}{1.98 \times 10^{-5}} = 1.18 \cdot 10^6
$$

The Reynolds numbers here show that it is very challenging to obtain similarity with a scale model in a wind tunnel as tunnel speeds are lower and the model is significantly smaller than the full scale aircraft.

