import xdrlib
from random import choice
# def xdr_packer():
#     p = xdrlib.Packer()
#     p.pack_list([1, 2, 3], p.pack_int)
#     print(p)
#
# def xdr_exception():
#     p = xdrlib.Packer()
#     try:
#         p.pack_double(8.01)
#     except xdrlib.ConversionError as instance:
#         print('packing the double failed:', instance.msg)

# def get_num():
#     num_total_set = set()
#     while(1):
#         num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
#         # num_set = set(num_list)
#         num1_list = [choice(num_list) for _ in range(3)]
#         for del_num1 in num1_list:
#             num_list.remove(del_num1)
#         num1 = int(''.join(num1_list))
#         # num1_set = set(num1_list)
#         # num2_choice_set = num_set - num1_set
#         num2_list = [choice(num_list) for _ in range(3)]
#         # num2_set = set(num2_list)
#         num2 = int(''.join(num2_list))
#         for del_num2 in num2_list:
#             num_list.remove(del_num2)
#         num3_list = [choice(num_list) for _ in range(4)]
#         num3 = int(''.join(num3_list))
#         num_total_set.add((num1, num2, num3))
#         if (num1, num2, num3) in num_total_set:
#             continue
#         if num1 + num2 == num3:
#             print(num1 + '+' + num2 + '=' + num3)
#             break

def get_num2():
    import itertools
    data = []
    for i in itertools.permutations('1234567890', 10):
        if i[0] != '0':
            data.append("".join(i))
    print(len(data))

if __name__ == "__main__":
    get_num2()