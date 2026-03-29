import math

G = 6.674e-11
M = 5.972e24     
R = 6.371e6     
g = 9.81

print("=== SPACE MISSION SIMULATOR ===")
fuel = float(input("Enter fuel mass (kg): "))
burn_rate = float(input("Enter burn rate (kg/s): "))
thrust = float(input("Enter thrust (N): "))
payload = float(input("Enter payload mass (kg): "))

mass = fuel + payload
velocity = 0
altitude = 0
time = 0
dt = 1

while fuel > 0:
    acceleration = (thrust / mass) - g
    velocity += acceleration * dt
    altitude += velocity * dt

    fuel -= burn_rate * dt
    mass -= burn_rate * dt
    time += dt

print("\n--- ASCENT COMPLETE ---")
print(f"Final altitude: {altitude:.2f} m")
print(f"Final velocity: {velocity:.2f} m/s")

escape_velocity = math.sqrt((2 * G * M) / (R + altitude))

print(f"\nEscape velocity needed: {escape_velocity:.2f} m/s")

if velocity >= escape_velocity:
    print("🚀 Mission Result: ESCAPED EARTH")
else:
    print("🛰️ Mission Result: Stayed in Earth orbit")

if velocity < escape_velocity:
    orbit_velocity = math.sqrt((G * M) / (R + altitude))
    orbit_time = (2 * math.pi * (R + altitude)) / orbit_velocity

    print(f"Orbit velocity: {orbit_velocity:.2f} m/s")
    print(f"Time for one orbit: {orbit_time/60:.2f} minutes")