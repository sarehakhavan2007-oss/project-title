# ================================
# دانشجو: ساره اخوان بهابادی 
# شماره دانشجویی: 404130333
# عنوان پروژه: شبیه‌ساز جام جهانی
# تاریخ تحویل: 1405/05/04
# ================================
from Team import Team
from Match import Match
from Group import Group
from KnockoutStage import KnockoutStage
from WorldCupSimulator import WorldCupSimulator


def menu_asli():
    '''منوی اصلی برنامه - تعامل با کاربر'''
    sim = WorldCupSimulator()

    while True:
        print("\n===== شبیه‌ساز جام جهانی =====")
        print("1) بارگذاری تیم‌ها از فایل CSV")
        print("2) انجام قرعه‌کشی گروه‌ها (سیدبندی خودکار)")
        print("3) اجرای مرحله گروهی و نمایش جدول هر گروه")
        print("4) اجرای کامل جام (گروهی + حذفی) و نمایش قهرمان")
        print("5) شبیه‌سازی ۱۰۰۰ باره و گزارش درصد قهرمانی")
        print("6) نمایش براکت حذفی آخرین شبیه‌سازی")
        print("7) خروج")

        entekhab = input("گزینه مورد نظر را وارد کنید: ")

        if entekhab == "1":
            filename = input("نام فایل CSV را وارد کنید: ")
            sim.csv_bekhan(filename)

        elif entekhab == "2":
            sim.gorouh_bandi_kon()

        elif entekhab == "3":
            if not sim.groups:
                print("ابتدا قرعه‌کشی را انجام دهید")
            else:
                sim.marhale_gorouhi_ejra_kon()

        elif entekhab == "4":
            if not sim.groups:
                print("ابتدا قرعه‌کشی را انجام دهید")
            else:
                sim.jam_kamel_ejra_kon()

        elif entekhab == "5":
            if not sim.hame_timha:
                print("ابتدا تیم‌ها را بارگذاری کنید")
            else:
                matn = input("تعداد شبیه‌سازی را وارد کنید (پیش‌فرض 1000): ")
                if matn.strip() == "":
                    tedad = 1000
                else:
                    tedad = int(matn)
                sim.shabih_sazi_1000_bar(tedad)

        elif entekhab == "6":
            sim.bracket_namayesh_bede()

        elif entekhab == "7":
            print("خدانگهدار!")
            break

        else:
            print("گزینه نامعتبر است. دوباره تلاش کنید.")


if __name__ == "__main__":
    menu_asli()
    
