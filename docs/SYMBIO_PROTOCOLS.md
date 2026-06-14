# Symbiotic Protocols and Host Utility Scoring

## Core Methodology
The Vectoreek AI operates on **Opportunistic Locomotion**. It treats the entire world as a set of directed graph edges that move at different velocities.

## Host Utility Function (HUF)
The AI evaluates every detectable object $O$ in its vicinity using the HUF:

$$U(O) = (\vec{V_O} \cdot \vec{G}) \times T_O + E_h(O)$$

Where:
- $\vec{V_O}$: Velocity vector of the Host.
- $\vec{G}$: Normalized vector towards the Goal.
- $T_O$: Expected duration the Host will remain on this route.
- $E_h(O)$: Predicted energy harvest rate from the Host.

## Adhesion Mechanisms
Vectoreek modules utilize **Tuned Surface Interfacing**:
1. **Van der Waals Pads:** For smooth surfaces (glass, polished metal).
2. **Neodymium Clamps:** Active magnetic locking for steel infrastructure.
3. **Electro-Adhesive Mesh:** For porous or organic surfaces.

## Mission Phases
1. **Dormancy:** Module remains powered down in a high-traffic area.
2. **Acquisition:** Target host is identified; module physically latches during a 'touch' event.
3. **Symbiosis:** Energy is harvested; data is collected.
4. **Transfer:** If the current host deviates from the goal, the module identifies a 'crossover' point to a new host.
