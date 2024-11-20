try:
    print("start code")
    print(10 / 0)
    print("no errors")
except NameError:
    print("we have no an error")
except ZeroDivisionError:
    print("we have an ZeroDivisionError")

print("code after capsule")

try:
    print("start code")
    print(10 / 0)
    print("no errors")
except (NameError, ZeroDivisionError) as error:
    print("We have", error )

print("code after capsule")

try:
    try:
        print("start code")
        print(error)
        print("No errors")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)

try:
    print("Hello")
    # print(error)
    print("No error")
except NameError as error:
    print(error)
else:
    print("No problems")
finally:
    print("Finally code")
