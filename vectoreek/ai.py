class SymbioteAI:
    def __init__(self):
        self.priority_map = {
            "Fan": 0.9,      # High energy, zero movement
            "Vehicle": 0.8,  # High movement, high risk
            "Conveyor": 0.6, # Reliable movement, low energy
            "Human": 0.3     # Unpredictable, high risk
        }

    def evaluate_hosts(self, hosts, goal_location, mission_type="Infiltration"):
        """
        Calculates the 'Host Utility Score'.
        Utility = (Movement_Towards_Goal * 0.7) + (Energy_Gain * 0.3)
        """
        print(f"AI: Evaluating {len(hosts)} potential hosts for mission: {mission_type}.")
        scored_hosts = []
        
        for h in hosts:
            # Simple heuristic simulation
            if mission_type == "Energy":
                score = self.priority_map[h.host_type] * 10
            else:
                # Infiltration uses speed and route compatibility
                score = h.speed * 2.0 + self.priority_map[h.host_type] * 5.0
            
            scored_hosts.append((score, h))
            
        scored_hosts.sort(key=lambda x: x[0], reverse=True)
        return scored_hosts

    def decide_transfer(self, current_host, available_hosts, goal):
        """Logic to decide if the module should 'hop' to a new host."""
        if not current_host:
            return available_hosts[0][1] # Take the best available
            
        best_score, best_host = available_hosts[0]
        
        # Only hop if the new host is significantly better (avoid jitter)
        if best_score > 15.0:
            return best_host
            
        return None
