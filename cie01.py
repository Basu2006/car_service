import sys

if len(sys.argv) != 4:
    print("Error: Invalid Arguments")
    print("Usage: python invoice.py <service_date> <service_amount> <service_center>")
else:
    service_date = sys.argv[1]
    service_amount = sys.argv[2]
    service_center = sys.argv[3]

    
    print(f"Service Date    : {service_date}")
    print(f"Service Amount  : {service_amount}")
    print(f"Service Center  : {service_center}")
    

    if service_amount.isdigit():
        print("Invoice Generated Successfully")
    else:
        print("cant print invoice")
