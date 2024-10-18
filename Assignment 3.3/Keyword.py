import re
import os

# Change the working directory to the folder containing your text files
# For example:
# os.chdir(r"C:\Users\Musrat\Semester 2,2024\Algorithms\Assignment_3.3")

def build_frequency_table(doc_files, keywords):
    frequency_table = {keyword: 0 for keyword in keywords}

    for doc_file in doc_files:
        try:
            with open(doc_file, 'r') as file:
                content = file.read().lower()
                words = re.findall(r'\b\w+\b', content)
                for word in words:
                    if word in frequency_table:
                        frequency_table[word] += 1
        except FileNotFoundError:
            print(f"Error: {doc_file} not found.")

    return frequency_table

def main():
    # Print current working directory for debugging
    print("Current Working Directory:", os.getcwd())
    documents = ['doc1.txt', 'doc2.txt']
    keywords = ['keyword1', 'keyword2', 'keyword3']
    frequency_counts = build_frequency_table(documents, keywords)
    
    print("Keyword Frequency Counts:")
    for keyword, count in frequency_counts.items():
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    main()
