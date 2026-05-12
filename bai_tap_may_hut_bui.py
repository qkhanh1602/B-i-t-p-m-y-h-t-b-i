import random

def is_clean(env):
    for row in env:
        if 0 in row: return False
    return True

def Rule(status, i, j):
    if status == 0:
        return "SUCK"
    if i == 0:  
        if j < 2: return "RIGHT"
        if j == 2: return "DOWN"
        
    elif i == 1:  
        if j > 0: return "LEFT"
        if j == 0: return "DOWN"
        
    elif i == 2:  
        if j < 2: return "RIGHT"
        if j == 2: return "STOP"

def action_exec(env, action, i, j):
    new_env = [row[:] for row in env]
    
    if action == "SUCK":
        new_env[i][j] = 1 
    elif action == "UP":    i -= 1
    elif action == "DOWN":  i += 1
    elif action == "LEFT":  j -= 1
    elif action == "RIGHT": j += 1
    
    return new_env, i, j

def solver(start_env):
    env = [row[:] for row in start_env]
    i, j = 0, 0 # Đặt máy ở góc trên cùng bên trái
    step = 1

    print("=== TRẠNG THÁI PHÒNG BAN ĐẦU (0: Bẩn, 1: Sạch) ===")
    for row in env:
        print(row)
    print("=" * 45 + "\n")

    while True:
        if is_clean(env):
            print(f"ĐÃ DỌN SẠCH HOÀN TOÀN PHÒNG SAU {step - 1} BƯỚC!")
            for row in env: print(row)
            break

        action = Rule(env[i][j], i, j)
        print(f"Bước {step}: Vị trí ({i}, {j}) | Trạng thái: {'Bẩn' if env[i][j] == 0 else 'Sạch'} -> Hành động: {action}")
        
        if action == "STOP":
            print("Máy đã đi hết quỹ đạo cài đặt sẵn và dừng lại.")
            break

        env, i, j = action_exec(env, action, i, j)
        step += 1

if __name__ == "__main__":

    room = [[random.choice([0, 1]) for _ in range(3)] for _ in range(3)]
    solver(room)