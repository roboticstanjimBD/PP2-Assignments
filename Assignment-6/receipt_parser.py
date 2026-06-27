import re
txt= """DUPLICATE
Branch of EUROPHARMA LLP Astana
BIN 080841000762
VAT Series 58002
 No. 0014371
Cash desk 300-190
Shift 10
Serial number of check No. 61
Receipt No. 2331180266
Cashier Pharmacy 17-1
SALE
1.
Sodium chloride 0.9%, 200 ml, fl
2,000 x 154.00
308.00
Cost
308.00
2.
Boric alcohol 3%, 20 ml, fl.
1,000 x 51.00
51.00
Cost
51.00
3.
Syringe 2 ml, 3 sets. (Bioject)
2,000 x 16.00
32.00
Cost
32.00
4.
Vogt Medical infusion system
2,000 x 60.00
120.00
Cost
120.00
5.
Syringe 5 ml, 3 sets. 
1,000 x 310.00
310.00
Cost
310.00
6.
AURA Cotton pads No. 150
1,000 x 461.00
461.00
Cost
461.00
7.
Clean line soft scrub 50 ml
1,000 x 381.00
381.00
Cost
381.00
8.
Clean line cleansing scrub apricot 50 ml
1,000 x 386.00
386.00
Cost
386.00
9.
Clean line soft scrub 50 ml
1,000 x 381.00
381.00
Cost
381.00
10.
Nivea shampoo 3in1 for men 400 ml
1,000 x 414.00
414.00
Cost
414.00
11.
Pro Series Shampoo bright color 500ml
1,000 x 841.00
841.00
Cost
841.00
12.
Pro Series conditioner for long-term care of colored hair Bright color 500ml
1,000 x 841.00
841.00
Cost
841.00
13.
Clear shampoo Active sport 2in1 for men 400 ml
1,000 x 1,200.00
1,200.00
Cost
1,200.00
14.
Bio World (HYDRO THERAPY)Micellar water 5in1, 445ml
1,000 x 1,152.00
1,152.00
Cost
1,152.00
15.
Bio World (HYDRO THERAPY) Gel-mousse for washing with hyaluronic acid, 250ml
1,000 x 1,152.00
1,152.00
Cost
1,152.00
16.
[RX]-Sodium chloride 0.9%, 100 ml, vial.
1,000 x 168.00
168.00
Cost
168.00
17.
[RX]-Disol solution 400 ml, fl.
1,000 x 163.00
163.00
Cost
163.00
18.
Tagansorbent with silver ion No. 30, por.
1,000 x 1,526.00
1,526.00
Cost
1,526.00
19.
[RX]-Cerucal 2%, 2 ml, No. 10, amp.
2,000 x 396.00
792.00
Cost
792.00
20.
[RX]-Andazole 200 mg, No. 40, tab.
1,000 x 7,330.00
7,330.00
Cost
7,330.00
Bank card:
18,009.00
TOTAL:
18,009.00
incl. VAT 12%:
0.00
Fiscal sign:
2331180266
Time: 04/18/2019 11:13:58
Nur-Sultan, Kazakhstan, Mangilik El, 19, no.-5
Fiscal data operator: Kazakhtelecom JSC To check the receipt, go to the website: consumer.oofd.kz
FISCAL CHECK
FP
INK OFD: 311559
KKM code KGD (RNM): 620300145311
ZNM: SWK00034965
WEBKASSA.KZ"""



## Extract all prices from the receipt:

prices=  re.findall(r'\d{1,3}(?:,\d{3})*\.\d{2}', txt)
print(prices)

## Find all product names:

product_Name = re.findall(r'\d+\.\s*\n(.+)', txt)
for product in product_Name:
    print(product)


# Calculate total amount
total = sum(float(price.replace(',', '')) for price in prices ) 

print(total, " US Dollar")

# Extract date and time information
import re

datetime_info = re.search(r'Time:\s+(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2}:\d{2})', txt)

if datetime_info:
    date = datetime_info.group(1)
    time = datetime_info.group(2)

    print("Date:", date)
    print("Time:", time)


# FInd Payment Method
import re

payment = re.search(r'(Bank card|Cash|Credit card|Debit card):', txt)

if payment:
    print("Payment Method:", payment.group(1))


# json output:

import re
import json

# Extract products
products = re.findall(r'\d+\.\s*\n(.+)', txt)

# Extract prices
prices = re.findall(r'Cost\s+([\d,]+\.\d{2})', txt)

# Extract date and time
datetime_info = re.search(
    r'Time:\s+(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2}:\d{2})', txt
)

date = datetime_info.group(1)
time = datetime_info.group(2)

# Extract payment method
payment = re.search(r'(Bank card|Cash|Credit card|Debit card):', txt)
payment_method = payment.group(1)

# Calculate total
total = sum(float(price.replace(',', '')) for price in prices)

# Build JSON
receipt_data = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "products": [],
    "total_amount": total
}

# Combine products + prices
for product, price in zip(products, prices):
    receipt_data["products"].append({
        "name": product,
        "price": float(price.replace(',', ''))
    })

# Print JSON nicely
print(json.dumps(receipt_data, indent=4))
