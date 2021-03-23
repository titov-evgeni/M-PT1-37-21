import time
#c_datetime = time.strftime("%H:%M")
#print(c_datetime)
c_datetime=input('Введите текущее время: ')
#create a list
c_datetime_list = c_datetime.split(":")
#separate the list
h = c_datetime_list[0]
m = c_datetime_list[1]

m_int=int(m)


#Hours with endings
hours_WE={
    "00"  : 'первого',
    "12" :  'первого',
    "01" :  'второго',
    "13" :  'второго',
    "02" :  'третьего',
    "14" :  'третьего',
    "03" :  'четвертого',
    "15" :  'четвертого',
    "04" :  'пятого',
    "16" :  'пятого',
    "05" :  'шестого',
    "17" :  'шестого',
    "06" :  'седьмого',
    "18" :  'седьмого',
    "07" :  'восьмого',
    "19" :  'восьмого',
    "08" :  'девятого',
    "20" :  'девятого',
    "09" :  'десятого',
    "21" :  'десятого',
    "10" :  'одиннадцатого',
    "22" :  'одиннадцатого',
    "11" :  'двенадцатого',
    "23" :  'двенадцатого',
}
#hours without endings
hours_WoE={
    "00"  : 'час',
    "12" :  'час',
    "01" :  'два',
    "13" :  'два',
    "02" :  'три',
    "14" :  'три',
    "03" :  'четыре',
    "15" :  'четыре',
    "04" :  'пять',
    "16" :  'пять',
    "05" :  'шесть',
    "17" :  'шесть',
    "06" :  'семь',
    "18" :  'семь',
    "07" :  'восемь',
    "19" :  'восемь',
    "08" :  'девять',
    "20" :  'девять',
    "09" :  'десять',
    "21" :  'десять',
    "10" :  'одиннадцать',
    "22" :  'одиннадцать',
    "11" :  'двенадцать',
    "23" :  'двенадцать',
}
#hours if 00 minutes
hours_IF00={
    "01"  : 'час',
    "13" :  'час',
    "02" :  'два',
    "14" :  'два',
    "03" :  'три',
    "15" :  'три',
    "04" :  'четыре',
    "16" :  'четыре',
    "05" :  'пять',
    "17" :  'пять',
    "06" :  'шесть',
    "18" :  'шесть',
    "07" :  'семь',
    "19" :  'семь',
    "08" :  'восемь',
    "20" :  'восемь',
    "09" :  'девять',
    "21" :  'девять',
    "10" :  'десять',
    "22" :  'десять',
    "11" :  'одиннадцать',
    "23" :  'одиннадцать',
    "12" :  'двенадцать',
    "00" :  'двенадцать',
}


#minutes till 39
minutes_T39 = {
    "00" : "часов ровно",
    "01" : "одна минута",
    "02" : "две минуты",
    "03" : "три минуты",
    "04" : "четыре минуты",
    "05" : "пять минут",
    "06" : "шесть минут",
    "07" : "семь минут",
    "08" : "восемь минут",
    "09" : "девять минут",
    "10" : "десять минут",
    "11" : "одиннадцать минут",
    "12" : "двенадцать минут",
    "13" : "тринадцать минут",
    "14" : "четырнадцать минут",
    "15" : "пятнадцать минут",
    "16" : "шестнадцать минут",
    "17" : "семнадцать минут",
    "18" : "восемнадцать минут",
    "19" : "девятнадцать минут",
    "20" : "двадцать минут",
    "21" : "двадцать одна минута",
    "22" : "двадцать две минуты",
    "23" : "двадцать три минуты",
    "24" : "двадцать четыре минуты",
    "25" : "двадцать пять минут",
    "26" : "двадцать шесть минут",
    "27" : "двадцать семь минут",
    "28" : "двадцать восемь минут",
    "29" : "двадцать девять минут",
    "30" : "половина",
    "31" : "тридцать одна минута",
    "32" : "тридцать две минуты",
    "33" : "тридцать три минуты",
    "34" : "тридцать четыре минуты",
    "35" : "тридцать пять минут",
    "36" : "тридцать шесть минут",
    "37" : "тридцать семь минут",
    "38" : "тридцать восемь минут",
    "39" : "тридцать девять минут",
}
#minutes between 39 and 59
minutes_B = {
    "40" : "без двадцати минут",
    "41" : "без девятнадцати минут",
    "42" : "без восемнадцати минут",
    "43" : "без семнадцати минут",
    "44" : "без шестнадцати минут",
    "45" : "без пятнадцати минут",
    "46" : "без четырнадцати минут",
    "47" : "без тринадцати минут",
    "48" : "без двенадцати минут",
    "49" : "без одиннадцати минут",
    "50" : "без десяти минут",
    "51" : "без девяти минут",
    "52" : "без восьми минут",
    "53" : "без семи минут",
    "54" : "без шести минут",
    "55" : "без пяти минут",
    "56" : "без четырех минут",
    "57" : "без трех минут",
    "58" : "без двух минут",
    "59" : "без одной минуты",
}
if 0 < m_int < 40:
    print(minutes_T39[m], hours_WE[h])
elif 40<=m_int<=59:
    print(minutes_B[m], hours_WoE[h])
elif m_int == 0:
    print(hours_IF00[h], minutes_T39[m])
else:
    print('Произошла ошибка')


