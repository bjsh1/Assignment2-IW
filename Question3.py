#3. Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.



def anagrams(sample_input):
    
    split_word = sample_input.split(' ')
    result = []
    for i in split_word:
        for j in split_word:
            if i != j:
                if sorted(i) == sorted(j):
                    if i not in result:
                        result.append(i)
                    if j not in result:
                        result.append(j)

    if result:
        return result
    else:
        return "No Anagrams Word"


if __name__ == "__main__":
    sample_sentence = "den end act tac hello papa"
    result = anagrams(sample_sentence)
    print(result)