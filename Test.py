import Lib_grip as lb
import lib
import colorednoise as cn


data = cn.powerlaw_psd_gaussian(1,1000)


lib.DFA_nolds(data, 16, 9)
scales, fluctuation, alpha = lib.DFA_NONAN(data, range(16,int(len(data)/9)))
print(alpha)