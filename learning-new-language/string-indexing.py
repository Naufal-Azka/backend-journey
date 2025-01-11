# indexing ada [start : end : step] 

credit_num = "4768-2932-1357-1024"

# START
print(credit_num[2])
print(credit_num[-2])
print(credit_num[8:])

# END
print(credit_num[:8])
print(credit_num[0:8])

# STEP
print(credit_num[::2])


# EXER
last_digits = credit_num[-4:]
revese = credit_num[::-1]

print(f"XXXX-XXXX-XXXX-{last_digits}")
print(revese)