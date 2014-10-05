pow =: */@:$~

fact =: */@:>:@:i.

rec_pow =: 1:`([*[$:[:<:])@.(0~:])

rec_fact =: 1:`(* $:@<:)@.*

NB. fibo n = fibo(n - 1) + fibo(n - 2)
rec_fibo =: 1:`(([: $: 2-~])+[: $: 1-~])@.(1<])

NB. fibo n = sum of the last two terms of fibo(n - 1)
rec_fibo2 =: 1:`((2 (] , [: +/ [ {. [: |. ]) ])@:$:@<:)@.(1 < ])
