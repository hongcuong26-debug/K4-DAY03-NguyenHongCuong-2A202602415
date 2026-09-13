# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [NGUYEN HONG CUONG]  
> **Mã Sinh Viên / Mã Học viên:** [2A202602415]  
> **Chủ đề Lựa chọn:** [Trợ lý Nhân sự VinFast (HR Assistant))  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4/ 5 | Agent phải phân tích yêu cầu của người dùng, tự xác định các tham số còn thiếu (mã NV, thời gian nghỉ, lý do), kiểm tra quỹ ngày phép trước rồi mới thực hiện tạo đơn.|
| **2. Tool Interaction** | 5 / 5 |Bắt buộc kết nối với MCP Server / Hệ thống HRM bên ngoài qua 2 Tool: get_leave_balance (đọc dữ liệu) và submit_leave_request (ghi dữ liệu). |
| **3. Dynamic Decision** | 4 / 5 | Kết quả bước 2 quyết định bước 3: Nếu get_leave_balance báo số ngày phép còn lại < số ngày xin nghỉ, Agent lập tức thay đổi luồng xử lý để từ chối/cảnh báo thay vì gọi tool submit_leave_request.|
| **4. Long Horizon Goal** | 4 / 5 | Agent phải duy trì mục tiêu "Hoàn tất tạo đơn xin nghỉ phép" qua nhiều lượt hội thoại (Multi-turn) để hỏi bổ sung thông tin khi người dùng cung cấp thiếu.|
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tra cứu số ngày phép cho nhân viên mã EMP001",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "get_leave_balance",
    "arguments": {
      "employee_id": "EMP001"
    },
    "observation": {
      "status": "SUCCESS",
      "employee_id": "EMP001",
      "data": {
        "full_name": "Nguyễn Hồng Cường",
        "leave_balance": 12,
        "department": "AI Engineering"
      }
    },
    "latency_ms": 0.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 2 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
