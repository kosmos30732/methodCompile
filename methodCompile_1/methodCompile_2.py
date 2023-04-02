
alt = {
    "A1": "!B!",
    "B1": "B`",
    "B`1": "T",
    "B`2": "B`+T",
    "T1": "T`",
    "T`1": "M",
    "T`2": "T`*M",
    "M1": "a",
    "M2": "b",
    "M3": "(B)",
}
L = {}
R = {}
for x in alt.keys():
    st = x[: len(x) - 1]
    L[st] = []
    R[st] = []
for x in L.keys():
    tmp = x + "1"
    while alt.get(tmp) != None:
        val = alt.get(tmp)
        l_tmp = L.get(x)
        if len(val) > 1:
            if val[1] == "`":
                if (val[0] + val[1]) in l_tmp:
                    pass
                else:
                    l_tmp.append(val[0] + val[1])
            else:
                if (val[0]) in l_tmp:
                    pass
                else:
                    l_tmp.append(val[0])
        else:
            if (val[0]) in l_tmp:
                pass
            else:
                l_tmp.append(val[0])
        L[x] = l_tmp
        r_tmp = R.get(x)
        if val[len(val) - 1] == "`":
            if (val[len(val) - 2] + val[len(val) - 1]) in r_tmp:
                pass
            else:
                r_tmp.append(val[len(val) - 2] + val[len(val) - 1])
        else:
            if (val[len(val) - 1]) in r_tmp:
                pass
            else:
                r_tmp.append(val[len(val) - 1])
        R[x] = r_tmp
        tmp = tmp[: len(tmp) - 1] + chr(ord(tmp[len(tmp) - 1]) + 1)
l_keys = list(L.keys())
for i in range(1, len(l_keys) - 1):
    append_l = L.get(l_keys[i])
    for j in range(i + 1, len(l_keys)):
        tmp_l = L.get(l_keys[j])
        for x in tmp_l:
            if x in append_l:
                pass
            else:
                append_l.append(x)
    L[l_keys[i]] = append_l
r_keys = list(R.keys())
for i in range(1, len(r_keys) - 1):
    append_r = R.get(r_keys[i])
    for j in range(i + 1, len(r_keys)):
        tmp_r = R.get(r_keys[j])
        for x in tmp_r:
            if x in append_r:
                pass
            else:
                append_r.append(x)
    R[r_keys[i]] = append_r
mp_idx = []
for x in alt.keys():
    tmp = alt.get(x)
    tmp_list = []
    for y in tmp:
        if y != "`":
            tmp_list.append(str(y))
        else:
            tmp_list[len(tmp_list) - 1] = tmp_list[len(tmp_list) - 1] + "`"
    for y in tmp_list:
        if y in mp_idx:
            pass
        else:
            mp_idx.append(y)
mp = []
for i in mp_idx:
    mp_str = []
    for j in mp_idx:
        mp_str.append("")
    mp.append(mp_str)
for x in alt.keys():
    tmp = alt.get(x)
    tmp_list = []
    for y in tmp:
        if y != "`":
            tmp_list.append(str(y))
        else:
            tmp_list[len(tmp_list) - 1] = tmp_list[len(tmp_list) - 1] + "`"
    if len(tmp_list) > 1:
        for i in range(0, len(tmp_list) - 1):
            v = mp_idx.index(tmp_list[i])
            g = mp_idx.index(tmp_list[i + 1])
            mp[v][g] = "=."
T = ["!", "(", "*", "+", ")"]
NT = ["B", "B`", "T", "T`", "M"]
for x in alt.keys():
    tmp = alt.get(x)
    tmp_list = []
    for y in tmp:
        if y != "`":
            tmp_list.append(str(y))
        else:
            tmp_list[len(tmp_list) - 1] = tmp_list[len(tmp_list) - 1] + "`"
    if len(tmp_list) > 1:
        for i in range(0, len(tmp_list) - 1):
            if (tmp_list[i] in T) and (tmp_list[i + 1] in NT):
                v = mp_idx.index(tmp_list[i])
                tmp_l = L.get(tmp_list[i + 1])
                for j in tmp_l:
                    g = mp_idx.index(j)
                    mp[v][g] = "<."
for x in alt.keys():
    tmp = alt.get(x)
    tmp_list = []
    for y in tmp:
        if y != "`":
            tmp_list.append(str(y))
        else:
            tmp_list[len(tmp_list) - 1] = tmp_list[len(tmp_list) - 1] + "`"
    if len(tmp_list) > 1:
        for i in range(0, len(tmp_list) - 1):
            if (tmp_list[i] in NT) and (tmp_list[i + 1] in T):
                g = mp_idx.index(tmp_list[i + 1])
                tmp_r = R.get(tmp_list[i])
                for j in tmp_r:
                    v = mp_idx.index(j)
                    mp[v][g] = ".>"
in_str = str(input("Enter string ="))
print("L=")
for x in L:
    print(x, "\t", L.get(x))
print("\nR=")
for x in R:
    print(x, "\t", R.get(x))
res = ""
for x in mp_idx:
    res += "\t" + x
print(res)
for x in range(len(mp_idx)):
    res = ""
    for y in mp[x]:
        res += y + "\t"
    print(mp_idx[x], "\t", res)
idx_alt = {
    "A1": "1",
    "B1": "2",
    "B`1": "3",
    "B`2": "4",
    "T1": "5",
    "T`1": "6",
    "T`2": "7",
    "M1": "8",
    "M2": "9",
    "M3": "10",
}
res = ""
stack1 = []
stack1.append(in_str[0])
in_str = in_str[1:]
while stack1[0] != "A":
    if len(in_str) == 0:
        svertka = []
        svertka = [stack1.pop()] + svertka
        while (
            len(stack1) > 0
            and mp[mp_idx.index(stack1[len(stack1) - 1])][mp_idx.index(svertka[0])]
            != "<."
        ):
            svertka = [stack1.pop()] + svertka
        st_svertka = ""
        for x in svertka:
            st_svertka += x
        flag = True
        for x in alt.keys():
            if alt.get(x) == st_svertka:
                res += idx_alt.get(x) + " "
                flag = False
                stack1.append(x[: len(x) - 1])
                break
        if flag:
            res = "Can't represent this string"
            break
        continue

    if (mp[mp_idx.index(stack1[len(stack1) - 1])][mp_idx.index(in_str[0])] == "<.") or (
        mp[mp_idx.index(stack1[len(stack1) - 1])][mp_idx.index(in_str[0])] == "=."
    ):
        stack1.append(in_str[0])
        in_str = in_str[1:]
        continue
    if mp[mp_idx.index(stack1[len(stack1) - 1])][mp_idx.index(in_str[0])] == ".>":
        svertka = []
        svertka = [stack1.pop()] + svertka
        while (
            len(stack1) > 0
            and mp[mp_idx.index(stack1[len(stack1) - 1])][mp_idx.index(svertka[0])]
            != "<."
        ):
            svertka = [stack1.pop()] + svertka
        st_svertka = ""
        for x in svertka:
            st_svertka += x
        flag = True
        for x in alt.keys():
            if alt.get(x) == st_svertka:
                res += idx_alt.get(x) + " "
                flag = False
                stack1.append(x[: len(x) - 1])
                break
        if flag:
            res = "Can't represent this string"
            break
        continue
    res = "Can't represent this string"
    break
print(res)