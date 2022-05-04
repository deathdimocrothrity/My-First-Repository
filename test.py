from decimal import Decimal, ROUND_HALF_UP
print(Decimal(0.0004).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP))
