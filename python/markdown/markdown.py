import re


def parse(markdown: str) -> str:
    html = h_tag(markdown)
    html = ul_tag(html)
    html = p_tag(html)
    html = strong_tag(html)
    html = em_tag(html)
    html = remove_new_lines(html)
    return html


def h_tag(input_: str) -> str:
    output = input_

    for i in range(6, 0, -1):
        output = re.sub(
            r"^{0} (.*?)$".format("#" * i),
            r"<h{0}>\1</h{0}>".format(i),
            output,
            flags=re.M,
        )

    return output


def ul_tag(input_: str) -> str:
    output = re.sub(r"^\* (.*?)$", r"<li>\1</li>", input_, flags=re.M)
    return re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", output, flags=re.S)


def p_tag(input_: str) -> str:
    return re.sub(r"^(?!<[hul])(.*?)$", r"<p>\1</p>", input_, flags=re.M)


def strong_tag(input_: str) -> str:
    return re.sub(r"__([^\n]*?)__", r"<strong>\1</strong>", input_)


def em_tag(input_: str) -> str:
    return re.sub(r"_([^\n]*?)_", r"<em>\1</em>", input_)


def remove_new_lines(input_: str) -> str:
    return re.sub(r"\n", "", input_)
