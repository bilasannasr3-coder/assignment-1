# برنامج إدارة النقاط في اللعبة
print("برنامج إدارة النقاط في اللعبة")

# الحصول على النقاط الحالية
current_points = int(input("أدخل النقاط الحالية للطالب: "))

# حساب النقاط المعدلة
if current_points < 50:
    new_points = current_points + 10
    print(f"النقاط أقل من 50، تم إضافة 10 نقاط")
elif current_points >= 50 and current_points < 60:
    new_points = current_points + 5
    print(f"النقاط بين 50 و60، تم إضافة 5 نقاط")
else:
    new_points = current_points
    print(f"النقاط 60 أو أكثر، لم يتم إضافة أي نقاط")

# عرض النتائج
print(f"النقاط الحالية: {current_points}")
print(f"النقاط بعد التعديل: {new_points}")