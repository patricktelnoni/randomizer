import xlrd, random, sys, math

workbook        = xlrd.open_workbook("namakelompok.xlsx")
worksheet       = workbook.sheet_by_name(sys.argv[1])
jumlahanggota   = sys.argv[2]
acessed         = []
counterkelompok = 1
anggotakelompok = 0

def randomize():
    pick = random.randint(0, worksheet.nrows-1)
    if pick in acessed :
         randomize()
    else:
        acessed.append(pick)

for i in range(worksheet.nrows):
    randomize()
    if counterkelompok == 1 and anggotakelompok <1:
        print "KELOMPOK", counterkelompok

    print worksheet.cell(acessed[i], 0).value
    if(anggotakelompok < int(jumlahanggota)-1):
        anggotakelompok = anggotakelompok+1
    else:
        print "\n"
        anggotakelompok = 0
        counterkelompok = counterkelompok+1
        if counterkelompok == math.ceil(float(worksheet.nrows)/float(jumlahanggota))+1:
            break
        else:
            print "KELOMPOK", counterkelompok
