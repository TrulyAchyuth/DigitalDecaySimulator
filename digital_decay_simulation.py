"""
Digital Decay Simulator
Author: Achyuth Selvaguru (VIT Chennai)
Based on the IEEE paper 'Digital Decay: Designing Data That Ages Like Humans'
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# --- PARAMETERS ---
days = 270  # simulation time (~9 months)
start_date = datetime(2025, 1, 1)

# Lifespan for each file type (in days)
lifespans = {"Photo": 240, "Note": 150, "Message": 90}

# Engagement schedule (days when file is used again)
engagements = {
    "Photo": [45, 120, 200],
    "Note": [15, 60, 140, 210],
    "Message": [5, 12, 20, 35, 60, 120]
}

def simulate_decay(T_days, engagement_days, total_days=270):
    freshness = np.zeros(total_days + 1)
    freshness[0] = 1.0
    last_interaction = 0
    for d in range(1, total_days + 1):
        if d in engagement_days:
            last_interaction = d
        t = d - last_interaction
        F = 1.0 - (t / T_days)
        freshness[d] = max(0.0, min(1.0, F))
    return freshness

results = {t: simulate_decay(lifespans[t], engagements[t], days) for t in lifespans}
date_index = [start_date + timedelta(days=i) for i in range(days + 1)]
df = pd.DataFrame({k: (results[k] * 100) for k in results}, index=date_index)
df.index.name = "Date"

# Plot freshness curves
plt.figure(figsize=(8,5))
for k in results:
    plt.plot(df.index, df[k], label=k)
plt.xlabel("Date")
plt.ylabel("Freshness (%)")
plt.title("Digital Decay Freshness Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("fig_freshness_over_time.png", dpi=200)
plt.close()

# Storage simulation (energy proxy)
sizes = {"Photo": 3.0, "Note": 0.2, "Message": 0.05}
counts = {"Photo": 100, "Note": 100, "Message": 100}
active_threshold = 0.3
active_gb, archived_gb = [], []

for d in range(days + 1):
    active, archived = 0.0, 0.0
    for typ in lifespans:
        F = results[typ][d]
        active_frac = 1.0 if F >= active_threshold else 0.0
        total_mb = sizes[typ] * counts[typ]
        active += (total_mb * active_frac) / 1024.0
        archived += (total_mb * (1 - active_frac)) / 1024.0
    active_gb.append(active)
    archived_gb.append(archived)

plt.figure(figsize=(8,5))
plt.plot(df.index, active_gb, label="Active Storage (GB)")
plt.plot(df.index, archived_gb, label="Archived Storage (GB)")
plt.xlabel("Date")
plt.ylabel("Storage (GB)")
plt.title("Active vs Archived Storage Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("fig_storage_profile.png", dpi=200)
plt.close()

print("Simulation completed. Figures saved.")
df.to_csv("monthly_snapshot.csv")
