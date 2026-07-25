# ================================
# دانشجو: ساره اخوان بهابادی 
# شماره دانشجویی: 404130333
# عنوان پروژه: شبیه‌ساز جام جهانی
# تاریخ تحویل: 1405/05/04
# ================================
import random
import csv
from Group import Group
from Team import Team
from Match import Match
from KnockoutStage import KnockoutStage
#همه چیز رو مدیریت می کنه خواندن فایل csvوقرعه کشی گروه ها تا اجرای مرحله گروهی وحذفی,تعیین قهرمان,شبیه سازی چند باره برای محاسبه درصد قهرمانی هر تیم
class WorldCupSimulator:
    #سازنده فقط سلف می گیره چون وقتی شبیه ساز جدید می سازیم هنوز هیچی  معلوم نیست
    def __init__(self):
        #یک لیست خالی می سازیم که قراره بعدش همه 32 تیم رو داخلش بریزیم
        self.hame_timha = []
        #یک لیست خالی برای 8 گروه که بعد از قرعه کشی داخلش می ریزیم
        self.groups = []
        #چهار متغیر برای چهار مرحله حذفی می سازیم
        self.yek_hashtom = None
        self.yek_chaharom = None
        self.nime_nahayi = None
        self.final = None
        self.ghahreman = None
#این متد فایل csv رو می خونه و ساخت لیست اشیا Team
    def csv_bekhan(self, filename):
       #شروع بلوک try
       #اگر خطا داد برنامه توقف نشه بره سراغ بخش except و کاری که اونجا گفته شده انجام بده
        try:
            #قبل از خوندن فایل لیست تیم ها رو خالی می کنیم چون شاید قبلا فایل خونده شده و می خوایم از اول شروع کنیم
            self.hame_timha = []
    #with openیک الگوی استاندارد پایتونه که تضمین می کنه فایل بعد از استفاده به طور خودکار بسته می شود
            with open(filename, newline='', encoding='utf-8') as f:
                #این ابزار که از کتابخانه وارد کردیم هر ردیف از فایل csv رو به صورت دیکشنری بهمون میده
                khanande = csv.DictReader(f)
                #یک حلقه که روی تک تک ردیف های csv حرکت می کنه
                for radif in khanande:
                    #برای هر ردیف یک ابجکت تیم می سازیم و چون بعضی ها رو رشته میده int می ذاریم تا تبدیل به عدد شود
                    tim = Team(radif['name'], int(radif['attack']), int(radif['defense']), int(radif['rank']))
                    #تیمی که تازه ساختیم رو به لیست همه تیم ها اضافه می کنیم
                    self.hame_timha.append(tim)
                    #بعد از این که همه ردیف های فایل خونده شد و حلقه تمام شد یک پیام موفقیت چاپ می کنیم و Trueبر می گردونیم
            print(f"تعداد {len(self.hame_timha)} تیم با موفقیت بارگذاری شد.")
            return True
        #اگر در try در پیدا کردن فایل مشکل به وجود اومد پایتون یه خطای خاص می دهد
        except FileNotFoundError:
            #یه پیام خطا چاپ می کنیم و False  رو بر می گردونیم به جای این که برنامه متوقف بشه 
            print(f"خطا: فایل {filename} پیدا نشد.")
            return False
#قرعه کشی گروه ها بر اساس سید بندی رنکینگ فیفا
    def gorouh_bandi_kon(self):
        #همه تیم ها یک لیسته و اگر این لیست خالی باشه یعنی هنوز متد های های قبلی انجام نشده
        #و چون لیست خالی یعنی نادرت با عکسش رو می گیم که درست میشه اگر درست بود که کاربر باید نام تیم ها رو وارد کنه
        #اگر لیست خالی بود و نادرست برای این که برنامه متوقف نشه با returnاز برنامه خارج می شیم
        if not self.hame_timha:
            print("ابتدا تیم‌ها را بارگذاری کنید")
            return
        #اینجا تیم ها رو بر اساس رتبه بندی فیفا مرتب می کنیم
        timha_moratab = sorted(self.hame_timha, key=lambda t: t.rank)
        #تعریف سید یک :میگه از اندیس 0 تا اندیس 7 یعنی 8 عنصر اول رو بردار که میشه همون تیم های 1 تا 8
        sid1 = timha_moratab[0:8]
        #اندیس 8 تا 15 یعنی تیم های 9 تا 16 می شود سید 2
        sid2 = timha_moratab[8:16]
        #اندیس 16 تا 23 میشه همون تیم های  17 تا 24 سید 3
        sid3 = timha_moratab[16:24]
        #اندیس 24 تا 31 میشه تیم های 25 تا 32 سید 4
        sid4 = timha_moratab[24:32]
        #هر کدوم از سید ها رو طبق خواسته pdf جداگانه به صورت تصادفی بهم می ریزیم
        random.shuffle(sid1)
        random.shuffle(sid2)
        random.shuffle(sid3)
        random.shuffle(sid4)
        #یک لیست از اسم گروه ها می سازیم چون جام جهانی هشت گروه دارد
        asami_groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        #لیست گروه شبیه ساز رو خالی می کنیم
        self.groups = []
        #و حلقه ای که 8 بار تکرار شود هر بار برای یک گروه
        for i in range(8):
            #طبق pdf برای هر گروه از 4 سید یک تیم لبر می داریم و هر گروه دقیقا یک تیم از هر سید داشته باشه
            timha_gorouh = [sid1[i], sid2[i], sid3[i], sid4[i]]
            #یک ابجکت Group می سازیم با اسم مناسب و لیست 4 تیمی که ساختیم
            g = Group(asami_groups[i], timha_gorouh)
            #و گروه تازه ساخته شده را به لیست کلی گروه ها شبیه ساز اضافه می کنیم
            self.groups.append(g)
            #بعد از تموم شدن حلقه یک پیام موفقیت چاپ می کنیم
        print("قرعه‌کشی گروه‌ها با موفقیت انجام شد.")
#اجرای مرحله گروهی و نمایش جدول هر گره 
    def marhale_gorouhi_ejra_kon(self):
        #اگر لیست گروه ها خالی باشد و قرعه کشی انجام نشده باشد قبلا پیام خطا چاپ می شود و با دستورreturn متد همینجا متوقف میشه
        if not self.groups:
            print("ابتدا قرعه‌کشی را انجام دهید")
            return
        #حلقه شروع می شود و روی 8 گروه موجود در لیست حرکت می کند
        for g in self.groups:
            #کار این متد اینه که تمام 6 مسابقه رفت و برگشت ان گروه خاص رو شبیه سازی کنه نتیجه رو مشخص کنه و امار تیم های درون اون گروه رو بروزرسانی کند
            g.hame_bazi_ha()
            
            print(f"===== Group {g.name} =====")
            #این متد تیم های درون گروه را بر اساس قوانین فوتبال  مرتب می کند و یک لیست مرتب شده از تیم ها رو بر می گردونه
            rotbe = g.rotbe_bandi()
            #یک حلقه روی لیست rotbe شروع می کند تابع enu...به لیست شماره اندیس می دهد و از 1 شروع می شود 
            for rank, t in enumerate(rotbe, start=1):
                #جدول رتبه‌بندی را برای هر تیم به صورت یک خط چاپ می‌کند
                print(f"{rank}. {t.name}: {t.emtiaz} pts, GD {t.tafazol_gol():+d}, GF {t.gol_zade}")
#ساخت براکت حذفی یک‌هشتم بر اساس قانون فیفا
    def bracket_besaz(self):
#دو تا لیست خالی  ساخته می شود تا به ترتیب تیم های اول و دوم هر گروه را در خود ذخیره کند
        avval_ha = []
        dovom_ha = []
        #حلقه ای که روی همه گرو های موجود حرکت میکنه و دو تیمئ برتر گروه را بر می گردونه
        for g in self.groups:
            a, b = g.do_tim_bartar()
            avval_ha.append(a)
            dovom_ha.append(b)
#این تیکه قانون براکت ثابت جام جهانی اجرا می کند و خروجیش یک لیست از تاپل ها است 
        joft_ha = [
            (avval_ha[0], dovom_ha[1]),
            (avval_ha[2], dovom_ha[3]),
            (avval_ha[4], dovom_ha[5]),
            (avval_ha[6], dovom_ha[7]),
            (avval_ha[1], dovom_ha[0]),
            (avval_ha[3], dovom_ha[2]),
            (avval_ha[5], dovom_ha[4]),
            (avval_ha[7], dovom_ha[6]),
        ]

        bazi_ha = []
        #تک تک تاپل های لیست باز می شوند و برای هر کدوم یک شی از کلاس Match  ساخته می شود و این مرحله حذفی هست
        for tim1, tim2 in joft_ha:
            bazi_ha.append(Match(tim1, tim2, marhale_hazfi=True))
#یک شیء از کلاس KnockoutStage ساخته می‌شود و نام مرحله و لیست مسابقات را دریافت می کند
        self.yek_hashtom = KnockoutStage("Round of 16", bazi_ha)
#اجرای تمام مراحل حذفی: یک‌هشتم، یک‌چهارم، نیمه‌نهایی، فینال
    def marhale_hazfi_ejra_kon(self):
       #اول متد را روی شی yek_hashtom صدا می زند تا 8 مسابقه دور یک هشتم را شبیه سازی کند و تیجه هرکدام را درون همان اشیاء Match ثبت کند
        self.yek_hashtom.marhale_bazi_kon()
#متد برنده ها بده لیست برندگان تمام مسابقات اون مرحله رو بر می گردونه شامل 8 تیم برنده اس 
        barande_hashtom = self.yek_hashtom.barande_ha_bede()
# لیست خالی برای مسابقات یک چهارم ساخته می شود
#حلقه با گام 2 از 0 تا 8 حرکت می کنه
#در هر  قدم دو تیم مجاور از لیست برندگان یک‌هشتم را برداشته و یک مسابقه حذفی جدید برای آنها می‌سازد و به لیست اضافه می‌کند.
        bazi_ha_chaharom = []
        for i in range(0, 8, 2):
            bazi_ha_chaharom.append(Match(barande_hashtom[i], barande_hashtom[i+1], marhale_hazfi=True))
            # یک جعبه‌ی جدید به نام یک‌چهارم درست می‌کنیم و ۴ مسابقه‌ی ساخته‌شده را داخل آن می‌گذاریم
            # به ان جعبه می گوییم همه‌ی مسابقات داخل خودت را اجرا کن و نتیجه‌شان را مشخص کن 
            # برنده‌های این ۴ مسابقه‌ات را به من بده تا با آن‌ها، مسابقات نیمه‌نهایی را بسازیم
        self.yek_chaharom = KnockoutStage("Quarterfinals", bazi_ha_chaharom)
        self.yek_chaharom.marhale_bazi_kon()
        barande_chaharom = self.yek_chaharom.barande_ha_bede()
#لیست مسابقات نیمه‌نهایی) ۲ مسابقه(
        bazi_ha_nimenahayi = []
        #جفت‌سازی برندگان یک‌چهارم۱↔۲ و ۳↔۴
        for i in range(0, 4, 2):
           bazi_ha_nimenahayi.append(Match(barande_chaharom[i], barande_chaharom[i+1], marhale_hazfi=True))
            # اجرای نیمه‌نهایی و گرفتن دو فینالیست
        self.nime_nahayi = KnockoutStage("Semifinals", bazi_ha_nimenahayi)
        self.nime_nahayi.marhale_bazi_kon()
        barande_nimenahayi = self.nime_nahayi.barande_ha_bede()
#فینال: ساخت، اجرا و ثبت قهرمان
        bazi_final = Match(barande_nimenahayi[0], barande_nimenahayi[1], marhale_hazfi=True)
        self.final = KnockoutStage("Final", [bazi_final])
        self.final.marhale_bazi_kon()

        self.ghahreman = self.final.barande_ha_bede()[0]
# یک دوره کامل از مسابقات را اجرا می‌کند از مرحله گروهی تا فینال
    def jam_kamel_ejra_kon(self):
        #یک حلقه رو همه تیم ها اجرا می شود  و ممکن است آمار تیم‌ها از شبیه‌سازی قبلی باقی مانده باشد. این خط، همه‌چیز را به حالت اولیه صفر برمی‌گرداند
        for t in self.hame_timha:
            t.riset_amar()
            #یک حلقه رو همه گروه ها اجرا می شود و تمام 6 مسابقات هر گروه رو شبیه سازی می شود  و امار تیم به روز می شود
        for g in self.groups:
            g.hame_bazi_ha()
            #ن متد، بر اساس نتایج مرحله‌ی گروهی ، براکت مرحله‌ی حذفی یک‌هشتم نهایی را می سازد
        self.bracket_besaz()
        #این متد، کل مراحل حذفی یک‌هشتم، یک‌چهارم، نیمه‌نهایی و فینال را پشت سر هم اجرا می‌کند
        self.marhale_hazfi_ejra_kon()
        print("===== FINAL =====")
        print(self.final.bazi_ha[0])
        print(f"قهرمان جام جهانی: {self.ghahreman.name}")
        #شیء تیم قهرمان را به عنوان خروجی از تابع برمی‌گردوند
        return self.ghahreman
   #شبیه‌سازی چندباره و محاسبه درصد قهرمانی هر تیم
    def shabih_sazi_1000_bar(self, tedad=1000):
        
        #اگر تعداد شبیه سازی صفر و منفی باشد  متد با دستور return متوقف می شود
        if tedad <= 0:
            print("خطا: تعداد شبیه‌سازی باید مثبت باشد")
            return
#  این دیکشنری تعداد قهرمانی‌های هر تیم را در طول شبیه‌سازی‌ها می شمارد
        shomaresh_ghahremani = {}
        #یک حلقه برای تمام تمام تیم ها اجرا می شود و  نام اون به عنوان کلید در دیکشنری  ثبت می شود و مقدار ان صفر قرار داده می شود 
        for t in self.hame_timha:
            shomaresh_ghahremani[t.name] = 0
        for shomare in range(tedad):
            for t in self.hame_timha:
                #در ابتدای هر شبیه سازی یک حلقه روی همه تیم ها حرکت می کنه و امار فوتبال اونا رو صفر می کنه
                t.riset_amar()
                #ر هر شبیه‌سازی، ترکیب گروه‌ها باید متفاوت باشد تا بتوانیم درصد قهرمانی واقعی را محاسبه کنیم
            self.gorouh_bandi_kon()
            for g in self.groups:
                #مرحله‌ی گروهی برای این قرعه‌کشی جدید اجرا می‌شود
                g.hame_bazi_ha()
                #ابتدا براکت حذفی ساخته می شود و سپس تمام مراحل حذفی اجرا می شوند
            self.bracket_besaz()
            self.marhale_hazfi_ejra_kon()
 #نام تیم قهرمان را می گیرد و به دیکشنری شماره قهرمانی مراجعه می کند و مقدار مربوط به ان تیم یک واحد افزایش پیدا می دهد
            shomaresh_ghahremani[self.ghahreman.name] += 1
        print(f"شبیه‌سازی {tedad} بار انجام شد.")
        print("درصد قهرمانی هر تیم:")
        # مرتب‌سازی تیم‌ها بر اساس تعداد قهرمانی )نزولی(
        moratab = sorted(shomaresh_ghahremani.items(), key=lambda x: x[1], reverse=True)
        #محاسبه و چاپ درصد قهرمانی تیم)فقط تیم های با برد مثبت(
        for name, tedad_bord in moratab:
            if tedad_bord > 0:
                #محاسبه درصد قهرمانی
                darsad = (tedad_bord / tedad) * 100
                #چاپ با یک رقم اعشار
                print(f"{name}: {darsad:.1f}%")
#نمایش براکت حذفی آخرین شبیه‌سازی
    def bracket_namayesh_bede(self):
       #اگر خالی باشد خطا چاپ می شود و با دستورreturn متوقف می شود متد
        if not self.final:
            print("ابتدا جام را اجرا کنید")
            return
        print("===== Knockout Bracket =====")
        #این متد وظیفه دارد تمام مسابقات اون مرحله را به صورت خوانا چاپ می کند
        self.yek_hashtom.natije_namayesh()
        self.yek_chaharom.natije_namayesh()
        self.nime_nahayi.natije_namayesh()
        self.final.natije_namayesh()
        #نام تیم قهرمان را چاپ می کند
        print(f"Champion: {self.ghahreman.name}")
        