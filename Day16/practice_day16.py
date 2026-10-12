def is_valid_parentheses(text: str) -> bool:
    matching_openers = {")": "(", "]": "[", "}": "{"}
    openers = set(matching_openers.values())
    stack: list[str] = []

    for character in text:
        if character in openers:
            stack.append(character)
        elif character in matching_openers:
            if not stack or stack.pop() != matching_openers[character]:
                return False
        else:
            return False

    return not stack


def reverse_words(text: str) -> str:
    return " ".join(text.split()[::-1])


def validate_required_text(value: str, field_name: str) -> str:
    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is required.")
    return cleaned_value


if __name__ == "__main__":
    assert is_valid_parentheses("()[]{}")
    assert is_valid_parentheses("{[()]}")
    assert not is_valid_parentheses("(]")
    assert not is_valid_parentheses("(((")
    assert not is_valid_parentheses("a()")
    assert reverse_words("CineShelf makes movie nights") == "nights movie makes CineShelf"
    assert reverse_words("  keep   spaces tidy  ") == "tidy spaces keep"
    assert validate_required_text("  Drama  ", "Genre") == "Drama"
    try:
        validate_required_text("   ", "Title")
    except ValueError as error:
        assert str(error) == "Title is required."
    else:
        raise AssertionError("Blank required input should be rejected")
    print("Day 16 validation and coding practice checks passed.")
