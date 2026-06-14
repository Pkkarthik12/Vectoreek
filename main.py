import time
from vectoreek.engine import FacilitySimulation
from vectoreek.ai import SymbioteAI

def run_simulation():
    sim = FacilitySimulation()
    ai = SymbioteAI()
    
    print("=== PROJECT VECTOREEK: MECHANICAL SYMBIONT ONLINE ===")
    print("Mission: Reach 'Data Center' via Proxy Infrastructure Hijacking.")
    print("-" * 60)
    
    for tick in range(1, 21):
        sim.run_tick()
        
        # Every 5 ticks, evaluate hosts
        if tick % 5 == 1:
            best_candidates = ai.evaluate_hosts(sim.hosts, "Data Center")
            target_host = ai.decide_transfer(sim.module.attached_to, best_candidates, "Data Center")
            
            if target_host and target_host != sim.module.attached_to:
                sim.module.unlatch()
                sim.module.latch(target_host)
                
        status = sim.module.attached_to.name if sim.module.attached_to else "Free Floating"
        print(f"Tick {tick:02d} | Power: {sim.module.power_level:05.2f}% | Host: {status}")
        time.sleep(0.1)

    print("-" * 60)
    print("Mission Log: Infiltration complete. Module remains undetected.")

if __name__ == "__main__":
    run_simulation()
