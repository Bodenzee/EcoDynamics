# EcoDynamics: Predator-Prey Simulation

## Project Overview
This project proposal presents a simulation study of ecosystem dynamics, focusing on predator–prey interactions and resource competition. The goal is to model predator–prey interactions using mathematical models such as Lotka–Volterra and Logistic growth with Holling II functional response.  

## Project Status
- Lotka-Volterra model implemented
- Entity classes (`Prey`, `Predator`, `Environment`) created 
- Logistic growth with Holling II predation implemented   
- Data Collector
- Visualization utilizing Matplotlib functioning
- Simulation engine utilizing SciPy ODE implemented
ABM Development
- Implement GridEnvironment class
- Implement Prey movement & reproduction
- Implement Predator hunting & starvation
- Energy/food balance mechanics
- Add random seed control
- Implement step/update loop
- Detect and log extinction events
  
## To do:
- Data Collection 
- Create DataCollector module
-  Write CSV/JSON exports
-   Record metadata for reproducibility

Parameterization & Batch Runs 
- Build config_loader.py with CLI overrides
- Implement run_all.py batch runner
- Save results into master index JSON

Testing & Validation 
- Compare ABM averages vs. Lotka–Volterra equilibrium
- Perform 10+ runs with varying parameters
- Generate comparative population plots
  
## Project Structure
- EcoDynamics/data_collector.py: Tracks results from simulation
- EcoDynamics/entities.py: Prey and Predator agent definitions
- EcoDynamics/main.py: Runs models and plots graphs
- EcoDynamics/models.py: Contains ODE Models
- EcoDynamics/simulation.py: Collects population data, SciPy ODE solver
- EcoDynamics/ABM.py: ABM environment and simulation controller
  
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
```bash
Run the following: src/main.py
```
