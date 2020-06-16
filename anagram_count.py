def fill_freq(s):
    freq=[0]*26
    for i in s: 
        freq[ord(i)-ord('a')]+=1
    return freq

def compare_freq(a,b):
    if a==b: 
        return True
    return False

def solve(arr, word):
    arr=arr.lower()
    word=word.lower()
    word_freq=fill_freq(word)
    arr_freq=fill_freq(arr[0:len(word)])

    count=0
    if arr_freq==word_freq:
        count+=1
    front=0
    end=len(word)

    while(end<len(arr)):
        if compare_freq(arr_freq, word_freq):
            count+=1
        arr_freq[ord(arr[end])-ord('a')]+=1
        arr_freq[ord(arr[front])-ord('a')]-=1
        end+=1
        front+=1
    return count

arr=input()
word=input()
print(solve(arr,word))
