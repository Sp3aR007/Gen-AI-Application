
prompt_template = """
    You are an expert at creating questions based on given materials and documentation.
    Your goal is to prepare a questions for their exam or tests
    You do this by asking questions about the text below:

    ------------
    {text}
    ------------

    Create questions that will prepare them for their tests.
    Make sure not to lose any important information.

    QUESTIONS:
    """


refine_template = ("""
    You are an expert at creating practice questions based on  material and documentation.
    Your goal is to help them prepare for their exam or test.
    We have received some practice questions to a certain extent: {existing_answer}.
    We have the option to refine the existing questions or add new ones.
    (only if necessary) with some more context below.
    ------------
    {text}
    ------------

    Given the new context, refine the original questions in English.
    If the context is not helpful, please provide the original questions.
    QUESTIONS:
    """
    )