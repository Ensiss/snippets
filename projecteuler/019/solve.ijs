div =: (=<.)@%~
leap =: 400&div +. (4&div *. 100&(-.@div))
echo +/0=7| 2&+ }: ~. +/\ , (0, 31 , 31 30 31 30 31 31 30 31 30 31 ,~ 28 + leap) "0 (1901&+ i.100)
exit ''
