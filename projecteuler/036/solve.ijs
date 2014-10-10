NB. return a string containing its parameter in binary representation
b2 =: ":`($:@(2<.@%~]) , ":@(2&|))@.(1&<)
NB. check if a given number is a palindrome
palin =: ] = ".@:|.@:":
echo +/ (] * palin *. palin@(". (b2 , 'x'"_))) "0 i.1e6
exit ''
