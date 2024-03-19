import numpy as np
import os

from bezier_curve import BezierCurve
from input_validation import InputValidation
from plot import Plot
from execution_time import ExecutionTime


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print("""
 /$$$$$$$                      /$$                            /$$$$$$                                         
| $$__  $$                    |__/                           /$$__  $$                                        
| $$  \ $$  /$$$$$$  /$$$$$$$$ /$$  /$$$$$$   /$$$$$$       | $$  \__/ /$$   /$$  /$$$$$$  /$$    /$$ /$$$$$$ 
| $$$$$$$  /$$__  $$|____ /$$/| $$ /$$__  $$ /$$__  $$      | $$      | $$  | $$ /$$__  $$|  $$  /$$//$$__  $$
| $$__  $$| $$$$$$$$   /$$$$/ | $$| $$$$$$$$| $$  \__/      | $$      | $$  | $$| $$  \__/ \  $$/$$/| $$$$$$$$
| $$  \ $$| $$_____/  /$$__/  | $$| $$_____/| $$            | $$    $$| $$  | $$| $$        \  $$$/ | $$_____/
| $$$$$$$/|  $$$$$$$ /$$$$$$$$| $$|  $$$$$$$| $$            |  $$$$$$/|  $$$$$$/| $$         \  $/  |  $$$$$$$
|_______/  \_______/|________/|__/ \_______/|__/             \______/  \______/ |__/          \_/    \_______/
""")


# =====================================================
# Input data
# =====================================================

prompt_method_choice = """
Pilih metode yang digunakan:
-------------------------------
| 1. Divide and Conquer       |
| 2. Brute Force              |
-------------------------------

Pilihan metode: """
method_choice = int(InputValidation.input_number_validation(prompt_method_choice, "integer", 1, 2))
num_of_control_points = int(InputValidation.input_number_validation("\nMasukkan jumlah titik kontrol: ", "integer", 3))
num_of_iteration = int(InputValidation.input_number_validation("\nMasukkan jumlah iterasi: ", "integer", 1))

control_points = np.zeros((num_of_control_points, 2))
print(f"\nMasukkan koordinat {num_of_control_points} titik:")
for i in range(num_of_control_points):
    control_points[i][0] = float(InputValidation.input_number_validation(f"x{i+1}: "))
    control_points[i][1] = float(InputValidation.input_number_validation(f"y{i+1}: "))


# =====================================================
# Process data
# =====================================================

plot = Plot(num_of_iteration, subplot_=111, figsize_=(800/120, 800/120), dpi_=120)
plot.plot(control_points)

execution_time = ExecutionTime()
bezier_curve = BezierCurve(num_of_iteration, control_points)

if method_choice == 1:    
    bezier_curve.divide_and_conquer(num_of_iteration, control_points, 0, len(bezier_curve.result_points)-1, plot, execution_time)
    plot.remove_saved_lines()
else:
    bezier_curve.brute_force(plot, execution_time)

plot.plot(bezier_curve.result_points)
plot.show()

print(f"\nWaktu eksekusi: {execution_time.total_time} ms")
print("\nTerima kasih dan sampai jumpa lagi!")