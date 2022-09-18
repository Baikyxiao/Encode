from mailbox import linesep
from django.shortcuts import render
from urllib.parse import unquote
from urllib.parse import quote
import hashlib
from hashlib import md5
from string import ascii_letters,digits
from itertools import permutations
import bcrypt
from Crypto.Hash import MD2
import json
import time, datetime


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# 解码 base64
def decryption(inputString):
    # 对前面不是“=”的字节取索引，然后转换为2进制
    asciiList = ['{:0>6}'.format(str(bin(letters.index(i))).replace('0b', ''))
                    for i in inputString if i != '=']
    outputString = ''
    # 补齐“=”的个数
    equalNumber = inputString.count('=')
    while asciiList:
        tempList = asciiList[:4]
        # 转换成2进制字符串
        tempString = ''.join(tempList)
        # 对没有8位2进制的字符串补够8位2进制
        if len(tempString) % 8 != 0:
            tempString = tempString[0:-1 * equalNumber * 2]
        # 4个6字节的二进制  转换  为三个8字节的二进制
        tempStringList = [tempString[x:x + 8] for x in [0, 8, 16]]
        # 二进制转为10进制
        tempStringList = [int(x, 2) for x in tempStringList if x]
        # 连接成字符串
        outputString += ''.join([chr(x) for x in tempStringList])
        asciiList = asciiList[4:]
    # print(output_str)
    return outputString

# 编码 base64
def encryption(inputString):
    # 对每一个字节取ascii数值或unicode数值，然后转换为2进制
    ascii = ['{:0>8}'.format(str(bin(ord(i))).replace('0b', '')) for i in inputString]
    # 返回的加密文本
    outputString = ''
    # 不够3字节的整数倍，需要补齐“=”的个数
    equalNumber = 0
    # 对每个字符的转换
    while ascii:
        # 三个asciiw为一组
        AsciiList = ascii[:3]
        if len(AsciiList) != 3:
            # 不满三个的，在后面加“=”
            while len(AsciiList) < 3:
                equalNumber += 1
                AsciiList += ['0' * 8]
        # join方法连接成三个8字节的字符串
        tempString = ''.join(AsciiList)
        # 三个8字节的二进制，转换为4个6字节的二进制
        tempStringList = [tempString[x:x + 6] for x in [0, 6, 12, 18]]
        # 二进制转为10进制
        tempStringList = [int(x, 2) for x in tempStringList]
        # 判断是否需要补“=”,只要equakNumber大于0即需要
        if equalNumber:
            tempStringList = tempStringList[0:4 - equalNumber]
        # 装换成那64个字符
        outputString += ''.join([letters[x] for x in tempStringList])
        ascii = ascii[3:]
    # 在最后加上“=”
    outputString = outputString + '=' * equalNumber
    # 返回加密后的文本
    return outputString

# 解码 url
def decode_url(data):
    text = quote(data, 'utf-8')
    return text

# 编码 url
def encode_url(data):
    # 对字符串‘%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1’进行解密
    text = unquote(data, 'utf-8')
    return text

# 编码 sha256
def get_sha256_data(inStr: str):
    sha256 = hashlib.sha256()  # 实例化对象
    sha256.update(inStr.encode('utf-8'))  # 使用update方法加密
    return sha256.hexdigest()  # 调用hexdigest方法获取加密结果

# 编码 MD5
def encodeMD5(data):
    md5 = hashlib.md5()  # 应用MD5算法
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()

# 解码 MD5
def decrypt_md5(md5_value):
    all_letters = ascii_letters + digits + '.,;'
    if len(md5_value) != 32:
        print('error')
        return
    md5_value = md5_value.lower()
    for k in range(5, 10):
        for item in permutations(all_letters, k):
            item = ''.join(item)
            if md5(item.encode()).hexdigest() == md5_value:
                return item

# sha2 256
def sha3(str):
    encoded_str = str.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_str)
    return obj_sha3_256.hexdigest()
# sha1
def SHA1cryption(string):
    sha1 = hashlib.sha1()
    sha1.update(string.encode('utf-8'))
    return sha1.hexdigest()

def SHA224cryption(string):
    sha224 = hashlib.sha224()
    sha224.update(string.encode('utf-8'))
    return sha224.hexdigest()

def bcrypt(string):
    salt = bcrypt.gensalt(round=10)
    hashed = bcrypt.hashpw(string.encode(), salt)
    return hashed

def md2Encryption(text):
    txt = MD2.new(text.encode("utf8")).hexdigest()
    return txt

def formated(js_content):
    indent = 0
    formatted = []
    lines = js_content.split(';')
    for line in lines:
        newline = []
        for char in line:
            newline.append(char)
        if char=='{': #{ 是缩进的依据
            indent+=1
            newline.append("\n")
            newline.append("\t"*indent)
        if char=="}":
            indent-=1
            newline.append("\n")
            newline.append("\t"*indent)
        formatted.append("\t"*indent+"".join(newline))
    ip = ''
    for line in formatted:
        ip += line
    return ip


def solve(ff, ip, key=None):
    if ff == 'To_Base64':
        return encryption(ip)
    elif ff == 'From_Base64':
        return decryption(ip)
    elif ff == 'To_MD5':
        return encodeMD5(ip)
    elif ff == 'To_URL':
        return encode_url(ip)
    elif ff == 'From_URL':
        return decode_url(ip)
    elif ff == 'To_SHA256':
        return get_sha256_data(ip)
    elif ff == "To_Binary":
        return str2bitnumarray(ip)
    elif ff == "From_Binary":
        return bitnumarray2str(ip)
    elif ff == "To_Utf-8_Binary":
        return str2bitarray(ip)
    elif ff == "To_upper":
        return to_upper(ip)
    elif ff == "To_lower":
        return to_lower(ip)
    elif ff == "To_capital":
        return to_capital(ip)
    elif ff == "To_title":
        return to_title(ip)
    elif ff == "Get_format_date":
        return get_format_date(ip)
    elif ff == "Date_to_stamp":
        return date_to_stamp(ip)
    elif ff == "Get_current_datestamp":
        return get_current_datestamp()
    elif ff == "Get_current_date":
        return get_current_date()
    elif ff == 'JavaScript':
        return formated(ip)
    



def index(request):
    if request.method == "GET":
        context = {}
        ip = request.GET.get('input')
        ff = request.GET.get('fun')
        key = request.GET.get('key')
        if ip != None:
            print(ip)
            context['input'] = ip
            context['value'] = ff
            context['key'] = key
            context['output'] = solve(ff, ip, key)
        else:
            context['input'] = ''
            context['value'] = ''
            context['key'] = ''
            context['output'] = ''
        print(context)
        return render(request, 'index.html', context)
    elif request.method == "POST":
        context = {}
        ip = request.POST.get('input')
        ff = request.POST.get('fun')
        key = request.POST.get('key')
        if ip != None:
            print(ip)
            context['input'] = ip
            context['value'] = ff
            context['key'] = key
            print(solve(ff, ip, key))
            context['output'] = solve(ff, ip, key)
        else:
            context['input'] = ''
            context['value'] = ''
            context['key'] = '' 
            context['output'] = ''
        return render(request, 'index.html', context)


#字符串转二进制数
def str2bitnumarray(s):
    # ret = bitarray(''.join([bin(int('1' + hex(c)[2:], 16))[3:] for c in s.encode('utf-8')]))
    # return ret
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
#二进制数转字符串
def bitnumarray2str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


#字符串转utf-8编码的二进制数据
def str2bitarray(bit):

    job_name = bit.encode('utf-8')
    return job_name

#utf-8二进制编码转字符串
#例：b'\xe4\xbd\xa0\xe5\xa5\xbd' --》你好
def bitarray2str(bitarray):
    job_name = bytes(bitarray).decode("utf-8")
    return job_name

#字符串转大写
def to_upper(str):
    return str.upper()
#字符串转小写
def to_lower(str):
    return str.lower()

# 把第一个字母转化为大写字母，其余小写
def to_capital(str):
    return str.capitalize()

#转化标题
def to_title(str):
    return str.title()

#时间戳转化为标准时间格式
def get_format_date(time_stamp):
    #time_stamp= 1649755347
    time_array = time.localtime(int(time_stamp))
    checkpoint = time.strftime("%Y-%m-%d %H:%M:%S", time_array )
    return checkpoint

#字符串格式转化为时间戳
def date_to_stamp(date_str):    #限定字符串格式，可以在文本框中进行提示
    #转换成时间数组
    timeArray = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp

#获取当前时间时间戳
def get_current_datestamp():
    stamp =  int(time.mktime(time.localtime(time.time())))
    return str(stamp)   #这里返回的是字符串类型的时间戳

#获取当前字符串格式时间
def get_current_date():
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
