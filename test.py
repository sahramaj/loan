
def calculate_monthly_payments(total_price, down_payment, interest_rate, months):
  """
  محاسبه اقساط ماهانه، قیمت تمام شده و سود کل با احتساب سود مرکب

  آرگومان‌ها:
    total_price: قیمت کل کالا
    down_payment: پیش پرداخت
    interest_rate: نرخ سود ماهانه (به صورت اعشاری)
    months: تعداد ماه‌های اقساط

  بازگشت:
    لیستی شامل مبالغ اقساط ماهانه، قیمت تمام شده و سود کل
  """

  # محاسبه مانده اولیه قرض
  remaining_balance = total_price - down_payment

  # لیستی برای ذخیره مبالغ اقساط
  monthly_payments = []
  total_payment = down_payment  # کل مبلغ پرداختی (شامل پیش پرداخت)
  total_interest = 0  # کل سود پرداختی

  for _ in range(months):
    # محاسبه سود ماهانه
    interest = remaining_balance * interest_rate
    total_interest += interest  # اضافه کردن سود ماهانه به کل سود

    # محاسبه قسط ماهانه (تقسیم مساوی مانده و سود بر تعداد ماه‌های باقیمانده)
    monthly_payment = (remaining_balance + interest) / (months - _)

    # اضافه کردن قسط به لیست و به کل مبلغ پرداختی
    monthly_payments.append(monthly_payment)
    total_payment += monthly_payment

    # به‌روزرسانی مانده قرض
    remaining_balance = remaining_balance + interest - monthly_payment
    

  return monthly_payments, total_payment, total_interest

# مثال استفاده:
total_price = int(input("write total price: "))
down_payment = total_price / 3
interest_rate = float(input("write profit percent: "))/100  # 4 درصد
months = int(input("write months: "))

payments, total_cost, total_interest = calculate_monthly_payments(total_price, down_payment, interest_rate, months)


print("Monthly cost:")
for i, payment in enumerate(payments, 1):
  print(f"Month {i}: {payment:,} Tooman")

print(f"Finished cost: {total_cost:,} Tooman")
print(f"Profit: {total_interest:,} Tooman")

print("Press any key to exit...")
input()


