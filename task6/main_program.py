from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
items_list = []

class PurchaseItem:
    def __init__(self, name):
        self.name = name
        self.added_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def home_page():
    print("عرض الصفحة الرئيسية")  # للتdebug
    print("عدد العناصر:", len(items_list))  # للتdebug
    return render_template('purchase_page.html', items=items_list)

@app.route('/add_item', methods=['POST'])
def add_new_item():
    item_name = request.form.get('item_name', '').strip()
    print("محاولة إضافة:", item_name)  # للتdebug
    
    if len(item_name) < 3:
        return render_template('purchase_page.html', 
                             items=items_list, 
                             error="العنصر يجب أن يحتوي على 3 حروف على الأقل",
                             item_name=item_name)
    
    for item in items_list:
        if item.name.lower() == item_name.lower():
            return render_template('purchase_page.html', 
                                 items=items_list, 
                                 error="هذا العنصر موجود بالفعل في القائمة",
                                 item_name=item_name)
    
    items_list.append(PurchaseItem(item_name))
    print("تم الإضافة بنجاح")  # للتdebug
    return redirect(url_for('home_page'))

@app.route('/remove_item/<int:item_id>')
def remove_item(item_id):
    print("محاولة حذف العنصر رقم:", item_id)  # للتdebug
    if 0 <= item_id < len(items_list):
        removed_item = items_list.pop(item_id)
        print("تم حذف:", removed_item.name)  # للتdebug
    return redirect(url_for('home_page'))

@app.route('/clear_all')
def clear_all_items():
    print("مسح القائمة بالكامل")  # للتdebug
    items_list.clear()
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    # التأكد من وجود مجلد templates
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("تم إنشاء مجلد templates")
    
    print("التطبيق يعمل على: http://localhost:5000")
    app.run(debug=True, port=5000)