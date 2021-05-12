#enumerate always returns iterable object (list/tuple)

routine=["eat","sleep","code","repeat"]

programmer_life=list(enumerate(routine))

print(programmer_life)


routine=["eat","sleep","code","repeat"]

programmer_life=list(enumerate(routine,start=1))

print(programmer_life)