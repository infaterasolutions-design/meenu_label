with open('snippets/notify-me-modal.liquid', 'r', encoding='utf-8') as f:
    c_snippet = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    c_index = f.read()

print("9988898845 in snippet:", '9988898845' in c_snippet)
print("9988898845 in index:", '9988898845' in c_index)
print("8511616133 in snippet:", '8511616133' in c_snippet)
print("8511616133 in index:", '8511616133' in c_index)
