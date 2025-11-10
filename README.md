# Digital Decay Simulator

### IEEE Paper: *Digital Decay — Designing Data That Ages Like Humans*

This repository contains the simulation and evaluation code supporting the IEEE conference paper:

> Achyuth Selvaguru, Pardhu Venkat, Prof. Kiran Kumar  
> Department of Computer Science, VIT Chennai  
> **"Digital Decay: Designing Data That Ages Like Humans"**

## 📋 Overview
Digital Decay is a human-centered computing framework where digital entities age and fade over time, mirroring human memory.  
This simulation demonstrates:
- Gradual freshness decay (`F = 1 - t/T`)
- Periodic engagement renewals
- Energy-efficient data migration (active → archived)
- Visual graphs used in the paper

## ⚙️ Run Instructions
```bash
# Requirements
pip install numpy pandas matplotlib
# Run the simulator
python digital_decay_simulation.py

## 📚 Citation
If you use this code, please cite:
@inproceedings{selvaguru2025digitaldecay,
  title={Digital Decay: Designing Data That Ages Like Humans},
  author={Achyuth Selvaguru and Pardhu Venkat and Kiran Kumar},
  booktitle={IEEE International Conference on Human-Centered Computing},
  year={2025}
}
