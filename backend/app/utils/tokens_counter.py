def estimate_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text string.
    This is a rough estimate, not an exact model token count.
    """
    if not text.strip():
        return 0

    return max(1, len(text.split()))
