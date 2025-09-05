def chunk_text(text, max_chars=3000):
    start = 0
    n = len(text)
    while start < n:
        end = min(start + max_chars, n)
        yield text[start:end]
        start = end
