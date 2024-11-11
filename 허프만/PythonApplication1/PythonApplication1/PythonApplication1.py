class HuffmanNode:
    def __init__(self, freq, word, left=None, right=None):
        self.freq = freq
        self.word = word
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def heappush(heap, node):
    heap.append(node)
    i = len(heap) - 1
    while i > 1:
        parent_idx = i // 2
        if heap[i].freq >= heap[parent_idx].freq:
            break
        heap[i], heap[parent_idx] = heap[parent_idx], heap[i]
        i = parent_idx

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]
    last = heap.pop()
    if size == 1:
        return root

    heap[1] = last
    i = 1
    while True:
        left = i * 2
        right = i * 2 + 1
        smallest = i
        if left < len(heap) and heap[left].freq < heap[smallest].freq:
            smallest = left
        if right < len(heap) and heap[right].freq < heap[smallest].freq:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return root

def make_tree(frequencies):
    heap = [None]  
    for char, freq in frequencies.items():
        heappush(heap, HuffmanNode(freq, char))
    
    while len(heap) > 2:
        left = heappop(heap)
        right = heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left.word + right.word, left, right)
        heappush(heap, merged)

    return heappop(heap)

def build_codes(node, prefix="", codes={}):
    if node is not None:
        if len(node.word) == 1: 
            codes[node.word] = prefix
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)
    return codes

def huffman(text, frequencies):
    root = make_tree(frequencies)
    codes = build_codes(root)
    encoded_text = "".join(codes[char] for char in text if char in codes)
    return encoded_text, codes

def calculate_compression_ratio(encoded_text, text):
    original_bits = len(text) * 7
    compressed_bits = len(encoded_text)
    compression_ratio = (1 - compressed_bits / original_bits) * 100
    return compression_ratio

def main():
    labels = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
    freqs = [10, 5, 2, 15, 18, 4, 7, 11]
    frequencies = dict(zip(labels, freqs))

    while True:
        text = input("Please a word: ")
        if all(char in frequencies for char in text):
            break
        else:
            print("illegal character")

    encoded_text, codes = huffman(text, frequencies)
    compression_ratio = calculate_compression_ratio(encoded_text, text)

    print("결과 비트 열:", encoded_text)
    print("압축률: {:.2f}%".format(compression_ratio))

if __name__ == "__main__":
    main()
