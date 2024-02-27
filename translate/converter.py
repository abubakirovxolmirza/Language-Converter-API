import re

CyrillicToLatin = {'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'Ye': 'Е', "YO'": 'Ё', 'J': 'Ж', 'Z': 'З',
                   'I': 'И', 'Y': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'R': 'Р', 'S': 'С',
                   'T': 'Т', 'U': 'У', 'F': 'Ф', 'X': 'Х', 'Ts': 'Ц', 'Ch': 'Ч', 'Sh': 'Щ', 'E': 'Э', 'Yu': 'Ю',
                   'Ya': 'Я', 'G‘': 'Ғ', 'Q': 'Қ', 'H': 'Ҳ', 'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е',
                   'yo': 'ё', 'j': 'ж','z': 'з', 'i': 'и', 'y': 'й', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
                   'r': 'р', 'k': 'к', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'x': 'х', 'ch': 'ч', 'sh': 'ш',
                   'yu': 'ю', 'ya': 'я', 'c': 'c', 'Oʻ': 'Ў', 'oʻ': 'ў', 'q': 'қ', 'g‘': 'ғ', 'h': 'ҳ', "'": 'ъ'
                   }

LatinToCyrillic = {a: b for b, a in CyrillicToLatin.items()}


def convert_text(context, pattern):
    """
    Bu funksiya matnni cyril yoki latinga o'giradi.
    Pasdagi binary_pattern va single_pattern tushunarsiz bo'lishi mumkin shuning uchun tushuntirib beraman.
    binary_pattern: Vazifasi keylarni filtrlaydi, faqat uzunligi 1 dan katta bo'lganlarni (ya'ni, ko'p bitli
                    ikkilik satrlarni) saqlaydi.
                    Misol uchun: Ko'p kiril belgilar bitta latin harfga teng ya'ni 1ta uzunlikdagi 'B' = 'Б', lekin ba'zi
                                 belgilar 2ta uzunlikdagi harflarga teng 'Ш': 'Sh', 'Ч': 'Ch'

    single_pattern:
        binary_patternga o'xshash ish qiladi lekin 1 uzunlikdagi keylarni filtirlaydi

    combined_pattern: birlashtirish vazifasini bajaradi.
    """

    result = ''
    mapping = None

    if pattern == 'cyrillic':
        mapping = CyrillicToLatin
    elif pattern == 'latin':
        mapping = LatinToCyrillic
    else:
        return 'Invalid pattern'

    binary_pattern = '|'.join(re.escape(binary) for binary in mapping.keys() if len(binary) > 1)
    single_pattern = '|'.join(re.escape(single) for single in mapping.keys() if len(single) == 1)

    combined_pattern = f'{binary_pattern}|{single_pattern}'

    def replace(match):
        key = match.group(0)
        if key in mapping:
            return mapping[key]
        else:
            return key

    result = re.sub(combined_pattern, replace, context)

    return result


def convert_file(file, pattern):
    if not file.name.endswith('.txt'):
        return 'Error: File format must be .txt'

    context = file.read().decode('utf-8')
    result = convert_text(context, pattern)
    return result
