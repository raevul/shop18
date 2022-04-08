# class iter_int(int):
#     def __iter__(self):
#         num = self.real
#         for i in str(num):
#             yield int(i)

# num = iter_int(12345)
# for i in num:
#     print(i)
# for  i in iter_int(12345):
#     print(i)
# a = iter(num)
# print(next(a))
