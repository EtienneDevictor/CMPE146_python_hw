def swap_last_item(inList):
	outList = []
	outList.extend(inList)
	temp = outList[0]
	outList[0] = outList[len(outList) - 1]
	outList[len(outList) - 1] = temp
	return outList

