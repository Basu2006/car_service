import sys

default_date = "01-01-2025"
default_amount = "1000"
default_center = "BMW"

if len(sys.argv) == 4:
    service_date = sys.argv[1]
    service_amount = sys.argv[2]
    service_center = sys.argv[3]
else:
    service_date = default_date
    service_amount = default_amount
    service_center = default_center


print("Car Service Invoice")
print(f"Service Date    : {service_date}")
print(f"Service Amount  : {service_amount}")
print(f"Service Center  : {service_center}")

if service_amount.isdigit():
    print("Invoice Generated Successfully")
else:
    print("Cannot generate invoice: Invalid amount")
