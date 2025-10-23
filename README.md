# EcoDynamics: Predator-Prey Simulation

## Project Overview
This project proposal presents a simulation study of ecosystem dynamics, focusing on predator–prey interactions and resource competition. The goal is to model predator–prey interactions using mathematical models such as Lotka–Volterra and Logistic growth with Holling II functional response.  

## Objectives

- Implement both continuous and agent-based predator–prey models  
- Demonstrate parameterized simulation runs with data collection  
- Generate comparative results and population trend visualizations  
- Support reproducible, multi-run experiments with configuration management 

## Project Status
### **Completed Features**
- Lotka–Volterra and Logistic–Holling II Models** (continuous dynamics)
- Entity Classes**: `Prey`, `Predator`, and `GridEnvironment`
- ABM Core**: movement, reproduction, hunting, energy balance, extinction detection
- Simulation Framework**: supports both ODE and discrete step models
- Data Collection**: automated CSV/JSON export for each run
- Parameterization**: configurable via `config_loader.py` and CLI overrides
- Batch Execution**: `run_all.py` executes 10+ parameterized runs
- Visualization**: Matplotlib plots for population time series and multi-run comparison
- Random Seed Control** for reproducibility
- Data Collection/ DataCollector module
- Parameterization & Batch Runs
- Implemented run_all.py batch runner

## To do:
- Statistical comparison of ABM vs. Lotka–Volterra equilibrium outcomes 
- Testing & Validation 

## Project Structure
- **EcoDynamics/abm.py – ABM environment and simulation controller  
- **EcoDynamics/data_collector.py – Tracks and exports simulation data  
- **EcoDynamics/entities.py – Defines Prey and Predator agent behaviors  
- **EcoDynamics/grid_environment.py – 2D grid for agent movement and interactions  
- **EcoDynamics/models/lotka_volterra.py – Lotka–Volterra predator–prey model  
- **EcoDynamics/models/logistic_hollingII.py – Logistic growth with Holling II predation  
- **EcoDynamics/simulation.py – SciPy-based ODE solver and population data collection  
- **EcoDynamics/config_loader.py – Loads and manages simulation parameters  
- **EcoDynamics/main.py – Runs models and plots results  
- **EcoDynamics/run_all.py – Batch execution script for multiple simulations  
- **EcoDynamics/plot_results.py – Visualizes population trends using Matplotlib  
- **EcoDynamics/data/ – Stores time-series, summary, and configuration outputs  
- **EcoDynamics/configs/ – Contains JSON configuration files for different runs  
- **EcoDynamics/requirements.txt – Lists Python dependencies  
- **EcoDynamics/README.md – Project documentation  
  
## Installation Instructions

### Requirements
- Python **3.10+**
- NumPy
- SciPy
- Matplotlib

### Enviromment Setup
```bash
git clone https://github.com/Bodenzee/EcoDynamics
cd EcoDynamics
pip install -r requirements.txt
```
### Running the Simulation
Run the following for single simulation
```bash
src/main.py
```
Run the following for batch simulation
```bash
python run_all.py
```
