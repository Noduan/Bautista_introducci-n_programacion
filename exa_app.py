monto_soles = float(input("\nIngrese el monto en soles (PEN): "))

tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))

monto_dolar = monto_soles / tasa_cambio

print(f"\n---Conversión en Global Change ---")
print(f"Monto en soles: S/ {monto_soles:.2f}")
print(f"Tasa de cambio: 1 USD = S/ {tasa_cambio}")
print(f"Equivalente en dólares: $ {monto_dolar:.2f}")