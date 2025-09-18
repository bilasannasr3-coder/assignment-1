# برنامج تحليل سلسلة أعداد
print("برنامج تحليل سلسلة أعداد")

# الحصول على الأعداد من المستخدم
numbers_input = input("أدخل سلسلة الأعداد مفصولة بفواصل: ")

# تحويل السلسلة إلى قائمة أعداد
numbers_list = numbers_input.split(',')
numbers = [float(num.strip()) for num in numbers_list]

# الحسابات الإحصائية
average = sum(numbers) / len(numbers) if numbers else 0
max_value = max(numbers) if numbers else 0
min_value = min(numbers) if numbers else 0

# حساب عدد الأعداد الفردية والزوجية
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# تحديد الأكثر عددا
if even_count > odd_count:
    majority = "زوجية"
elif odd_count > even_count:
    majority = "فردية"
else:
    majority = "متساوية"

# عرض النتائج
print(f"\nنتائج التحليل:")
print(f"الأعداد: {numbers}")
print(f"المتوسط الحسابي: {average:.2f}")
print(f"أكبر قيمة: {max_value}")
print(f"أصغر قيمة: {min_value}")
print(f"عدد الأعداد الزوجية: {even_count}")
print(f"عدد الأعداد الفردية: {odd_count}")
print(f"الأكثر عددا: {majority}")