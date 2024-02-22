LatinToCyrillic = {'А': 'A',  'Б': 'B',  'В': 'V',  'Г': 'G',  'Д': 'D',  'Е': 'Ye',  'Ё': "YO'",  'Ж': 'J',  'З': 'Z',
                   'И': 'I',  'Й': 'Y',  'К': 'K',  'Л': 'L',  'М': 'M',  'Н': 'N',  'О': 'O',  'П': 'P',  'Р': 'R',
                   'С': 'S',  'Т': 'T',  'У': 'U',  'Ф': 'F',  'Х': 'H',  'Ц': 'Ts',  'Ч': 'Ch',  'Ш': 'Sh',  'Щ': 'Sh',
                  'Э': 'E',  'Ю': 'Yu',  'Я': 'Ya',  ''  'а': 'a',  'б': 'b',  'в': 'v',  'г': 'g',  'д': 'd',
                   'е': 'ye',  'ё': 'yo',  'ж': 'j',  'з': 'z',  'и': 'i',  'й': 'y',  'к': 'k',  'л': 'l',  'м': 'm',
                   'н': 'n',  'о': 'o',  'п': 'p',  'р': 'r',  'с': 's',  'т': 't',  'у': 'u',  'ф': 'f',  'х': 'h',
                     'ч': 'ch',  'ш': 'sh',  'щ': 'sh',  'ы': 'i',  'э': 'e',  'ю': 'yu',  'я': 'ya',
                     'c': 'c',  'Ў': "O'", 'ў': "o'", 'Ў': "Oʻ", 'ў': "oʻ"}
CyrillicToLatin = {a: b for b, a in LatinToCyrillic.items()}


def convert_text(context, pattern):
    result = ''
    mapping = None

    if pattern == 'cyrillic':
        mapping = CyrillicToLatin
        for char in context.replace('Sh', 'Ш').replace('Sh', 'Щ').replace('Ch', 'Ч').replace('sh', 'ш').replace('sh',
                                                                                                                'щ').replace(
                'ch', 'ч').replace('Oʻ', "Ў"):
            if char in mapping:
                result += mapping[char]
            else:
                result += char
    elif pattern == 'latin':
        mapping = LatinToCyrillic
        for char in context.replace('Ш', 'Sh').replace('Щ', 'Sh').replace('Ч', 'Ch').replace('ш', 'sh').replace('щ',
                                                                                                                'sh').replace(
                'ч', 'ch').replace('Ў', "Oʻ").replace('ў', "oʻ"):
            if char in mapping:
                result += mapping[char]
            else:
                result += char
    else:
        return 'Invalid pattern'

    return result

def convert_file(file, pattern):
    if not file.name.endswith('.txt'):
        return f'''Error reading file: " reading file: '''

    context = file.read().decode('utf-8')
    result = convert_text(context, pattern)
    return result