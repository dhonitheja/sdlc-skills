def create_invoice(customer, amount_cents):
    return {"customer": customer, "amount_cents": amount_cents, "status": "draft"}
