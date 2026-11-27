# Vertical rocket flight: find maximum altitude and maximum velocity.
# Powered ascent for the burn time, then ballistic coast until the rocket
# returns to the ground. Integrated with semi-implicit Euler.

import matplotlib.pyplot as plt

# given
thrust = 50000      # N
m = 1000            # kg (assumed constant)
g = 9.8             # m/s^2, magnitude of gravity (acts downward)
burn_time = 10.0    # s
dt = 0.01           # s

burn_steps = round(burn_time / dt)   # integer step count avoids float drift in t
step = 0
t, h, v = 0.0, 0.0, 0.0
ts, hs, vs = [t], [h], [v]

while True:
    # net acceleration: thrust up minus gravity during the burn, gravity only after
    a = thrust / m - g if step < burn_steps else -g

    v = v + a * dt
    h = h + v * dt
    step += 1
    t = step * dt

    if h < 0:           # rocket has hit the ground
        break

    ts.append(t)
    hs.append(h)
    vs.append(v)

max_velocity = max(vs)
max_alt = max(hs)
t_apogee = ts[hs.index(max_alt)]

# analytic check (no drag, constant mass)
a_burn = thrust / m - g
v_burnout = a_burn * burn_time
h_burnout = 0.5 * a_burn * burn_time ** 2
h_apogee_exact = h_burnout + v_burnout ** 2 / (2 * g)

print(f"Maximum velocity : {max_velocity:.1f} m/s (exact {v_burnout:.1f} m/s, at burnout)")
print(f"Maximum altitude : {max_alt:.1f} m at t = {t_apogee:.1f} s (exact {h_apogee_exact:.1f} m)")
print(f"Flight time      : {ts[-1]:.1f} s")

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].plot(ts, vs, 'b', label='Velocity')
axs[0].axvline(burn_time, color='gray', linestyle='--', label='Burnout')
axs[0].set_ylabel('Velocity (m/s)')
axs[0].set_title('Velocity vs Time')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(ts, hs, 'r', label='Altitude')
axs[1].axvline(burn_time, color='gray', linestyle='--', label='Burnout')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Altitude (m)')
axs[1].set_title('Altitude vs Time')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
