def readfile(name):
    with open(name, "r", encoding="utf8") as f:
        contents = f.read()
    return contents


def count_paragraphs(text):
  paragraphs = [n for n in text.split("\n\n") if n.strip()]
  return len(paragraphs)