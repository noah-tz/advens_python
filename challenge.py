


# ex1
def task1() -> None: # translate latters by other latters, by table
    string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    old_latters = "abcdefghijklmnopqrstuvwxyz"
    new_latters = "cdefghijklmnopqrstuvwkyzab"
    table = string.maketrans(old_latters, new_latters)
    string = string.translate(table)
    print(string)
def change_string_with_key(string: str) -> str: #this solution less good (of task 1), because latters 'y' & 'z' translated twice
    all_latters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b']
    for index in range(2, len(all_latters)).__reversed__():
        string = string.replace(all_latters[index], all_latters[index + 2])
    return string



def main():
    """
    task1()"""



if __name__ == '__main__':
    main()
