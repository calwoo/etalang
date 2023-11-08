import os
import pytest

from etalang.lexer import lexer
from etalang.utils import find_column


@pytest.mark.parametrize("source", [
    # "add",
    "arrayinit",
])
def test_lexer(source):
    source_f = os.path.join(os.path.dirname(__file__), f"source/{source}.eta")
    with open(source_f, "r") as f:
        source_s = f.read()

    lexer.input(source_s)

    output_s = ""
    while True:
        tok = lexer.token()
        if not tok:
            break
        output_s += f"{tok.lineno}:{find_column(source_s, tok)} {tok.type} {tok.value}\n"

    print(output_s)

    lexed_f = os.path.join(os.path.dirname(__file__), f"lexed/{source}.lexedsol")
    with open(lexed_f, "r") as f:
        lexed_s = f.read()

    assert output_s == lexed_s
