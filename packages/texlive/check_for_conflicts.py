#!/usr/bin/python3

with open("collections.txt", "r") as f:
    pkgs = f.read().split("\n")
# print(pkgs)

files = {}
for pkg in pkgs:
    if pkg:
        with open("collection-"+pkg+".txt", "r") as f:
            files[pkg] = f.readlines()

l = len(pkgs)-1
for i in range(0,l):
    for k in range(i+1,l):
        Diff = set(files[pkgs[i]]).intersection(files[pkgs[k]])
        if Diff:
            print("\n"+pkgs[i]+" "+pkgs[k])
            print(Diff)