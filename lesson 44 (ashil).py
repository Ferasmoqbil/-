# فقرة الاسئله


days = int(input('which day u have born? (1-31)'))
months = int(input('which month u have born? (1-12)'))
years = int(input('which year u have born? '))


# يعطي الكود تاريخ اليوم عشان يقدر يحسب كم عمره بالضبط


year_now = 2026
month_now = 8+1
day_now = 8+1
years -= year_now
months -= month_now
days -= day_now
print(f'You are {abs(years)} years, {abs(months)} months, and {abs(days)} days old u have to ')


# كود إضافي توضعه في نهاية الكود الأساسي تماماً
# (يحسب كم باقي له من أيام وشهور ليدخل السنة التي تلي عمره الحالي)


current_age_years = abs(years)
current_age_months = abs(months)
current_age_days = abs(days)


# حساب ما تبقى لإكمال السنة القادمة (مثلاً لو عمره 16 و 8 أشهر، نحسب كم باقي ليكمل 17 سنة)


rem_months = 12 - current_age_months
rem_days = 30 - current_age_days


#print


print(f"you have to end this year:{rem_months} mounth and {rem_days} days")