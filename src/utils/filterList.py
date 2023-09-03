
def filterList(l, keepIfPrefix = None, keepIfSuffix = None, keepIfContains = None, \
	throwIfPrefix = None, throwIfSuffix = None, throwIfContains = None):

	if (keepIfPrefix is not None):
		l = [x for x in l if x.startswith(keepIfPrefix)]

	if (keepIfSuffix is not None):
		l = [x for x in l if x.endswith(keepIfSuffix)]

	if (keepIfContains is not None):
		l = [x for x in l if keepIfContains in x]

	if (throwIfPrefix is not None):
		l = [x for x in l if not x.startswith(throwIfPrefix)]

	if (throwIfSuffix is not None):
		l = [x for x in l if not x.endswith(throwIfSuffix)]

	if (throwIfContains is not None):
		l = [x for x in l if not throwIfContains in x]

	return(l)




