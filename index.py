import telebot
from telebot import types
import config
import sqlite3
import time

bot = telebot.TeleBot(config.token)

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.fname = None

bosh_menyu = types.ReplyKeyboardMarkup(True, row_width=2)
menyu_1 = types.KeyboardButton('Mening tovuqlarim 🐓')
menyu_2 = types.KeyboardButton('Kanalga a`zo bo`lish ✍️')
menyu_3 = types.KeyboardButton('Bozor 🚚')
menyu_4 = types.KeyboardButton('Balans 💵')
menyu_5 = types.KeyboardButton('Shaxsiy kabinet 👨‍⚕️')
bosh_menyu.add(menyu_1, menyu_2, menyu_3, menyu_4, menyu_5)

reg_un = types.InlineKeyboardMarkup()
menyu_11 = types.InlineKeyboardButton(text="Ro`yhatdan o`tish 👨‍⚕️", callback_data="121212")
reg_un.add(menyu_11)

balans_un = types.InlineKeyboardMarkup(True)
menyu_11 = types.InlineKeyboardButton(text="Pulni chiqarish", callback_data="pulchiq")
menyu_12 = types.InlineKeyboardButton(text="Hisobni to`ldirish", callback_data="tuldir")
balans_un.add(menyu_11, menyu_12)

def sql_aloqa(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    baza = sqlite3.connect('db.db')
    c1 = baza.cursor()
    c1.execute("INSERT INTO talaba(userismi, id, tovuq, xoroz, balans, chiqbalans, ref, tuxum, oavaqt, kirit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))
    baza.commit()
    baza.close()

def sql_aloqatuxum(x1, x2, x3):
    baza = sqlite3.connect('db.db')
    c1 = baza.cursor()
    c1.execute("UPDATE talaba SET tuxum=?, oavaqt=? WHERE id=?",(x1, x2, x3))
    baza.commit()
    baza.close()

def sql_aloqatuxum1(x1, x3):
    baza = sqlite3.connect('db.db')
    c1 = baza.cursor()
    c1.execute("UPDATE talaba SET tuxum=? WHERE id=?",(x1, x3))
    baza.commit()
    baza.close()

def sql_aloqabalns(x1, x2, x3):
    baza = sqlite3.connect('db.db')
    c1 = baza.cursor()
    c1.execute("UPDATE talaba SET balans=balans+?, chiqbalans=chiqbalans+? WHERE id=?",(x1, x2, x3))
    baza.commit()
    baza.close()

def sql_userismi(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  userismi FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_id(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  id FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_tovuq(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  tovuq FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_xoroz(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  xoroz FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_balans(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  balans FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_chiqbalans(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  chiqbalans FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_ref(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  ref FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_tuxum(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  tuxum FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_oavaqt(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  oavaqt FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

def sql_kirit(x1):
    baza_tek = sqlite3.connect('db.db')
    c2 = baza_tek.cursor()
    c2.execute("SELECT  kirit FROM talaba WHERE id=(?)",(x1,))
    nat_qayt = c2.fetchall()
    baza_tek.commit()
    baza_tek.close()
    return nat_qayt

@bot.message_handler(commands=['start'])
def start_bosildi(message):
    t1 = sql_id(message.from_user.id)
    if t1 == [(message.from_user.id,)]:
        bot.send_message(message.chat.id, 'Salom 🙋. Telegram orqali vaqtingizni besamar ketkazmang 🙅. Endi telegram orqali'
                                          ' 🐓 tovuq boqishingiz va pul ishlashingiz mumkin 💵. '
                                          'Ishlagan pullaringiz albatta Sizga to`lab beriladi 💁. '
                                          'Hurmat bilan @tovuq_bot >>(Tovuq ferma 🐓)', reply_markup=bosh_menyu)
    else:
        x1 = message.from_user.username
        x2 = message.from_user.id
        x3 = 1
        x4 = 0
        x5 = 0
        x6 = 0
        x7 = 0
        x8 = 0
        x9 = int(time.time())
        x10 = 0
        sql_aloqa(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)
        bot.send_message(message.chat.id,
                         'Salom 🙋. Telegram orqali vaqtingizni besamar ketkazmang 🙅. Endi telegram orqali'
                         ' 🐓 tovuq boqishingiz va pul ishlashingiz mumkin 💵. '
                         'Ishlagan pullaringiz albatta Sizga to`lab beriladi 💁. '
                         'Hurmat bilan @tovuq_bot >>(Tovuq ferma 🐓 🐓)', reply_markup=bosh_menyu)


@bot.message_handler(content_types=["text"])
def mening_tovuqlarim(message):
    if message.text == "Mening tovuqlarim 🐓":
        t1 = sql_tovuq(message.from_user.id)
        t2 = sql_oavaqt(message.from_user.id)
        t3 = sql_tuxum(message.from_user.id)
        try:
            vaqt1 = int(time.time()) - t2[0][0]
            yigilgan_tuxum = t3[0][0] + vaqt1//14400*t1[0][0]
            qolgantuxum = vaqt1%14400
            id11 = message.from_user.id
            if yigilgan_tuxum > t3[0][0]:
                t22 = int(time.time())-qolgantuxum
                sql_aloqatuxum(yigilgan_tuxum, t22, id11)
                bot.send_message(message.chat.id, 'Sizning har bir tovug`ingiz {ts} tadan tuxum berdi, jami '
                                                  '{ts1} ta tuxum yig`ildi'.format(ts=vaqt1//14400 , ts1=vaqt1//14400*t1[0][0]))
            bot.send_photo(chat_id=message.chat.id, photo=open('rasm/tovuq.jpg', 'rb'),  caption = 'Sizda {ts} ta tovuq bor'.format(ts=t1[0][0]))
            if yigilgan_tuxum>0:
                bot.send_message(message.chat.id, 'Sizda {ts} ta tuxum bor, <<Bozor 🚚>> bo`limida Siz tuxumlarni sotishingiz mumkin.'.format(ts=yigilgan_tuxum))
            else:
                bot.send_message(message.chat.id, 'Sizda hozircha yig`ilgan tuxum yo`q')
        except:
            bot.send_message(message.chat.id, 'Xatolik yuz berdi /start ni bosing')

    if message.text == "Kanalga a`zo bo`lish ✍️":
        bot.send_message(message.chat.id, 'Quyidagi kanalga azo buling', reply_markup=reg_un)

    if message.text == "Bozor 🚚":
        try:
            t3 = sql_tuxum(message.from_user.id)
            if t3[0][0] > 0:
                balan = t3[0][0]*5
                balans = balan*0.5
                chiqbalans = balan*0.5
                sql_aloqabalns(balans, chiqbalans, message.from_user.id)
                x1 = 0
                sql_aloqatuxum1(x1, message.from_user.id)
                bot.send_message(message.chat.id, 'Sizda {tt1} ta tuxum yig`ilgan edi. \nJami {tt2} so`m pul yig`ildi\n'
                                                  'Shundan {tt3} so`m chiqarish uchun\n {tt4} so`m tovuq sotib olish uchun'.format(tt1=t3[0][0], tt2=balan, tt3=chiqbalans, tt4=balans))
            else:
                bot.send_message(message.chat.id, 'Sizda tuxum yig`ilmagan')
        except:
            bot.send_message(message.chat.id, 'Xatolik yuz berdi! /start ni bosing')

    if message.text == "Shaxsiy kabinet 👨‍⚕️":
        try:
            t1 = sql_userismi(message.from_user.id)
            t2 = sql_tovuq(message.from_user.id)
            t3 = sql_xoroz(message.from_user.id)
            t4 = sql_balans(message.from_user.id)
            t5 = sql_chiqbalans(message.from_user.id)
            t6 = sql_ref(message.from_user.id)
            t7 = sql_kirit(message.from_user.id)
            bot.send_message(message.chat.id, 'Hurmatli {tt1}! 🙋🙋\n'
                                                '🐓 Tovuqlaringiz soni {tt2} ta \n'
                                                '🐔 Xo`rozlaringiz soni {tt3} ta\n'
                                               '👬 Taklif qilgan do`stlaringiz soni {tt6} ta\n'
                                              '💰 Siz kiritgan balans {tt7} so`m\n'
                                                '💵 Sotib olish balansingiz {tt4} so`m\n'
                                              '💵 Chiqarish balansingiz {tt5} so`m\n'.format(tt1=t1[0][0], tt2=t2[0][0], tt3=t3[0][0], tt4=t4[0][0], tt5=t5[0][0], tt6=t6[0][0], tt7=t7[0][0]))
        except:
            bot.send_message(message.chat.id, 'Xatolik yuz berdi! /start ni bosing')

    if message.text == "Balans 💵":
       try:
           t4 = sql_balans(message.from_user.id)
           t5 = sql_chiqbalans(message.from_user.id)
           t7 = sql_kirit(message.from_user.id)
           bot.send_message(message.chat.id, 'Balans 💵 \n\nPulni yechib olish uchun balans: {tt1} so`m 💰\n'
                                             'Sotib olish uchun balans: {tt2} so`m 💰\n'.format(tt1=t5[0][0], tt2=t4[0][0]+t7[0][0]), reply_markup=balans_un)
       except:
           bot.send_message(message.chat.id, 'Xatolik yuz berdi! /start ni bosing')


bot.polling(none_stop=True, interval=0)



