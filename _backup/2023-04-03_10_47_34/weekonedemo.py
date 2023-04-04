# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)



a= "1"+"2"
print(a)

a= 1+2
print(a)

b = 2/1
print(b)
print(type(b))

hello world = 2
print(hello world)

A = 1+1
print(A)

A_@ = 1+ 2
print(A_@)