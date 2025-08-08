def longest_substring(s):
    longest = 0     
    
    current = ("")    

    
    for letter in s:
        
        if letter in current:
            cut_index = current.index(letter) + 1
            current = current[cut_index:]

        current += letter

        if len(current) > longest:
            longest = len(current)

    return longest

if __name__ == "__main__":
     print(longest_substring("ggggg"))
     print(longest_substring("zzfoyi"))
     print(longest_substring("zzzzyyyyzo"))


