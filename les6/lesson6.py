# a = 5
# b = 0
#
# try:
#     result = a / b
# except ZeroDivisionError:
#     print("ZDE")
# except (KeyError, IndexError):
#     print('KeyE')
# finally:
#     print("FIN")


def some(a, b, c):
    h = []
    result = None
    try:
        if c:
            result = a / b
        else:
            result = h[a]
        return result
    except ZeroDivisionError:
        print("ZDE")
    except (KeyError, IndexError):
        print('KeyE')
    finally:
        return 234
    return result


a = some(1, 2, 1)
print(a)


def nums(number):
    result = []
    a, b = number // 10, number % 10
    pre_result = nums(a) if a else []
    result.extend(pre_result)
    result.append(b)
    return result


numbers = 1234567890

some_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, 10]]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def flat_list(iter_object):
    result = []
    for itm in iter_object:
        if isinstance(itm, list):
            result.extend(flat_list(itm))
        else:
            result.append(itm)
    return result


print(flat_list(some_list))


def fibo_gen(stop):
    print("GENERATOR SPAWN")
    memo = [0, 1]
    for idx in range(stop):
        print("GENERATOR ITER")
        result = sum(memo)
        print("YELD RUN")
        yield result
        memo.pop(0)
        memo.append(result)
        print("CYCLE CONTINUE")
    print("GENERATOR END")
    return None


# def demo_gen(n):
#     yield n ** 2
#     yield n ** 3
#     yield n ** 4
#     yield n ** 5
#
#
# for i, n in enumerate(demo_gen(3), 2):
#     print(f"{i}: {n}")
#
# # some = fibo_gen(15)
# print(type(fibo_gen(15)))
#
# def abs_for(in_obj):
#     pass
#
# for n in fibo_gen(15):
#     print(f"yield send {n}")
# print("*" * 10)
# some = fibo_gen(15)
# print("*" * 10)
# print("#" * 10)
# while True:
#     try:
#         n = next(some)
#     except StopIteration:
#         break
#     print(f"yield send {n}")

def some_zip(*args):
    idx = 0
    while args:
        result = []
        for itm in args:
            try:
                result.append(itm[idx])
            except IndexError:
                return None
        yield tuple(result)
        idx += 1


a = [1, 2, 3, 4]
b = [6, 5, 4, 3]
c = [98058, 47, 4, 9, 7, 4, 3, 6]

h = (a, b, c)

for itm in some_zip(*h):
    print(itm)