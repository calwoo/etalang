import os
import pytest

from etalang.lexer import lexer
from etalang.utils import find_column


@pytest.mark.parametrize("source", [
    "add",
    "arrayinit",
    "arrayinit2",
    "beauty",
    "ex1",
    "ex2",
    "gcd",
    "insertionsort",
    "mdarrays",
    "ratadd",
    "ratadduse",
    "spec1",
    "spec2",
    "spec3",
])
def test_lexer(source):
    source_f = os.path.join(os.path.dirname(__file__), f"source/{source}.eta")
    with open(source_f, "r") as f:
        source_s = f.read()

    lexer.lineno = 1   # resets lexer position
    lexer.input(source_s)

    output_s = ""
    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == "ID":
            output_s += f"{tok.lineno}:{find_column(source_s, tok)} id {tok.value}\n"
        elif tok.type == "INTEGER":
            output_s += f"{tok.lineno}:{find_column(source_s, tok)} integer {tok.value}\n"
        elif tok.type == "STRING":
            output_s += f"{tok.lineno}:{find_column(source_s, tok)} string {tok.value}\n"
        elif tok.type == "CHARACTER":
            output_s += f"{tok.lineno}:{find_column(source_s, tok)} character {tok.value}\n"
        elif tok.type == "ERROR":
            output_s += f"{tok.lineno}:{find_column(source_s, tok)} error:{tok.value}\n"
            break
        else:
            output_s += f"{tok.lineno}:{find_column(source_s, tok)} {tok.value}\n"

    print(output_s)

    lexed_f = os.path.join(os.path.dirname(__file__), f"lexed/{source}.lexed")
    with open(lexed_f, "r") as f:
        lexed_s = f.read()

    assert output_s == lexed_s
