import sys
from stats import numOfWords, countCharacters, sortedList

def getBookText(path):
    with open(path) as f:
        content = f.read()

    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = getBookText(path)
    numOfWords_ = numOfWords(content)
    charCountDict = countCharacters(content)
    finalList = sortedList(charCountDict)

    generateReport(finalList, numOfWords_, path)

    
def generateReport(finalList, totalWords, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {totalWords} total words")
    print("--------- Character Count -------")
    for item in finalList:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")





main()