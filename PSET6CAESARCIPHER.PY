def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    dict = {}
    U = string.ascii_uppercase
    L = string.ascii_lowercase
    for x in range(0,len(U)):
        dict[L[x]] = L[(x + shift)%len(L)]
        dict[U[x]] = U[(x + shift)%len(U)]
    return dict
        
def applyCoder(text, coder):
	result = ''
	for x in text:
		if x in coder.keys():
			result += coder[x]
		else:
			result += x
	return result
	
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.
    coder=buildCoder(shift)
    return applyCoder(text,coder)
    
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    max = 0
    best = 0
    for shift in range(0,26):
        valid = 0
        shifted = applyShift(text, shift)
        words = shifted.split()

        for x in words:
            if isWord(wordList, x):
                valid += 1
        if valid > max:
            max = valid
            best = shift
            
  def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    List = loadWords()
    text = getStoryString()
    shift = findBestShift(List, text)
    return applyShift(text, shift)
    return best
