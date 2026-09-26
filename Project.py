# ข้อมูลรายการอาหารและราคา
MENU = {
    1: {"name": "ข้าวผัดกะเพราไข่ดาว", "price": 60},
    2: {"name": "ข้าวมันไก่", "price": 50},
    3: {"name": "ผัดไทยกุ้งสด", "price": 70},
    4: {"name": "ชาไทยเย็น", "price": 30},
    5: {"name": "น้ำดื่ม", "price": 10}
}


# ---------------------------------------------------------

# ---------------------------------------------------------
def display_menu():
    print("\n" + "=" * 45)
    print("             --- รายการอาหาร ---")
    print("=" * 45)
    for key, item in MENU.items():
        print(f"  [{key}] {item['name']:<22} {item['price']:>5} บาท")
    print("=" * 45)


# ---------------------------------------------------------

# ---------------------------------------------------------
def take_order():
    cart = []
    while True:
        display_menu()
        print("💡 พิมพ์ '0' เมื่อเลือกรายการอาหารเสร็จแล้ว")
        
        # [Try-Except จุดที่ 1] ดักจับการกรอกข้อมูลที่ไม่ใช่ตัวเลข
        try:
            choice = int(input("กรุณาเลือกหมายเลขเมนู: "))
            
            if choice == 0:
                break
                
            if choice not in MENU:
                print("\n❌ ไม่มีหมายเลขเมนูนี้ในระบบ กรุณาเลือกใหม่อีกครั้ง")
                continue
            
            quantity = int(input(f"กรุณากรอกจำนวนสำหรับ '{MENU[choice]['name']}': "))
            if quantity <= 0:
                print("\n❌ จำนวนต้องมากกว่า 0 รายการนี้จะไม่ถูกเพิ่มในตะกร้า")
                continue
                
            item_total = MENU[choice]["price"] * quantity
            cart.append({
                "name": MENU[choice]["name"],
                "price": MENU[choice]["price"],
                "quantity": quantity,
                "total": item_total
            })
            print(f"\n✔️ เพิ่ม {MENU[choice]['name']} จำนวน {quantity} จาน เรียบร้อย!")
            
        except ValueError:
            print("\n❌ ป้อนข้อมูลไม่ถูกต้อง! กรุณากรอกเฉพาะตัวเลขเต็มเท่านั้น")
            
    return cart


# ---------------------------------------------------------

# ---------------------------------------------------------
def calculate_bill(cart):
    subtotal = sum(item["total"] for item in cart)
    discount = 0.0
    
   
    if subtotal >= 200:
        discount = subtotal * 0.10
        
    after_discount = subtotal - discount
    vat = after_discount * 0.07
    grand_total = after_discount + vat
    
    return subtotal, discount, vat, grand_total


# ---------------------------------------------------------

# ---------------------------------------------------------
def process_payment_and_receipt(cart):
    if not cart:
        print("\nไม่มีรายการอาหารในตะกร้า ขอบคุณที่ใช้บริการครับ")
        return

    subtotal, discount, vat, grand_total = calculate_bill(cart)
    paid_amount = 0.0
    
    
    while True:
        try:
            print(f"\n💰 ยอดชำระสุทธิทั้งหมด (รวม VAT 7%): {grand_total:.2f} บาท")
            paid_amount = float(input("กรุณากรอกจำนวนเงินที่รับมา (บาท): "))
            
            if paid_amount < grand_total:
                raise ValueError("จำนวนเงินที่รับมาไม่พอชำระยอดสุทธิ")
            break
        except ValueError as e:
            print(f"❌ ชำระเงินไม่สำเร็จ: {e} กรุณากรอกใหม่อีกครั้ง")

    change = paid_amount - grand_total

    print ("\n" + "=" * 50)
    print ("               ใบเสร็จรับเงิน / RECEIPT")
    print ("=" * 50)
    for item in cart:
        print(f"  {item['name']:<22} x{item['quantity']:<3} {item['total']:>12.2f} บาท")
    print ("-" * 50)
    print (f"  {'ยอดรวม (Subtotal):':<30} {subtotal:>12.2f} บาท")
    if discount > 0:
        print (f"  {'ส่วนลดพิเศษ (Discount 10%):':<30} -{discount:>11.2f} บาท")
    print (f"  {'ภาษีมูลค่าเพิ่ม (VAT 7%):':<30} {vat:>12.2f} บาท")
    print (f"  {'ยอดรวมทั้งสิ้น (Grand Total):':<30} {grand_total:>12.2f} บาท")
    print ("-" * 50)
    print (f"  {'รับเงินมา (Paid):':<30} {paid_amount:>12.2f} บาท")
    print (f"  {'เงินทอน (Change):':<30} {change:>12.2f} บาท")
    print ("=" * 50)
    print ("          ขอบคุณที่อุดหนุน โอกาสหน้าเชิญใหม่ครับ/ค่ะ")
    print ("=" * 50)


# ---------------------------------------------------------

# ---------------------------------------------------------
if __name__ == "__main__":
    orders = take_order()
    process_payment_and_receipt(orders)