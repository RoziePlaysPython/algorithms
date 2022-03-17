def max_common_divider(a,b):
    r=a%b
    if r==0:
        return b
    return max_common_divider(b, r)

if __name__=="__main__":
    from sys import argv
    print(max_common_divider(int(argv[1]), int(argv[2])))
