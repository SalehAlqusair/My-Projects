Hello = input("اهلًا بك في حاسب الاراضي اضغط Enter للاكمال في التطبيق!") #ترحيب
City = input("بريدة [1]، الرياض [2] ") #المدينة

if City == ("1"): # بريدة
    neighborhood = input("حي الريان [1]، الاسكان [2]، حي الرحاب [3]") # الاحياء

    if neighborhood == ("1"): # حي الريان
        # هذا سعر المتر
        price_per_meter = 1410

        # نطلب من المستخدم يدخل كم متر يبي
        area = input("اكتب كم متر تبي تشتري: ")

        # نحول المدخل من نص إلى رقم
        area = float(area)

        # نحسب السعر الكلي بضرب المساحة في سعر المتر
        total_price = area * price_per_meter

        # نطبع السعر النهائي
        print("السعر الكلي للأرض هو:")
        print(total_price, "SAR")

    if neighborhood == ("2"): #حي الاسكان
        # هذا سعر المتر
        price_per_meter = 1200

        # نطلب من المستخدم يدخل كم متر يبي
        area = input("اكتب كم متر تبي تشتري: ")

        # نحول المدخل من نص إلى رقم
        area = float(area)

        # نحسب السعر الكلي بضرب المساحة في سعر المتر
        total_price = area * price_per_meter

        # نطبع السعر النهائي
        print("السعر الكلي للأرض هو:")
        print(total_price, "SAR")

    if neighborhood == ("3"): #حي الرحاب
        # هذا سعر المتر
        price_per_meter = 1450

        # نطلب من المستخدم يدخل كم متر يبي
        area = input("اكتب كم متر تبي تشتري: ")

        # نحول المدخل من نص إلى رقم
        area = float(area)

        # نحسب السعر الكلي بضرب المساحة في سعر المتر
        total_price = area * price_per_meter

        # نطبع السعر النهائي
        print("السعر الكلي للأرض هو:")
        print(total_price, "SAR")


elif City == ("2"):
    neighborhood = input("حي النرجس [1]، حي العارض [2]، حي الرمال [3]")  # الاحياء

    if neighborhood == ("1"):  # حي النرجس
        # هذا سعر المتر
        price_per_meter = 3500

        # نطلب من المستخدم يدخل كم متر يبي
        area = input("اكتب كم متر تبي تشتري: ")

        # نحول المدخل من نص إلى رقم
        area = float(area)

        # نحسب السعر الكلي بضرب المساحة في سعر المتر
        total_price = area * price_per_meter

        # نطبع السعر النهائي
        print("السعر الكلي للأرض هو:")
        print(total_price, "SAR")

    if neighborhood == ("2"):  # حي الرمال
        # هذا سعر المتر
        price_per_meter = 2000

        # نطلب من المستخدم يدخل كم متر يبي
        area = input("اكتب كم متر تبي تشتري: ")

        # نحول المدخل من نص إلى رقم
        area = float(area)

        # نحسب السعر الكلي بضرب المساحة في سعر المتر
        total_price = area * price_per_meter

        # نطبع السعر النهائي
        print("السعر الكلي للأرض هو:")
        print(total_price, "SAR")

    if neighborhood == ("3"): # حي العارض
        # هذا سعر المتر
        price_per_meter = 3000

        # نطلب من المستخدم يدخل كم متر يبي
        area = input("اكتب كم متر تبي تشتري: ")

        # نحول المدخل من نص إلى رقم
        area = float(area)

        # نحسب السعر الكلي بضرب المساحة في سعر المتر
        total_price = area * price_per_meter

        # نطبع السعر النهائي
        print("السعر الكلي للأرض هو:")
        print(total_price, "SAR")