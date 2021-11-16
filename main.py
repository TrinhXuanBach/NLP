import json

link = ["wiki.test.tokens", "wiki.train.tokens", "wiki.valid.tokens"]


def readfile(path: str) -> str:
    with open(path, 'r', encoding="UTF-8") as file:
        data = file.read().replace('\n', ' ')
        data = data.replace('=', '.')
        data = data.replace('<unk>', '')
        return data
    pass


def save_sentences_to_file(raw: str) -> [str]:
    list_sentences = raw.split('.')
    save_sentence_to_file(remove_empty_sentences(list_sentences))


def create_dictionary(raw: str) -> [str]:
    words = raw.split(' ')
    save_dictionary(unique(words))
    return [str]


def unique(words) -> dict:
    dictionary_character: dict = {}
    index = 0
    for word in words:
        if word in dictionary_character:
            continue
        else:
            dictionary_character[word] = index
            index += 1
    dictionary_character[" "] = index
    return dictionary_character


def save_dictionary(dictionary_char: dict):
    with open('data.json', 'w') as fp:
        json.dump(dictionary_char, fp)


def non_blank_sentence(sentence: str) -> bool:
    if len(sentence.replace(' ', '')) == 0:
        return False
    else:
        return True


def remove_empty_sentences(list_sentences: [str]) -> [str]:
    non_blank_sentences = filter(non_blank_sentence, list_sentences)
    return non_blank_sentences


def save_sentence_to_file(list_sentences: [str]):
    with open('train_sentences.txt', 'w', encoding="UTF-8") as f:
        for item in list_sentences:
            f.write("%s\n" % item)
    pass


if __name__ == '__main__':
    raw_data = readfile(path="test_train.tokens")
    sentences = readfile(path="train_sentences.txt")
    dictionary = create_dictionary(sentences)
