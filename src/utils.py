from comment_formats import comment_formats


def format_comment(language: str, content: str) -> str:
    frmt = comment_formats.get(language)

    if not frmt:
        raise ValueError("Language not supported")

    return frmt.format(comment=content)
