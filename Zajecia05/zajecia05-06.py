# =============================================
# M5Z06
import Helper as helper


def main(args):
    while True:
        print("################################################################################\n")
        for i in range(0, 22):
            print("2 do potęgi {:_>3} = {:>8}".format(i, 2**i))
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

# =============================================