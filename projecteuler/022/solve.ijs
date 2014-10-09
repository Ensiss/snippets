sorted =: /:~ ',' cut (#~ '"'&~:) fread 'names.txt'
n =: ([: +/ (a.i.'@') -~ a.&i.) &.> sorted

echo +/ (>:@:i.@# * ]) >n
exit ''
