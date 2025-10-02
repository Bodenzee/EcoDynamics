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
- To do: ABM Model, parameter configuration, expand visualization with resource tracking and phase plots
  
## Project Structure
- EcoDynamics/data_collector.py: Tracks results from simulation
- EcoDynamics/entities.py: Defines Prey,Predator, and environment
- EcoDynamics/main.py: Runs models and plots graphs
- EcoDynamics/models.py: Contains ODE Models
- EcoDynamics/simulation.py:Collects population data, SciPy ODE solver

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
