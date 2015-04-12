alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(instring, shift):
	cipher = []
	for i in instring.lower():
		if i not in alphabet:
			cipher.append(i)
		else:
			cipher.append(alphabet[(alphabet.index(i) + shift) % len(alphabet)])
	return ''.join(cipher)	 
def caesar_decipher(instring, shift):
	deciphered = []
	for i in instring.lower():
		if i not in alphabet:
			deciphered.append(i)
		else:
			deciphered.append(alphabet[(alphabet.index(i) - shift) % len(alphabet)])
	return ''.join(deciphered)
