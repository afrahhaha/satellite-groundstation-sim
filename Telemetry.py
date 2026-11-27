# Real-time telemetry plot using SIMULATED sensor data.
# The values are random numbers in typical ranges, standing in for a live
# satellite/avionics downlink. Close the window or press Ctrl+C to stop.
import matplotlib.pyplot as plt
import random
import time

# initialization of vectors
time_data = []
temperature_data = []
voltage_data = []
current_data = []

start_time = time.time()

plt.ion()
fig, ax = plt.subplots()

try:
    while plt.fignum_exists(fig.number):
        t = time.time() - start_time
        temperature = random.uniform(20, 40)    # °C   (simulated)
        voltage = random.uniform(10.0, 12.0)    # V    (simulated)
        current = random.uniform(0.1, 2.0)      # A    (simulated)

        # append the new sample
        time_data.append(t)
        temperature_data.append(temperature)
        voltage_data.append(voltage)
        current_data.append(current)

        # redraw the frame
        ax.clear()
        ax.plot(time_data, temperature_data, label='Temperature (°C)')
        ax.plot(time_data, voltage_data, label='Voltage (V)')
        ax.plot(time_data, current_data, label='Current (A)')

        ax.legend()
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Value')
        ax.set_title('Simulated Telemetry')

        plt.pause(0.5)  # update every 0.5 s
except KeyboardInterrupt:
    pass
