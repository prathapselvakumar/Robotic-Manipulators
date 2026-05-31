import codecs
import json

nb_path = r"d:\Presentations\Masters Data\Semester-2\Robotics Manipulators\Week-6\lesson07_continuous_assessment\lesson07_continuous_assessment.ipynb"
with codecs.open(nb_path, 'r', encoding='utf-8') as f:
    content = f.read()
    
new_code = """# Convert initial angle to radians
q0_rad = np.deg2rad(q0)
# Kinetic energy at initial position (zero velocity)
T = 0.0
# Potential energy: V = Mgl(1 - cos(theta)), with zero at lowest pos (theta=0)
V = M * g * l * (1 - np.cos(q0_rad))
# Lagrangian L = T - V
L = T - V
"""

nb = json.loads(content)
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = cell.get('source', [])
        new_source = []
        for line in source:
            if 'L = None' in line:
                for new_line in new_code.split('\n'):
                    if new_line:
                        new_source.append(new_line + '\n')
            else:
                new_source.append(line)
        cell['source'] = new_source

with codecs.open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
