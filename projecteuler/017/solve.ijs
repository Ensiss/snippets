d1to9 =: 'one','two','three','four','five','six','seven','eight','nine'
d10to19 =: 'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'
d20to90 =: 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'
d100 =: 'hundred'
d1000 =: 'thousand'

c1to99 =: (#d1to9) + (#d10to19) + (10 * #d20to90) + (8 * #d1to9)
c1to999 =: (900 * #d100) + (100 * #d1to9) + (9 * 99 * 3) + (10 * c1to99)
c1000 =: c1to999 + ((#'one') + #d1000)
echo c1000
exit ''
