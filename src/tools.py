import json
from typing import Dict, Any

TOOLS_SCHEMA = [
    {
        "name": "get_leave_balance",
        "description": "Tra cứu số ngày phép còn lại và thông tin nhân viên VinFast theo mã NV.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên (ví dụ: 'EMP001')"
                }
            },
            "required": ["employee_id"]
        }
    },
    {
        "name": "submit_leave_request",
        "description": "Tạo đơn xin nghỉ phép cho nhân viên VinFast lên hệ thống HRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên (ví dụ: 'EMP001')"
                },
                "start_date": {
                    "type": "string",
                    "description": "Ngày bắt đầu nghỉ (YYYY-MM-DD)"
                },
                "end_date": {
                    "type": "string",
                    "description": "Ngày kết thúc nghỉ (YYYY-MM-DD)"
                },
                "reason": {
                    "type": "string",
                    "description": "Lý do xin nghỉ phép"
                }
            },
            "required": ["employee_id", "start_date", "end_date", "reason"]
        }
    }
]

MOCK_EMPLOYEES = {
    "EMP001": {"full_name": "Nguyễn Hồng Cường", "leave_balance": 12, "department": "AI Engineering"},
    "EMP002": {"full_name": "Trần Văn A", "leave_balance": 2, "department": "Manufacturing"}
}

def execute_get_leave_balance(employee_id: str) -> str:
    emp = MOCK_EMPLOYEES.get(employee_id.strip().upper())
    if emp:
        return json.dumps({
            "status": "SUCCESS",
            "employee_id": employee_id,
            "data": emp
        }, ensure_ascii=False)
    return json.dumps({"status": "NOT_FOUND", "message": f"Không tìm thấy nhân viên mã '{employee_id}'"}, ensure_ascii=False)

def execute_submit_leave_request(employee_id: str, start_date: str, end_date: str, reason: str) -> str:
    emp = MOCK_EMPLOYEES.get(employee_id.strip().upper())
    if not emp:
        return json.dumps({"status": "NOT_FOUND", "message": f"Mã nhân viên '{employee_id}' không tồn tại!"}, ensure_ascii=False)
    
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"LR-{employee_id}-2026",
        "message": f"Đã tạo đơn nghỉ phép thành công cho nhân viên {emp['full_name']} ({employee_id}) từ {start_date} đến {end_date}. Lý do: {reason}."
    }, ensure_ascii=False)

TOOL_ROUTER = {
    "get_leave_balance": execute_get_leave_balance,
    "submit_leave_request": execute_submit_leave_request
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)