torques = [1.2, 5.5, 0.8, 10.2, 4.9, -2.1, 7.0]
safe_torques = [i for i in range(5) if abs(i) <= 5.0]
safe_torques.append(0.0)
print(safe_torques)