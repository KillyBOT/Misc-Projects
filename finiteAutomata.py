testTransitionFunction2 = {"a" : {0 : tuple("abcde"), 1 : tuple("de")},
"b" : {0: "c", 1: "e"},
"c" : {0: None, 1: "b"},
"d" : {0: "e", 1: None},
"e" : {0: None, 1: None}}

class finiteAutomata:

	def __init__(self, states, alphabet, transitionFunction, initState, finalStates):
		self.states = states
		self.alphabet = alphabet
		self.transitionFunction = transitionFunction
		self.initState = initState
		self.finalStates = set(tuple(finalStates))
		#print(self.states,self.alphabet,self.initState,self.finalStates)

	def printTransitionFunction(self):
		print(" \t", end = "")
		for letter in self.alphabet:
			print(letter, end = "\t")

		print("")
		for state in self.states:
			print(state, end="\t")
			for letter in self.alphabet:
				print(self.transitionFunction[state][letter], end = "\t")
			print("")

	def checkPossible(self, string):
		currentStates = [self.initState]
		for letter in string:
			currentState = currentStates.pop()
			if currentState not in self.transitionFunction.keys():
				return False
			currentStates.append(self.transitionFunction[currentState][letter])

		for state in currentStates:
			if state in self.finalStates:
				return True

		return False

def NFAToDFA(NFA):
	newStates = []
	newTransitionFunction = NFA.transitionFunction
	newStates.extend(NFA.states)
	newFinalStates = set()
	newFinalStates = newFinalStates | NFA.finalStates

	for state in newStates:			
		if state not in newTransitionFunction.keys():
			newTransitionFunction[state] = dict()
			for indivState in state:
				if indivState in newFinalStates:
					newFinalStates = newFinalStates | {state}

			for letter in NFA.alphabet:
				toAdd = []

				for indivState in state:
					if newTransitionFunction[indivState][letter] != None and newTransitionFunction[indivState][letter] not in toAdd:

						if type(newTransitionFunction[indivState][letter]) == tuple:
							for elem in newTransitionFunction[indivState][letter]:
								if elem not in toAdd:
									toAdd.append(elem)
						else:
							toAdd.append(newTransitionFunction[indivState][letter])

				toAdd = tuple(toAdd)

				if len(toAdd) == 0:
					newTransitionFunction[state][letter] = None
				elif len(toAdd) == 1:
					newTransitionFunction[state][letter] = toAdd[0]
				else:
					newTransitionFunction[state][letter] = toAdd

		for letter in NFA.alphabet:

			toAdd = newTransitionFunction[state][letter]
			if toAdd not in newStates and toAdd != None:
				newStates.append(toAdd)

	"""print(newStates)
	print(newTransitionFunction)
	print(newFinalStates)"""

	return finiteAutomata(newStates, NFA.alphabet, newTransitionFunction, NFA.initState, newFinalStates)


if __name__ == "__main__":
	testStates = ["a","b","c","d","e"]
	testAlphabet = [0,1]
	testInitState = "a"
	testFinalStates = ["e"]
	testAutomata = finiteAutomata(testStates, testAlphabet, testTransitionFunction2, testInitState, testFinalStates)
	#testAutomata.printTransitionFunction()
	#print(testAutomata.checkPossible([1,0]))
	NFAToDFA(testAutomata).printTransitionFunction()