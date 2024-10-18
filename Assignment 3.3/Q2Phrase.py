import os
import re
from collections import defaultdict

class TrieNode:
  
    def __init__(self):
        self.children = defaultdict(TrieNode)  
        self.is_end_of_phrase = False  
        self.documents = set() 

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase, doc_id):
       
        node = self.root
        for word in phrase:
            node = node.children[word] 
        node.is_end_of_phrase = True 
        node.documents.add(doc_id) 

    def get_common_phrases(self, phrase_length):

        common_phrases = []
        self._search_common_phrases(self.root, [], common_phrases, phrase_length)
        return common_phrases

    def _search_common_phrases(self, node, current_phrase, common_phrases, phrase_length):

        if node.is_end_of_phrase and len(current_phrase) == phrase_length and len(node.documents) > 1:
            common_phrases.append((" ".join(current_phrase), len(node.documents)))  

        # Recursively traverse the children nodes
        for word, child_node in node.children.items():
            self._search_common_phrases(child_node, current_phrase + [word], common_phrases, phrase_length)


def extract_phrases(document, phrase_length):

    phrases = []
    # Extract words using regex and convert to lowercase for case insensitivity
    words = re.findall(r'\b\w+\b', document.lower())
    
    # Ensure that there are enough words to form at least one phrase
    if len(words) < phrase_length:
        return phrases
    
    # Create tuples of consecutive words to form phrases
    for i in range(len(words) - phrase_length + 1):
        phrases.append(tuple(words[i:i + phrase_length]))
    
    return phrases


def main():
    print("Current Working Directory:", os.getcwd())
    documents = ['doc1.txt', 'doc2.txt']  # List of document filenames to process
    phrase_length = 3  # Length of phrases to detect (3-word phrases)

    trie = Trie()  # Initialize the Trie

    # Insert phrases from each document into the Trie
    for doc_id, doc_file in enumerate(documents):
        try:
            with open(doc_file, 'r') as file:
                content = file.read()
                phrases = extract_phrases(content, phrase_length)
                
                # Handle edge case where document doesn't contain enough words for a phrase
                if not phrases:
                    print(f"Warning: {doc_file} contains fewer than {phrase_length} words, skipping.")
                    continue
                
                for phrase in phrases:
                    trie.insert(phrase, doc_id) 
        except FileNotFoundError:
            print(f"Error: {doc_file} not found.")
        except Exception as e:
            print(f"Error processing {doc_file}: {e}")

    # Get common phrases that appear in more than one document
    common_phrases = trie.get_common_phrases(phrase_length)

    print("Common Phrases (appearing in more than one document):")
    if common_phrases:
        # Sort phrases alphabetically before printing
        common_phrases.sort()
        for idx, (phrase, count) in enumerate(common_phrases, start=1):
            print(f"{idx}. {phrase} (Appears in {count} documents)")
    else:
        print("No common phrases found.")


if __name__ == "__main__":
    main()
