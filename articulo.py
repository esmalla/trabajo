PARA_DESCUNETO=15
DES_MAX=0.10

precio=49.9
cantidad=12
iva=0.16

if cantidad > PARA_DESCUNETO:
  descuento=DES_MAX
else: 
  descuento=0.0
 






   
subtotal=precio*cantidad
Descuento=subtotal*descuento
IVA=(subtotal-Descuento)*iva
total=subtotal-Descuento

salida=f""""
subtotal:         ${subtotal:,.2f}:
Descuento         (${descuento:.2%}):
IVA(${iva:.2f}):        ${IVA:,.2f}

Total:             {total:,.2f}
"""

print(salida)
