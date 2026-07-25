# ================================
# دانشجو: ساره اخوان بهابادی 
# شماره دانشجویی: 404130333
# عنوان پروژه: شبیه‌ساز جام جهانی
# تاریخ تحویل: 1405/05/04
# ================================

import numpy as np  #برای تولید عدد گل با توزیع پواسون
import random       #برای تولید عدد تصادفی در شبیه سازی پنالتی
'''کلاس تیم فوتبال'''
class Team:
    def __init__(self,name,attack,defense,rank):
        self.name=name
        self.attack=attack
        self.defense=defense
        self.rank=rank
        #این خط ها رو  رو صفر می ذاریم چون  تیم تازه ساخته شده وهنوز هیچ تیمی بازی نکرده
        self.gol_zade=0
        self.gol_khorde=0
        self.emtiaz=0
        self.grouh=''
    def tafazol_gol(self):
        #تفاضل گل=گل زده-گل خورده
        tafazol=self.gol_zade-self.gol_khorde
        return tafazol
    #ما میخوایم جام جهانی رو چندین بار شبیه سازی کنیم و قبل هر بار باید امارقبلی تیم ها پاک شود وگرنه امار ها باهم قاطی می شود
    def riset_amar(self):
        self.gol_zade=0
        self.gol_khorde=0
        self.emtiaz=0
        #احتمال گل شدن پنالتی رو محاسبه می کنیم
    def zarbe_penalti(self, harif):
        #فرمول احتمال گل طبق پروژه
        #زننده حمله قوی داشته باشه یا مدافع دفاع ضعیف داشته باشه احتمال گل بیشتره
        ehtemal = 0.75 + (self.attack - harif.defense) / 250
        #چون احتمال گل طبق فرمول یا عدد خیلی بزرگ میشه عدد خیلی کوچیک
    #یه بازه ای  بین 0.6 تا 0.9 مشخص می کنیم
        ehtemal = max(0.6, min(0.9, ehtemal))
        #با استفاده از کتابخانه رندوم عددی بین 0 تا 1 می سازیم اگر اون عدد کمتر از احتمال بود یعنی گل شده 
        return random.random() < ehtemal
    #این متد قراره کل روند پنالتی هارو مدیریت کنه
    #خط اول تعریف متده
    def penalti_ha(self, harif):
        #دو تا متغیر می سازیم تعداد گل های پنالتی رو بشماره
        #چون هنوز هیچ پنالتی انجام نشده مقدار اولیه صفر می زاریم
        gol_man = 0
        gol_harif = 0
        #یک حلقه تشکیل می دیم 5 بار تکرار میشه چون طبق قوانین 5 ضربه استاندارد فوتبال داریم
        for i in range(5):
            #یعنی برو تو متد ضرب پنالتی که قبلا نوشتیم و اطلاعات حریف رو بفرست برای اون متد
            if self.zarbe_penalti(harif):
                #اگر شرط درست بود یکی شمارنده رو زیاد می کنیم
                gol_man += 1
                #اینجا حریف پنالتی میزنه و ما باید دفاع کنیم
            if harif.zarbe_penalti(self):
        
                gol_harif += 1
                #وقتی بعد از پنالتی قبل هنوز مساوی موندیم حلقه while تشکیل می دیم
                #و تا وقتی که گل های ما و حریف مساوی باشه ادامه داره
        while gol_man == gol_harif:
            #یک پنالتی جدید می زنیم و در متغیر من زدم یا نه ذخیره می کنیم
            zad_man = self.zarbe_penalti(harif)
            #حریف هم پنالتی میزنه و ذخیره می کنه
            zad_harif = harif.zarbe_penalti(self)
            #اگر ما گل زدیم شماره گلمون رو زیاد می کنیم
            if zad_man:
                gol_man += 1
                #اگر حریف زد همینطور
            if zad_harif:
                gol_harif += 1
                #اگر نتیجه خودمون با نتیجه حریف فرق داشت یعنی یکی جلو افتاد
            if zad_man != zad_harif:
                #پس با breakاز کل حلقه whileخارج می شیم
                break
            #هرکی تعداد گل بیشتری زده رو همراه با تعداد گل های اون بر می گردونیم
        if gol_man > gol_harif:
            return self, gol_man, gol_harif
        else:
            return harif, gol_man, gol_harif
        #این تابع میاد متد های قبلی که نوشتیم و کنار هم جمع می کنه و یه بازی رو کامل شبیه سازی می کنه
        #علاوه بر پارامتر های قبلی پارامتر مرحله حذفی دارد که به طور پیش فرض فالس در نظر گرفته شده
    def shabih_sazi_bazi(self, harif, marhale_hazfi=False):
        #این خط طبق فرمول پی دی اف میانگین کل مور انتظار خودمون رو محاسبه می کنه
        # و در اخر یه عددیه که هرچی حمله قوی تر و دفاع حریف ضعیف تر بشه انتظار گل زدنمون بیشتره
        
        lamda_man = (self.attack/100)*1.5 + (1-harif.defense/100)*0.8
        #مثل خط بالاست ولی داریمم میانگین گل مورد انتظار حریف رو حساب می‌کنه
        lamda_harif = (harif.attack/100)*1.5 + (1-self.defense/100)*0.8
        #اینجا از کتابخانه numpyاستفاده می کنیم
        #و می گیم بر اساس اون میانگینی که محاسبه کردیم یک عدد گل تصادفی ولی واقعی به نظر برسه بساز
        gol_man = np.random.poisson(lamda_man)
        #برای حریف هم همینجور
        gol_harif = np.random.poisson(lamda_harif)
        #برای وقت اضافه دو تا شرط زیر باید همزمان باشند
        #مرحله حذفی باشد و گل ها مساوی باشد
        if marhale_hazfi and gol_man == gol_harif:
            #اول لامبدایخودمون رو حساب می کنیم میانگین گلی که انتظار داریم چون وقت اضافه 30 دقیقه است ضرب در 0.33 می کنیم
            lamda_et_man = lamda_man * 0.33
            #همینجور لامبدای حریف هم حساب می کنیم
            lamda_et_harif = lamda_harif * 0.33
            #حالا بر اساس اون لامبدای تازه ساختیم یه عدد گل تصادفی برای وقت اضافی  هم می سازیم
            gol_et_man = np.random.poisson(lamda_et_man)
            #همینطور برای حریف
            gol_et_harif = np.random.poisson(lamda_et_harif)
            #حالا گل زمان اضافه رو به گل زمان 90 دقیقه اضافه می کنیم
            gol_man += gol_et_man
            #همینطور برای حریف
            gol_harif += gol_et_harif
     
            #اضافه کردن گل این بازی به مجموعه گل های زده این تیم
        self.gol_zade += gol_man
        #گل حریف این بازی  رو به گل های خورده خودمون اضافه می کنیم
        self.gol_khorde += gol_harif
        #گل این بازی حریف رو به مجوعه گل های زده تیم حریف اضافه می کنیم
        harif.gol_zade += gol_harif
        #گل خودمون رو به گل های خورده حریف اضافه می کنیم
        harif.gol_khorde += gol_man
        #اگر گل ما از حریف بیشتره طبق قانون فوتبال 3 امتیاز به خودمون اضافه می کنیم
        if gol_man > gol_harif:
            self.emtiaz += 3
            #یه متغیر جدید می سازیم و می گیم برنده این بازی خود این تیمه
            barande = self
            #اگر  گل حریف از گل ما بیشتر بود به امتیاز حریف 3 تا اضافه می کنیم
        elif gol_harif > gol_man:
            harif.emtiaz += 3
            #برنده رو حریف اعلام می کنیم
            barande = harif
        else:
            #اگر مساوی باشیم و مرحله گروهی باشد
            if not marhale_hazfi:
                #در این شرایط طبق قانون فوتبال هر دو تیم 1 امتیاز می گیرن
                self.emtiaz += 1
                harif.emtiaz += 1
                #و هیچکس برنده نمی شود
                barande = None
                
            else:
                #اگر مرحله حذفی بود و مساوی بودیم
                #چون مرحله حذفیه و باید یکی ببره می ریم سراغ  متد پنالتی
                barande, pen_man, pen_harif = self.penalti_ha(harif)
                #ایا برنده پنالتی ما بودیم؟ 3 امتیاز به خودمون اضافه می کنیم
                if barande is self:
                    self.emtiaz += 3
                    #در غیر این صورت حریف 3 امتیاز می گیرد
                    
                else:
                    harif.emtiaz += 3
                    #و 3 تا چیز رو باهم بر می گردانیم
        return gol_man, gol_harif,barande
    
    
    
    