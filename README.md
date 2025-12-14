# Giải thuật Tô màu đồ thị Tham lam (Greedy Graph Coloring)

Dự án này triển khai một thuật toán tô màu đồ thị tham lam (Greedy Algorithm) bằng Python, ưu tiên chọn đỉnh có bậc (degree) lớn nhất để tô màu. Thuật toán được thiết kế để tìm ra một cách tô màu hợp lệ (không có hai đỉnh kề nhau cùng màu) với số lượng màu tối đa được cung cấp ($k$).

## 1. Tính năng chính

* **Tô màu Tham lam Ưu tiên:** Sử dụng chiến lược ưu tiên tô màu các đỉnh có bậc **lớn nhất** trước.
* **Xử lý Đỉnh ưu tiên (Tie-breaker):** Nếu nhiều đỉnh có cùng bậc cao nhất, thuật toán sẽ ưu tiên chọn đỉnh có **chỉ số nhỏ hơn** để đảm bảo tính nhất quán.
* **Đầu vào:** Đọc ma trận kề (Adjacency Matrix) của đồ thị từ một file văn bản.
* **Trực quan hóa:** Sử dụng thư viện `matplotlib` để vẽ đồ thị và trực quan hóa kết quả tô màu. 

## 2. Cấu trúc Đầu vào (Input Format)

Đồ thị cần được cung cấp dưới dạng **Ma trận kề (Adjacency Matrix)** trong một file văn bản, mặc định là `graph.txt`.

**Định dạng file `graph.txt`:**

* Các số (`0` hoặc `1`) trong mỗi hàng được phân cách bằng dấu cách.
* `1` đại diện cho cạnh (có kết nối), `0` đại diện cho không có cạnh.

**Ví dụ (Đồ thị 6 đỉnh - $6 \times 6$):**

```text
# graph.txt
0 1 1 0 1 0 
1 0 1 1 0 1
1 1 0 1 1 0
0 1 1 0 0 1
1 0 1 0 0 1
0 1 0 1 1 0
