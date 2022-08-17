import cv2
import numpy as np

#bitwise işemi: genel bir görüntünün belli bir kısmının nasıl değiştiğini bize gösterir(iki resmi karşılaştırarak(üst üste bindirerek)).

resim1=cv2.imread(si.jpg)
resim2=cv2.imread(um.jpg)

cv2.imshow("orjinal resim",resim1)

bit_and=cv2.bitwise_and(resim1,resim2)
bit_or=cv2.bitwise_or(resim1,resim2)
bit_xor=cv2.bitwise_xor(resim1,resim2)
bit_not=cv2.bitwise_not(resim1,resim2)


cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not",bit_not)


"""
**bit düzeyinde siyah 0 beyaz 1 olarak tanımlanır.


bitwise işlemi 4 tanedir.
1. AND(&-bitwise_and (birinciresim,ikinciresim) )
2. OR(|-bitwise_or (birinciresim,ikinciresim) )
3. XOR(^-bitwise_xor (birinciresim,ikinciresim))
4. NOT(bitwise_not (birinciresim))
------------------------------------------------------
**And'de her iki resim 1 ise 1 olur, gerisi siyahtır.

1.
bit a	bit b	a & b (a AND b)
0	0	0
0	1	0
1	0	0
1	1	1
------------------------------------------------------
**OR'da iki  resimden biri 1 ise çıktı 1 olur, her iki resim 0 ise siyahtır.

2.
bit a	bit b	a | b (a OR b)
0	0	0
0	1	1
1	0	1
1	1	1
------------------------------------------------------
**XOR'da her ikisi aynı ise siyah olur(0), her ikisi farklı ise beyaz(1) olur.

3.
bit a	bit b	a ^ b (a XOR b)
0	0	0
0	1	1
1	0	1
1	1	0
-------------------------------------------------------
4. 0 olanı 1, 1 olanı 0 yapar.

"""


cv2.waitKey(0)
cv2.destroyAllWindows()
