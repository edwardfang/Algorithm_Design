#!/user/bin/env python3
# -*- coding=utf-8 -*-

import sys


def main():
    dim = int(input())
    pref_dalao = list()
    pref_mengxin = list()
    for idx in range(dim):
        ls = list(map(int, input().split()))  # 以列表的形式读入
        pref_dalao.append(ls)

    for idx in range(dim):
        ls = list(map(int, input().split()))  # 以列表的形式读入
        pref_mengxin.append(ls)
    # algorithm begin
    pairs = dict()
    unpaired_dalao = list(range(dim))
    position = [0] * dim
    dl_in_mx_order = list()
    for pref in pref_mengxin:
        dl_order = dict()
        for idx, dl in enumerate(pref):
            dl_order[dl] = idx
        dl_in_mx_order.append(dl_order)

    while unpaired_dalao:
        # print(unpaired_dalao)
        next_dalao = unpaired_dalao[0]
        del unpaired_dalao[0]
        cur_try = position[next_dalao]
        if cur_try < dim:
            cur_try_mengxin = pref_dalao[next_dalao][cur_try]
            if cur_try_mengxin not in pairs.keys():
                pairs[cur_try_mengxin] = next_dalao + 1
            else:
                # print("mengxin:%d\npair:%d\ndalao%d" % (cur_try_mengxin,pairs[cur_try_mengxin], next_dalao+1))
                cur_mx_pref = dl_in_mx_order[cur_try_mengxin-1]
                if cur_mx_pref[next_dalao + 1] < cur_mx_pref[pairs[cur_try_mengxin]]:
                    unpaired_dalao.append(pairs[cur_try_mengxin] - 1)
                    pairs[cur_try_mengxin] = next_dalao + 1
                else:
                    position[next_dalao] += 1
                    unpaired_dalao.append(next_dalao)
        # print(unpaired_dalao, pairs)
    reverse_dict = dict()
    for key, value in pairs.items():
        reverse_dict[value] = key
    out_str = ''
    for idx in range(1, dim + 1):
        out_str += str(reverse_dict[idx]) + ' '
    print(out_str[:-1])
    # print(pairs)


if __name__ == '__main__':
    main()
