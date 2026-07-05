units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200: 
    bill = units * 7
else:
    bill = units * 10

gst = bill * 0.18
total_bill = bill + gst

print("Bill Amount =", bill)
print("GST (18%) =", gst)
print("Total Bill =", total_bill)
