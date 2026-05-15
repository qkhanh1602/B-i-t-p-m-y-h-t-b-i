# B-i-t-p-m-y-h-t-b-i
Môn trí tuệ nhân tạo
# Vacuum Cleaner Agent - Simple Reflex Agent

## Giới thiệu

Dự án này mô phỏng một **máy hút bụi thông minh đơn giản** sử dụng mô hình **Simple Reflex Agent** trong môn Trí tuệ nhân tạo.

Agent sẽ di chuyển trong một căn phòng dạng ma trận `3x3`.  
Mỗi ô trong ma trận biểu diễn trạng thái của một vị trí trong phòng.

Quy ước:

- `0`: Ô bẩn
- `1`: Ô sạch

Máy hút bụi bắt đầu tại vị trí `(0, 0)` và di chuyển theo một quỹ đạo cố định để dọn sạch phòng.

---

## Mục tiêu của chương trình

Chương trình dùng để minh họa cách một agent hoạt động trong môi trường đơn giản.

Agent có nhiệm vụ:

1. Quan sát trạng thái ô hiện tại.
2. Nếu ô hiện tại bẩn thì hút bụi.
3. Nếu ô hiện tại sạch thì di chuyển sang ô tiếp theo.
4. Lặp lại quá trình cho đến khi phòng sạch hoàn toàn hoặc agent đi hết quỹ đạo.

---

## Ý tưởng chính

Agent hoạt động dựa trên tập luật dạng:

```text
IF điều kiện THEN hành động
```

Cụ thể:

```text
IF ô hiện tại bẩn
    THEN hút bụi

ELSE IF ô hiện tại sạch
    THEN di chuyển theo quỹ đạo đã định
```

Đây là đặc trưng của **Simple Reflex Agent**, vì agent chỉ dựa vào trạng thái hiện tại để đưa ra hành động.

---

## Ma trận môi trường

Phòng được biểu diễn bằng ma trận `3x3`.

Ví dụ:

```python
[
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]
```

Trong đó:

```text
0 = Bẩn
1 = Sạch
```

---

## Quỹ đạo di chuyển của Agent

Agent di chuyển theo đường ziczac như sau:

```text
(0,0) → (0,1) → (0,2)
                      ↓
(1,0) ← (1,1) ← (1,2)
↓
(2,0) → (2,1) → (2,2)
```

Agent bắt đầu tại ô `(0,0)`.

Khi agent đi tới ô cuối cùng `(2,2)`, nếu phòng đã sạch thì chương trình kết thúc.

---

## Tập luật của Agent

### Luật 1: Hút bụi

Nếu ô hiện tại bẩn thì agent thực hiện hành động hút bụi.

```python
if status == 0:
    return "SUCK"
```

Ý nghĩa:

```text
IF ô hiện tại bẩn
THEN hút bụi
```

Sau khi hút bụi, ô hiện tại được chuyển thành sạch:

```python
new_env[i][j] = 1
```

---

### Luật 2: Di chuyển ở hàng đầu tiên

Nếu agent đang ở hàng đầu tiên, tức là `i == 0`:

```python
if i == 0:
    if j < 2:
        return "RIGHT"
    if j == 2:
        return "DOWN"
```

Ý nghĩa:

```text
IF đang ở hàng 0 và chưa tới cuối hàng
THEN đi sang phải

IF đang ở hàng 0 và đã tới cuối hàng
THEN đi xuống
```

Ví dụ:

```text
(0,0) → (0,1) → (0,2)
```

Khi tới `(0,2)`, agent đi xuống `(1,2)`.

---

### Luật 3: Di chuyển ở hàng thứ hai

Nếu agent đang ở hàng thứ hai, tức là `i == 1`:

```python
elif i == 1:
    if j > 0:
        return "LEFT"
    if j == 0:
        return "DOWN"
```

Ý nghĩa:

```text
IF đang ở hàng 1 và chưa tới đầu hàng
THEN đi sang trái

IF đang ở hàng 1 và đã tới đầu hàng
THEN đi xuống
```

Ví dụ:

```text
(1,2) → (1,1) → (1,0)
```

Khi tới `(1,0)`, agent đi xuống `(2,0)`.

---

### Luật 4: Di chuyển ở hàng cuối

Nếu agent đang ở hàng cuối, tức là `i == 2`:

```python
elif i == 2:
    if j < 2:
        return "RIGHT"
    if j == 2:
        return "STOP"
```

Ý nghĩa:

```text
IF đang ở hàng 2 và chưa tới cuối hàng
THEN đi sang phải

IF đang ở hàng 2 và đã tới cuối hàng
THEN dừng lại
```

Ví dụ:

```text
(2,0) → (2,1) → (2,2)
```

Khi tới `(2,2)`, agent dừng lại.

---

## Tập luật tổng quát

Có thể viết tập luật của agent như sau:

```text
IF ô hiện tại bẩn
    THEN hút bụi

ELSE IF đang ở hàng 0 và chưa tới cuối hàng
    THEN đi sang phải

ELSE IF đang ở hàng 0 và đã tới cuối hàng
    THEN đi xuống

ELSE IF đang ở hàng 1 và chưa tới đầu hàng
    THEN đi sang trái

ELSE IF đang ở hàng 1 và đã tới đầu hàng
    THEN đi xuống

ELSE IF đang ở hàng 2 và chưa tới cuối hàng
    THEN đi sang phải

ELSE IF đang ở hàng 2 và đã tới cuối hàng
    THEN dừng lại
```

---

## Cấu trúc chương trình

Chương trình gồm các hàm chính:

| Hàm | Chức năng |
|---|---|
| `is_clean(env)` | Kiểm tra phòng đã sạch hoàn toàn chưa |
| `Rule(status, i, j)` | Chứa tập luật để chọn hành động |
| `action_exec(env, action, i, j)` | Thực hiện hành động của agent |
| `solver(start_env)` | Điều khiển toàn bộ quá trình hoạt động của agent |

---

## Giải thích các hàm

### 1. Hàm `is_clean(env)`

```python
def is_clean(env):
    for row in env:
        if 0 in row: return False
    return True
```

Hàm này kiểm tra xem trong phòng còn ô bẩn không.

Nếu còn số `0` trong bất kỳ hàng nào, nghĩa là phòng vẫn còn bẩn.

Nếu không còn số `0`, nghĩa là phòng đã sạch hoàn toàn.

---

### 2. Hàm `Rule(status, i, j)`

```python
def Rule(status, i, j):
```

Đây là hàm chứa tập luật điều khiển agent.

Hàm nhận vào:

- `status`: trạng thái ô hiện tại
- `i`: vị trí hàng hiện tại
- `j`: vị trí cột hiện tại

Hàm trả về một trong các hành động:

```text
SUCK
RIGHT
LEFT
DOWN
STOP
```

Trong đó:

| Hành động | Ý nghĩa |
|---|---|
| `SUCK` | Hút bụi |
| `RIGHT` | Đi sang phải |
| `LEFT` | Đi sang trái |
| `DOWN` | Đi xuống |
| `STOP` | Dừng lại |

---

### 3. Hàm `action_exec(env, action, i, j)`

```python
def action_exec(env, action, i, j):
```

Hàm này dùng để thực hiện hành động mà agent đã chọn.

Đầu tiên chương trình tạo bản sao của môi trường:

```python
new_env = [row[:] for row in env]
```

Việc tạo bản sao giúp tránh thay đổi trực tiếp ma trận ban đầu.

Nếu hành động là hút bụi:

```python
if action == "SUCK":
    new_env[i][j] = 1
```

Ô hiện tại được chuyển từ bẩn thành sạch.

Nếu hành động là di chuyển:

```python
elif action == "UP":    
    i -= 1

elif action == "DOWN":  
    i += 1

elif action == "LEFT":  
    j -= 1

elif action == "RIGHT": 
    j += 1
```

Sau đó hàm trả về:

```python
return new_env, i, j
```

Nghĩa là trả về:

- Môi trường mới
- Vị trí hàng mới
- Vị trí cột mới

---

### 4. Hàm `solver(start_env)`

```python
def solver(start_env):
```

Đây là hàm chính điều khiển toàn bộ hoạt động của agent.

Hàm này thực hiện các bước:

1. Sao chép môi trường ban đầu.
2. Đặt vị trí bắt đầu của agent là `(0,0)`.
3. In trạng thái phòng ban đầu.
4. Lặp lại quá trình quan sát, chọn hành động và thực hiện hành động.
5. Dừng khi phòng sạch hoàn toàn hoặc agent đi hết quỹ đạo.

---

## Code chính

```python
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
    elif action == "UP":    
        i -= 1
    elif action == "DOWN":  
        i += 1
    elif action == "LEFT":  
        j -= 1
    elif action == "RIGHT": 
        j += 1
    
    return new_env, i, j

def solver(start_env):
    env = [row[:] for row in start_env]
    i, j = 0, 0
    step = 1

    print("=== TRẠNG THÁI PHÒNG BAN ĐẦU (0: Bẩn, 1: Sạch) ===")
    for row in env:
        print(row)
    print("=" * 45 + "\n")

    while True:
        if is_clean(env):
            print(f"ĐÃ DỌN SẠCH HOÀN TOÀN PHÒNG SAU {step - 1} BƯỚC!")
            for row in env:
                print(row)
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
```

---

## Cách chạy chương trình

### Bước 1: Tạo file Python

Tạo file tên:

```text
main.py
```

Sau đó dán code vào file `main.py`.

---

### Bước 2: Chạy chương trình

Mở terminal hoặc command prompt và chạy lệnh:

```bash
python main.py
```

Hoặc nếu máy dùng Python 3:

```bash
python3 main.py
```

---

## Ví dụ kết quả chạy

Ví dụ chương trình tạo ra phòng ban đầu như sau:

```text
=== TRẠNG THÁI PHÒNG BAN ĐẦU (0: Bẩn, 1: Sạch) ===
[0, 1, 0]
[1, 0, 1]
[0, 1, 1]
=============================================
```

Sau đó agent bắt đầu hoạt động:

```text
Bước 1: Vị trí (0, 0) | Trạng thái: Bẩn -> Hành động: SUCK
Bước 2: Vị trí (0, 0) | Trạng thái: Sạch -> Hành động: RIGHT
Bước 3: Vị trí (0, 1) | Trạng thái: Sạch -> Hành động: RIGHT
Bước 4: Vị trí (0, 2) | Trạng thái: Bẩn -> Hành động: SUCK
Bước 5: Vị trí (0, 2) | Trạng thái: Sạch -> Hành động: DOWN
...
ĐÃ DỌN SẠCH HOÀN TOÀN PHÒNG SAU ... BƯỚC!
```

---

## Kết quả mong đợi

Sau khi chạy, agent sẽ dọn sạch toàn bộ phòng.

Kết quả cuối cùng của phòng sẽ là:

```python
[
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
```

Điều này có nghĩa là tất cả các ô đều đã sạch.

---

## Kiến thức AI được minh họa

Dự án này minh họa các khái niệm cơ bản trong Trí tuệ nhân tạo:

### Agent

Agent là đối tượng có khả năng quan sát môi trường và thực hiện hành động.

Trong chương trình này, agent là máy hút bụi.

---

### Environment

Environment là môi trường mà agent hoạt động.

Trong chương trình này, environment là căn phòng dạng ma trận `3x3`.

---

### Percept

Percept là thông tin agent nhận được từ môi trường.

Trong chương trình này, percept là trạng thái của ô hiện tại:

```text
Bẩn hoặc sạch
```

---

### Action

Action là hành động mà agent thực hiện.

Trong chương trình này, các action gồm:

```text
SUCK, RIGHT, LEFT, DOWN, STOP
```

---

### Simple Reflex Agent

Simple Reflex Agent là agent đưa ra hành động dựa trên trạng thái hiện tại.

Trong chương trình này:

```text
Nếu ô hiện tại bẩn thì hút.
Nếu ô hiện tại sạch thì di chuyển.
```

Agent không cần học, không cần dự đoán, chỉ phản ứng theo tập luật đã được lập trình sẵn.

---

## Ưu điểm

- Code đơn giản, dễ hiểu.
- Minh họa rõ mô hình Simple Reflex Agent.
- Dễ chạy và không cần cài đặt thêm thư viện ngoài.
- Phù hợp cho bài học nhập môn Trí tuệ nhân tạo.

---

## Hạn chế

- Agent chỉ hoạt động tốt với ma trận `3x3`.
- Quỹ đạo di chuyển được lập trình cố định.
- Agent không có bộ nhớ về những ô đã đi qua.
- Agent không tự học hoặc tối ưu đường đi.
- Nếu thay đổi kích thước ma trận, cần chỉnh lại tập luật.

---

## Hướng phát triển

Có thể mở rộng chương trình theo các hướng sau:

1. Cho phép nhập kích thước ma trận bất kỳ.
2. Thêm bộ nhớ để trở thành Model-Based Reflex Agent.
3. Thêm thuật toán tìm đường thông minh.
4. Thêm giao diện hiển thị trực quan.
5. Cho agent tự chọn đường đi tối ưu hơn.

---

## Kết luận

Chương trình mô phỏng một máy hút bụi đơn giản hoạt động theo mô hình **Simple Reflex Agent**.

Agent sử dụng tập luật cố định để quyết định hành động:

```text
Nếu ô bẩn thì hút.
Nếu ô sạch thì di chuyển.
Nếu đi hết phòng thì dừng.
```

Dự án phù hợp để học và minh họa các khái niệm cơ bản trong môn Trí tuệ nhân tạo như:

- Agent
- Environment
- Percept
- Action
- Rule-Based Agent
- Simple Reflex Agent
