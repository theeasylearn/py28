def SayHello(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello Mr/Miss/M.R.S.",name)
    return

SayHello("Ram","ramesh","meena","haresh")
