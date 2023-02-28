unit_price=49.99
quantity=30

print(f"subtotal: ${quantity * unit_price}")
print(f"subtotal: ${quantity * unit_price:,.2f}")

iva =0.16
print(f"{iva:,.2%}")


user1="dilan"
user2="alex"
user3="tony"


output=f"{user1}\n{user2}"

print(output)

subtotal=unit_price*quantity
IVA= subtotal*iva
total=subtotal+IVA
salida=f"""subtotal:${subtotal}
IVA:  ${IVA:,.2f}
total: ${total:,.2f}
"""

print(salida)

if unit_price>12:
    descuento=0.10

    else:
        descuento=0.0


    subtotal=unit_price*quantity
    Descuento=(subtotal)*descuento
IVA= (subtotal-Descuento)*iva
total=subtotal+IVA


