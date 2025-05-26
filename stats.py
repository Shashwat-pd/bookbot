def numOfWords (content):
    return len(content.split())

def countCharacters(content):
    hmap = {}
    for char in content:
        char = char.lower()
        hmap[char] = hmap.get(char, 0) +1

    return hmap

def sortedList(hmap):
    res = []
    for char in hmap.keys():
        if not char.isalpha():
            continue
        res.append({"char":char, "num":hmap[char]})
    res.sort(reverse=True, key=lambda x:x["num"])
    return res
