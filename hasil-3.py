# uncompyle6 version 3.3.4
# Python bytecode 3.7
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 11:21:56) 
# [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
import os, sys, marshal, time

def marsha():
    os.system('clear')
    os.system('sh cnxn1xnxckzopsapapapappslzzlxlxlxxxlxcxxkxkxkxkxkxkxkxkxlalapqpqpqpqlalalallalzlxlxlxkxxkxkxxmxnnxnxmxxklxlxlxlslapqppqpwlslslzlzlxlxlxlxlxkxmxmzmsmamqmqmalalaospzpzpxxpxpxpxppxxpxkxxkzmnsnsnsnsmskzlxoxoxoxkzkkskakalwqlqpqpqpqppqqppqpqpqpqpqpalslalslsl.sh')
    print('\x1b[34;1m Ex\x1b[31;1m:\x1b[32;1m(\x1b[39;1m/sdcard/script.py\x1b[32;1m)')
    print(' ')
    a = input('\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1mMasukan Nama File\x1b[31;1m: \x1b[1;39m')
    os.system('python2 lxmxmmzlalpapalalalLLLlzmzmznxnxnxxnnxxnmxmxkzlalapapalalalalxmxmmzlalpapalalalLLLlzmzmznxnxnxxnnxxnmxmxkzlalapapalalalalalllxmxmmzlalpapalalalLLLlzmzmznxnxnxxnnxxnmxmxkzlalapapalalalalxmxmmzlalpapalalalLLLlzmzmznxnxnxxnnxxnmxmxkzlalapapalalalalallalal.py')
    f = open(a).read()
    s = f.replace('\r\n', '\n')
    s = s.replace('\r', '\n')
    if s:
        if s[(-1)] != '\n':
            s = s + '\n'
        asade = compile(s, '', 'exec')
        todi = marshal.dumps(asade)
        awal = '#Coder By: Rusmana-ID\n#Team: Black Coder Cerush\n#Github: https://github.com/Rusmana-ID\n#Channel Youtube: Tutorial Android-ID\nimport marshal\nexec(marshal.loads('
        akhir = '))'
        open(a[:-3] + '@Rus.py', 'w').write(awal + repr(todi) + akhir)
        time.sleep(1)
    try:
        print(' ')
        print('\x1b[39;1m[\x1b[32;1m√\x1b[39;1m]\x1b[39;1mScript Berhasil Di Encript\x1b[39;1m[\x1b[32;1m√\x1b[39;1m]')
        time.sleep(1.5)
        print('\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1mHASIL\x1b[31;1m:\x1b[36;1m ' + a, '@Rus.py')
        print()
    except ImportError:
        print('\n\x1b[32;1m Anda telah keluar..')
        exit()


def mulai():
    marsha()


mulai()