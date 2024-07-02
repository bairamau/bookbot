def main():
    def get_text(path):
        with open(path) as f:
            return f.read()
    
    def get_words_count(text):
        return len(text.split())

    def count_different_characters(text):
        lowercase = text.lower()
        characters = {}
        for ch in lowercase:
            if ch in characters:
                characters[ch] += 1
            else: characters[ch] = 1
        return characters
    
    def print_report(path):
        words = get_text(path)
        count = get_words_count(words)
        characters = count_different_characters(words)
        print(f"--- Begin report of {path} ---")
        print(f"{count} words found in the document\n")
        alpha = []
        for ch in characters:
            if ch.isalpha():
                alpha.append((ch, characters[ch]))
        alpha.sort(reverse=True,key= lambda x: x[1])
        for (ch, count) in alpha:
            print(f"The '{ch}' character was found {count} times")
        print(f"--- End report ---")

    print_report("books/frankenstein.txt")
main()
