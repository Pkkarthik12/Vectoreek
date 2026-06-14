import time
import random

class Host:
    def __init__(self, name, speed, route_id, host_type):
        self.name = name
        self.speed = speed # m/s
        self.route_id = route_id # Simple ID for where it goes
        self.host_type = host_type # "Fan", "Conveyor", "Human", "Vehicle"
        self.current_position = 0.0

    def move(self, dt=1.0):
        self.current_position += self.speed * dt
        return self.current_position

class VectoreekModule:
    def __init__(self, id):
        self.id = id
        self.attached_to = None
        self.is_latched = False
        self.power_level = 100.0 # Percentage
        self.mission_data = []

    def latch(self, host):
        if not self.is_latched:
            self.attached_to = host
            self.is_latched = True
            print(f"MODULE {self.id}: Successfully latched to {host.name} ({host.host_type}).")
            return True
        return False

    def unlatch(self):
        if self.is_latched:
            print(f"MODULE {self.id}: Detached from {self.attached_to.name}.")
            self.attached_to = None
            self.is_latched = False
            return True
        return False

    def harvest_energy(self):
        """Harvests kinetic or thermal energy from the host."""
        if self.is_latched:
            gain = 0
            if self.attached_to.host_type == "Fan":
                gain = 2.0 # High energy from rotation
            elif self.attached_to.host_type == "Conveyor":
                gain = 0.5 # Low kinetic energy
            
            self.power_level = min(100.0, self.power_level + gain)
            return gain
        return 0

class FacilitySimulation:
    def __init__(self):
        self.hosts = [
            Host("Fan-Alpha", 0, "Static-Rotary", "Fan"),
            Host("Belt-01", 1.5, "Route-A", "Conveyor"),
            Host("Service-Bot-9", 3.0, "Route-B", "Vehicle"),
            Host("Maintenance-Worker-Jan", 1.2, "Random-Walk", "Human")
        ]
        self.module = VectoreekModule(id="V1-Alpha")

    def run_tick(self):
        for h in self.hosts:
            h.move()
        self.module.harvest_energy()
        self.module.power_level -= 0.1 # Base consumption
