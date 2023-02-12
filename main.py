import time
import json
import telebot

##TOKEN DETAILS
TOKEN = "KUPON"

BOT_TOKEN = "6264694599:AAF4NsB029DlXhloD7UuQ8u3a4V000EqSQw"
PAYMENT_CHANNEL = "https://t.me/+FT_1ZBRxPV5jYzkx" #add payment channel here including the '@' sign
OWNER_ID = 6204092032 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@utamaku1"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"] 
              #you  add as many channels here and also add the '@' sign before channel username
Daily_bonus = 10 #Put daily bonus amount here!
Mini_Withdraw = 1000  #remove 0 and add the minimum withdraw u want to set
Per_Refer = 1.5 #add per refer bonus here

bot = telebot.TeleBot(BOT_TOKEN)

def menu(id):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('🆔 CEK SALD')
    keyboard.row('👑 VERIFIKAS')
    bot.send_message(id, "*🏡 Klik di bagian bawah sini menu 👇👇*", parse_mode="Markdown",
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
   try:
    if message.text == '🆔 CEK SALDO':
        data = json.load(open('users.json', 'r'))
        accmsg = '*👮 User : {}\n\n⚙️ Status Vip : *`{}`*\n\n💸 Kupon : *`{}`*\n\n Minimal Tukar👉 {}*'
        user_id = message.chat.id
        user = str(user_id)

        if user not in data['balance']:
            data['balance'][user] = 925
        if user not in data['wallet']:
            data['wallet'][user] = "none"

        json.dump(data, open('users.json', 'w'))

        balance = data['balance'][user]
        wallet = data['wallet'][user]
        msg = accmsg.format(message.from_user.first_name,
                            wallet, balance, Mini_Withdraw)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    if message.text == '🙌🏻 Undang':
        data = json.load(open('users.json', 'r'))
        ref_msg = "*⏯️ Total Undang : {} Users\n\n👥 Undangan System\n\n1 Level:\n🥇 Level°1 - {} {}\n\n🔗 Undang Link ⬇️\n{}*"

        bot_name = bot.get_me().username
        user_id = message.chat.id
        user = str(user_id)

        if user not in data['referred']:
            data['referred'][user] = 0
        json.dump(data, open('users.json', 'w'))

        ref_count = data['referred'][user]
        ref_link = 'https://telegram.me/{}?start={}'.format(
            bot_name, message.chat.id)
        msg = ref_msg.format(ref_count, Per_Refer, TOKEN, ref_link)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    if message.text == "👑 VERIFIKASI":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        send = bot.send_message(message.chat.id, "_🔐 Silahkan Ketik YES dan kirim kesini._",
                                parse_mode="Markdown", reply_markup=keyboard)
        # Next message will call the name_handler function
        bot.register_next_step_handler(message, trx_address)
    if message.text == "💌 Info":
        user_id = message.chat.id
        user = str(user_id)
        
        data = json.load(open('users.json', 'r'))
        #bot.send_message(user_id, "*🎁 Bonus Button is Under Maintainance*", parse_mode="Markdown")
        if (user_id not in bonus.keys)(bonus[user_id]):
            data['balance'][(user)] += Daily_bonus
            bot.send_message(
                user_id, f"*Cara Dapat Group VIP secara gratis !!!\n1. Di menu ada undang kemudian klik dan salin kode undangan\n 2. Kemudian bagikan ke group Wa, FB, Tele, Yt dan lain!!\n3. Cek Saldo Dulu Jika sudah mencapai 1000 kupon, kamu bisa langsung menukarkan pada menu penukaran\n4. Klik link vip yang telah tersedia\n\n📢 Info Pada Menu 👑 Member Vip!!! Menggunakan Password dari Admin!!\n🎟 Penukaran Secara Otomatis, Jika Sudah Sesuai Maka link Vip akan dikirim kan. Kamu bisa lihat Tutorial di sini @tutorboss @tutorboss https://t.me/tutorboss\n\n✅ Selamat Kamu baru saja mendapatkan bonus pertama sebesar 💵 🎁 {Daily_bonus} {TOKEN}*")
            bonus[user_id]
            json.dump(data, open('users.json', 'w'))
        else:
            bot.send_message(
                message.chat.id, "*Cara Dapat Group VIP secara gratis !!!\n1. Di menu ada undang kemudian klik dan salin kode undangan\n 2. Kemudian bagikan ke group Wa, FB, Tele, Yt dan lain!!\n3. Cek Saldo Dulu Jika sudah mencapai 1000 kupon, kamu bisa langsung menukarkan pada menu penukaran\n4. Klik link vip yang telah tersedia\n\n📢 Info Pada Menu 👑 Member Vip!!! Menggunakan Password dari Admin!!\n🎟 Penukaran Secara Otomatis, Jika Sudah Sesuai Maka link Vip akan dikirim kan. Kamu bisa lihat Tutorial di sini @tutorboss @tutorboss https://t.me/tutorboss\n\n❌ Yah bonus sudah habis, Silakhan besok lagi  🕚*",parse_mode="markdown")
        return

    if message.text == "📊Jumlah Pengguna":
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        msg = "*📊 Total Semua Member : {} Users\n\n*"
        msg = msg.format(data['total'], TOKEN)
        bot.send_message(user_id, msg, parse_mode="Markdown")
        return

    if message.text == "💸 Tukar Kupon":
        user_id = message.chat.id
        user = str(user_id)

        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 925
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        wall = data['wallet'][user]
        if wall == "none":
            bot.send_message(user_id, "_❌ Data Anda masih kosong ⁉️ VERIFIKASI Dulu di menu 👉 🧾 Verivikasi_",
                             parse_mode="Markdown")
            return
        if bal >= Mini_Withdraw:
            bot.send_message(user_id, "_*✅ Selamat, kamu sudah berhasil 😊 sekarang kamu bisa melakukam penukaran Kupon. Ketik dan kirim 1000 Kupon 🤗*_",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, amo_with)
        else:
            bot.send_message(
                user_id, f"*❌Kupon anda tidak cukup untuk melakukan penukaran silahkan undang teman sebanyak banyaknya 🚹!! Minimal Penukaran 💵 {Mini_Withdraw} {TOKEN} *", parse_mode="Markdown")
            return
   except:
        bot.send_message(message.chat.id, " *Cara Dapat Group VIP secara gratis !!!\n\n 1. Di menu ada undang kemudian klik dan salin kode undangan Dulu\n\n 2. Kemudian bagikan ke group Wa, FB, Tele, Yt dan lain!!\n\n 3. Cek Saldo Jika sudah mencapai 1000 kupon, kamu bisa langsung menukarkan pada menu penukaran\n\n4. Klik link vip yang telah tersedia\n\n📢 Info Pada Menu 👑 KLIK VARIFIKASI DULU !!! Untuk menukarkan kupon !!\n\n🎟 Penukaran Secara Otomatis, Jika Sudah Sesuai Maka link Vip akan dikirim kan. \n\nKamu bisa lihat Tutorial di sini 👉 @tutorboss @tutorboss https://t.me/tutorboss *")
        bot.send_message(OWNER_ID, "Pengguna mengecek info pada sub menu "+message.text)
        return

def trx_address(message):
   try:
    if message.text == "🚫 Kembali":
        return menu(message.chat.id)
    if len(message.text) == 3:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        data['wallet'][user] = message.text

        bot.send_message(message.chat.id, "*✅ Terimakasih telah melakukan veryfikasi bot anda, Sekarang anda dapat menukarkan Kupon Anda di menu penukaran\n\n " +
                         data['wallet'][user]+"*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
        return menu(message.chat.id)
    else:
        bot.send_message(
            message.chat.id, "*⁉️📵 Apa yang kamu masukan salahkan coba ketik dan kirim ulang YES *", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "*Mukin bot sedang Error coba ulang kembali* ")
        bot.send_message(OWNER_ID, "Salah satu user telah melakukan\n Penukaran Kupon sebesar: "+message.text)
        return

def amo_with(message):
   try:
    user_id = message.chat.id
    amo = message.text
    user = str(user_id)
    data = json.load(open('users.json', 'r'))
    if user not in data['balance']:
        data['balance'][user] = 925
    if user not in data['wallet']:
        data['wallet'][user] = "0"
    json.dump(data, open('users.json', 'w'))

    bal = data['balance'][user]
    wall = data['wallet'][user]
    msg = message.text
    if msg.isdigit() == False:
        bot.send_message(
            user_id, "_📛 Tidak boleh ada Huruf Titik koma!! Semua angka Sesuai minimal penukaran_", parse_mode="Markdown")
        return
    if int(message.text) < Mini_Withdraw:
        bot.send_message(
            user_id, f"_❌Kupon anda tidak cukup untuk melakukan penukaran silahkan undang teman sebanyak banyaknya 🚹!! Minimal Penukaran 💵 {Mini_Withdraw} {TOKEN}_", parse_mode="Markdown")
        return
    if int(message.text) > bal:
        bot.send_message(
            user_id, "_❓Kamu menukarkan dengan jumlah banyak dari hasil kupon yang kamu miliki !! penukaran minimal 💵 1000 Kupon_", parse_mode="Markdown")
        return
    amo = int(amo)
    data['balance'][user] -= int(amo)
    bot_name = bot.get_me().username
    json.dump(data, open('users.json', 'w'))
    bot.send_message(user_id, "✅* Selamat Kupon Berhasil Ditukarkan Secara Otomatis\n\n💹 Channel Vip :- "+PAYMENT_CHANNEL +"*", parse_mode="Markdown")

    markupp = telebot.types.InlineKeyboardMarkup()
    markupp.add(telebot.types.InlineKeyboardButton(text='🍀 BOT LINK', url=f'https://telegram.me/{bot_name}?start={OWNER_ID}'))

    send = bot.send_message(PAYMENT_CHANNEL,  "✅* New Withdraw\n\n⭐ Amount - "+str(amo)+f" {TOKEN}\n🦁 User - @"+message.from_user.username+"\n💠 Wallet* - `"+data['wallet'][user]+"`\n☎️ *User Referrals = "+str(
        data['referred'][user])+"\n\n🏖 Bot Link - @"+bot_name+"\n⏩ Please wait our owner will confrim it*", parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markupp)
   except:
        bot.send_message(message.chat.id, "1")
        bot.send_message(OWNER_ID, "Salah satu user telah melakukan!\n Penukaran Kupon sebesar: "+message.text)
        return

if __name__ == '__main__':
    bot.polling(none_stop=True)
