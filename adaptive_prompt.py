def get_level_instruction(level):

    if level == "Beginner":
        return """
Explain simply.
Avoid jargon.
Use examples.
Assume the user is new to programming.
"""

    elif level == "Intermediate":
        return """
Explain clearly.
Use standard programming terminology.
Include best practices.
"""

    else:
        return """
Explain at an advanced level.
Include optimizations.
Discuss trade-offs.
Include complexity analysis.
"""