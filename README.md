Aquí tienes la versión en inglés de tu README:  

---

# **Optimal Thermostat with Dynamic Programming**  

## **Description**  
This project implements an **optimal thermostat control** using **Bellman Equations** to determine the optimal heating system on/off policy. The goal is to minimize **operational costs** while maintaining the temperature within a desired range.  

---  
## **📋 Features**  
- Problem modeling using **dynamic programming**.  
- Implementation of the Bellman equation to determine the optimal policy.  
- Simulation of thermostat behavior under different initial conditions.  
- Evaluation of the impact of different costs and configurations.  

---  
## **💻 Installation & Usage**  

### **Requirements**  
This project is developed in **Python 3** and requires the following libraries:  
```bash
pip install numpy matplotlib
```  

---  
### **🚀 Execution**  
To run the program, simply execute the main script:  
```bash
python thermostat.py
```  
This will generate graphs and statistics on the thermostat’s operation under the optimal policy.  

---  
## **Technical Explanation**  
The problem is modeled as a **Markov Decision Process (MDP)** with the following elements:  
- **States**: The current system temperature.  
- **Actions**: Turning the heating system on or off.  
- **Rewards**: Costs associated with energy consumption and penalties for deviations from the target temperature.  
- **Bellman Equation**: Used to compute optimal values and derive the optimal control policy.  

---  
## **Expected Results**  
By executing the model, an optimal strategy is obtained that balances energy costs and thermal stability. Graphs are provided showing temperature over time and decisions made at each moment.  

---  
## **Team Members**  
- **Martín Portugal**  
- **Jorge Viñas**  

---

Let me know if you'd like any refinements! 🚀
