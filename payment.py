class payment:
    def pay(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Payment amount must be a number")

        return f"Payment of {amount} completed successfully."
