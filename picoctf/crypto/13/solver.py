def rot13(string):
    result = ""
    for i in string:
        if i.islower():
            result += chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
        elif i.isupper():
            result += chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += i
    return result

string = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
string2 = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
decrypt = rot13(string2)
print(decrypt)
