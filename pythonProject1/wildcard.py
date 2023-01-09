import fnmatch
ls={"this","thus","just","hello"}
filtered=fnmatch.filter(ls,'th*s')
filtered1=fnmatch.filter(ls,'th?s')
print(filtered)
print(filtered1)