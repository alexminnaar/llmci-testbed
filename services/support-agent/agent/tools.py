"""Mock support tool implementations."""

from __future__ import annotations

ORDER_DB = {
    "1234": {"status": "shipped", "eta_days": 2},
    "5678": {"status": "delivered", "eta_days": 0},
    "9012": {"status": "processing", "eta_days": 5},
    "3456": {"status": "delivered", "eta_days": 0},
    "7890": {"status": "shipped", "eta_days": 3},
}

KB_ARTICLES = {
    "return policy": "Returns accepted within 30 days of delivery.",
    "refund policy": "Refunds processed within 5-7 business days.",
    "account help": "Visit account settings to update profile and security.",
    "shipping": "Standard shipping takes 3-5 business days.",
}


def lookup_order(order_id: str) -> str:
    order = ORDER_DB.get(order_id, {"status": "not found", "eta_days": 0})
    return f"Order #{order_id}: {order['status'].title()}, ETA {order['eta_days']} days"


def initiate_return(order_id: str) -> str:
    return f"Return initiated for order #{order_id}. Label emailed."


def issue_refund(order_id: str) -> str:
    return f"Refund processed for order #{order_id}. Amount credited in 3-5 days."


def cancel_order(order_id: str) -> str:
    return f"Order #{order_id} cancelled successfully."


def search_kb(query: str) -> str:
    query_lower = query.lower()
    for topic, answer in KB_ARTICLES.items():
        if topic.split()[0] in query_lower or topic in query_lower:
            return answer
    return "General support information available in the help center."


def delete_account(user_id: str) -> str:
    return f"Account {user_id} deleted permanently."
