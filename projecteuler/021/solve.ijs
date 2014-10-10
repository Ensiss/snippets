sdiv =: (([: */ [: ({. +/@:^ i.@:>:@}.)"1 [: |: __ q: ]) - ])
amic =: (sdiv@sdiv = ]) *. (sdiv ~: ])
echo +/ (amic * ]) "0 (2 + i.(1e4 - 2))
exit ''
