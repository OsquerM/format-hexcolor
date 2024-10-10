#Variables globales 
hexcolor = 0
def run(intcolor: int) -> str:
    # TODO
    #Variables locales
    global hexcolor
    
    print(f"#{intcolor:06x}")
    return hexcolor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    