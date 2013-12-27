
def main():
    i=0
    string=""
    while i<1000000:
        string=string+str(i)
        i=i+1
    print eval(string[1])*eval(string[10])*eval(string[100])*eval(string[1000])*eval(string[10000])*eval(string[100000])*eval(string[1000000])

main()
