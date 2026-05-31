# Robotics Manipulators

A comprehensive repository for the **Robotics Manipulators** Master's module. This repository contains weekly coursework, continuous assessments, and practical implementations covering the fundamental principles of robotics, including kinematics, dynamics, trajectory planning, and control systems.

All assessments are implemented using Python and Jupyter Notebooks, emphasizing computational approaches to robotic manipulator design and control.

## 📚 Curriculum Structure

The repository is structured week-by-week, gradually building up the complexity from basic linear algebra to advanced force-motion control of a robotic arm in contact-rich tasks.

### 🔹 Week 1: Foundations of Linear Algebra
- **Overview**: Establishing the mathematical groundwork for robotics.
- **Intended Learning Outcomes**: Put to practice basic scalar, vector, and matrix algebra in Python using `numpy`, which are used extensively throughout the unit.

### 🔹 Week 2: Spatial Descriptions and Transformations
- **Overview**: Representing positions and orientations in 2D and 3D space.
- **Intended Learning Outcomes**: Practical application of Special Orthogonal and Special Euclidean groups: $SO(2)$, $SE(2)$, $SO(3)$, and $SE(3)$ elements and their composition.

### 🔹 Week 3: Forward Kinematics
- **Overview**: Computing the pose of the end-effector given joint angles.
- **Intended Learning Outcomes**: Implementation of forward kinematics computations using `numpy`, translating joint space to task space coordinates.

### 🔹 Week 4 & 5: Differential Kinematics & Jacobians
- **Overview**: Relating joint velocities to end-effector velocities.
- **Intended Learning Outcomes**: Computation and analysis of differential kinematics (Jacobians) using `numpy`. Understanding singular configurations and velocity transformations.

### 🔹 Week 6: Introduction to Dynamics
- **Overview**: Understanding the forces and torques that cause motion.
- **Intended Learning Outcomes**: Be able to analyze system behavior using rigid-body dynamics models.

### 🔹 Week 7: Multi-DoF Manipulator Dynamics
- **Overview**: Extending dynamics concepts to complex multi-link arms.
- **Intended Learning Outcomes**: Be able to implement a dynamic model and analyze the motion of multi-degree-of-freedom (DoF) robotic manipulators.

### 🔹 Week 8: Joint Space Control
- **Overview**: Designing feedback controllers to track desired trajectories in joint space.
- **Intended Learning Outcomes**: Be able to implement a Proportional-Derivative (PD) based controller and an Inverse Dynamics controller for manipulators.

### 🔹 Week 9: Task Space Control (Inverse Dynamics)
- **Overview**: Controlling the manipulator directly in the operational (task) space.
- **Intended Learning Outcomes**: Be able to implement an inverse dynamics controller in task space to track Cartesian trajectories.

### 🔹 Week 10: Hybrid Force/Motion Control
- **Overview**: Handling tasks that require both precise positioning and controlled force application.
- **Intended Learning Outcomes**: Be able to apply a hybrid force/motion controller in a contact-rich task. (Includes simulated tasks with Kinova manipulators).

## 🛠️ Tech Stack & Requirements

The tasks within these notebooks rely heavily on the Python scientific stack:
- **Python 3.x**
- **Jupyter Notebook** (`.ipynb`)
- **NumPy** for matrix and vector operations
- **Matplotlib** for plotting trajectory data and dynamics behavior
- Standard Python Math library

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prathapselvakumar/Robotic-Manipulators.git
   cd Robotic-Manipulators
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install jupyter numpy matplotlib
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

5. Navigate to the desired week's folder and open the corresponding `lessonX_continuous_assessment.ipynb` notebook to get started!
