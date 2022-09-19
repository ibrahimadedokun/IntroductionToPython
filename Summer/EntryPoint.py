import Summer as _summer
import Subtracter as _subtracter
import Multiplier as _mul
import Divider as _div

s = _summer.CustomAdder(3, -3, 100, 1)
s.invoke()

sub = _subtracter.CustomSubtracter()
sub.invoke()

d = _div.CustomDivider()
d.invoke()

m = _mul.CustomMultiplier()
m.invoke()