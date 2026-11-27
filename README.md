# RocketLeague: Avionics SIG Assignment

My submission for the NITK Rocket League Avionics SIG assignment. It covers satellite tracking and ground-station handover, rocket flight simulation, real-time telemetry plotting, and basic Arduino I/O.

## Contents

| File | What it does |
|---|---|
| `HandOver_Simulation.py` | Propagates the ISS orbit from a TLE with Skyfield, plots its ground track, and logs handovers between two ground stations (Bengaluru, Trivandrum) using a 10° elevation mask. |
| `MaxVandT.py` | Simulates a vertical rocket flight (powered ascent, then ballistic coast) and reports the maximum velocity and altitude, checked against the analytic solution. |
| `Telemetry.py` | Live-updating plot of temperature, voltage and current. Uses **simulated** (random) data in place of a real downlink. |
| `Arduino/ButtonLED` | LED on while a button is held. |
| `Arduino/BinaryCounter` | 4-bit binary counter (0–15) on four LEDs, with a debounced push button. |
| `Arduino/PotDimmer` | Potentiometer controls LED brightness via PWM. |

## Running

```
pip install numpy matplotlib skyfield
python HandOver_Simulation.py
python MaxVandT.py
python Telemetry.py
```

Open each Arduino sketch folder in the Arduino IDE.

## Tinkercad circuits

- [Task 1](https://www.tinkercad.com/things/eawZW6LQ0fM/editel?returnTo=%2Fdashboard&sharecode=fOnbhJLf8IrwkB0u4JmM-FzWl5wEIzXrhUbVIpVkmIQ)
- [Task 2](https://www.tinkercad.com/things/lKAOquQibA7/editel?sharecode=B3Yp8Zofydtt71hg8PQi2FqUPbz468YAo9Oj-WLG6Yk)
- [Task 3](https://www.tinkercad.com/things/k4Hwa6etq5L/editel?sharecode=ai5RcPW1sPqFH2a5IRL0nhPPKm2wDeBtQbfo308rRis)
- [Task 4](https://www.tinkercad.com/things/9C9aE0aqXwJ/editel?sharecode=rn6gZdgCpDnyOH6bd62WIiIB33__HyEneyWRjF0F7VM)

## Notes

### Python/NumPy basics used
- `np.arange(0, 100, 1)` creates an array of the integers 0 to 99 (the stop value is excluded).
- NumPy arrays are optimized for numerical computation.
- `fig.add_subplot(nrows, ncols, index)` adds a set of axes to a figure.
- `np.eye(100)` creates a 100×100 identity matrix.
- `random.uniform(20, 40)` returns a random float between 20 and 40.

### Satellite tracking workflow
1. **Get TLE data** from Space-Track.org (element sets, ELSET). Example: ISS (ZARYA), NORAD ID 25544, low Earth orbit at about 400 km.
   A TLE encodes the orbital elements: inclination (°), RAAN (°), eccentricity, argument of perigee (°), mean anomaly (°), mean motion (rev/day), and epoch.
2. **Propagate the orbit** with `skyfield.api`:
   1. Define the satellite from its TLE: `sat = EarthSatellite(line1, line2, "ISS (ZARYA)")`
   2. Load a timescale for the propagation times.
   3. `sat.at(t)` gives the geocentric (ECI) position vector at each time.

### Coordinate systems for the satellite position
1. **Earth-Centered, Earth-Fixed (ECEF):** x, y, z with the centre of the Earth as origin, rotating with the Earth.
2. **Geodetic (latitude, longitude, height):** relative to a reference ellipsoid such as WGS 84.
   - Latitude (φ): angle north or south of the equator.
   - Longitude (λ): angle east or west of the prime meridian.
   - Ellipsoidal height (h): altitude above the ellipsoid surface.
3. **Keplerian elements:** inclination, RAAN, eccentricity, argument of perigee, mean anomaly, mean motion, epoch.

### Visibility from a ground station
- `(sat - station).at(t)` gives the satellite's position in the station's topocentric frame; `.altaz()` returns elevation, azimuth and range.
- In theory the satellite is visible above 0° elevation. In practice, for LEO, a 5–10° elevation mask is used to allow for terrain and atmospheric effects.
