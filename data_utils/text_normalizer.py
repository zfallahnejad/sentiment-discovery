normalization_map = {
    u'\u0622': u'\u0627', u'\u0627': u'\u0627', u'\u0671': u'\u0627', u'\u0672': u'\u0627', u'\u0673': u'\u0627',
    u'\u0675': u'\u0627', u'\ufb50': u'\u0627', u'\ufb51': u'\u0627', u'\ufe81': u'\u0627', u'\ufe8d': u'\u0627',
    u'\u0628': u'\u0628', u'\ufb52': u'\u0628', u'\ufb53': u'\u0628', u'\ufb54': u'\u0628', u'\ufb55': u'\u0628',
    u'\ufe8f': u'\u0628', u'\ufe90': u'\u0628', u'\ufe91': u'\u0628', u'\ufe92': u'\u0628',
    u'\ufb5a': u'\u0628', u'\ufb5b': u'\u0628', u'\ufb5c': u'\u0628', u'\ufb5d': u'\u0628',
    u'\u067e': u'\u067e', u'\ufb58': u'\u067e', u'\ufb59': u'\u067e',
    u'\ufb56': u'\u067e', u'\ufb57': u'\u067e',
    u'\u0629': u'\u062a', u'\u062a': u'\u062a', u'\ufe93': u'\u062a', u'\ufe94': u'\u062a', u'\ufe95': u'\u062a',
    u'\ufe96': u'\u062a', u'\ufe97': u'\u062a', u'\ufe98': u'\u062a',
    u'\u062b': u'\u062b', u'\ufe99': u'\u062b', u'\ufe9a': u'\u062b', u'\ufe9b': u'\u062b', u'\ufe9c': u'\u062b',
    u'\u062c': u'\u062c', u'\ufe9d': u'\u062c', u'\ufe9e': u'\u062c', u'\ufe9f': u'\u062c', u'\ufea0': u'\u062c',
    u'\u0686': u'\u0686', u'\ufb7a': u'\u0686', u'\ufb7b': u'\u0686', u'\ufb7c': u'\u0686', u'\ufb7d': u'\u0686',
    u'\u062d': u'\u062d', u'\ufea1': u'\u062d', u'\ufea2': u'\u062d', u'\ufea3': u'\u062d', u'\ufea4': u'\u062d',
    u'\u062e': u'\u062e', u'\ufea5': u'\u062e', u'\ufea6': u'\u062e', u'\ufea7': u'\u062e', u'\ufea8': u'\u062e',
    u'\u062f': u'\u062f', u'\ufea9': u'\u062f', u'\ufeaa': u'\u062f',
    u'\u0630': u'\u0630', u'\ufeab': u'\u0630', u'\ufeac': u'\u0630',
    u'\u0631': u'\u0631', u'\ufead': u'\u0631', u'\ufeae': u'\u0631',
    u'\u0632': u'\u0632', u'\ufeaf': u'\u0632', u'\ufeb0': u'\u0632',
    u'\u0698': u'\u0698', u'\ufb8a': u'\u0698', u'\ufb8b': u'\u0698',
    u'\u0633': u'\u0633', u'\ufeb1': u'\u0633', u'\ufeb2': u'\u0633', u'\ufeb3': u'\u0633', u'\ufeb4': u'\u0633',
    u'\u0634': u'\u0634', u'\ufeb5': u'\u0634', u'\ufeb6': u'\u0634', u'\ufeb7': u'\u0634', u'\ufeb8': u'\u0634',
    u'\u0635': u'\u0635', u'\ufeb9': u'\u0635', u'\ufeba': u'\u0635', u'\ufebb': u'\u0635', u'\ufebc': u'\u0635',
    u'\u0636': u'\u0636', u'\ufebd': u'\u0636', u'\ufebe': u'\u0636', u'\ufebf': u'\u0636', u'\ufec0': u'\u0636',
    u'\u0637': u'\u0637', u'\ufec1': u'\u0637', u'\ufec2': u'\u0637', u'\ufec3': u'\u0637', u'\ufec4': u'\u0637',
    u'\u0638': u'\u0638', u'\ufec5': u'\u0638', u'\ufec6': u'\u0638', u'\ufec7': u'\u0638', u'\ufec8': u'\u0638',
    u'\u0639': u'\u0639', u'\ufec9': u'\u0639', u'\ufeca': u'\u0639', u'\ufecb': u'\u0639', u'\ufecc': u'\u0639',
    u'\u063a': u'\u063a', u'\ufecd': u'\u063a', u'\ufece': u'\u063a', u'\ufecf': u'\u063a', u'\ufed0': u'\u063a',
    u'\u0641': u'\u0641', u'\ufed1': u'\u0641', u'\ufed2': u'\u0641', u'\ufed3': u'\u0641', u'\ufed4': u'\u0641',
    u'\u0642': u'\u0642', u'\ufed5': u'\u0642', u'\ufed6': u'\u0642', u'\ufed7': u'\u0642', u'\ufed8': u'\u0642',
    u'\u0643': u'\u06a9', u'\ufed9': u'\u06a9', u'\ufeda': u'\u06a9', u'\ufedb': u'\u06a9', u'\ufedc': u'\u06a9',
    u'\ufb8f': u'\u06a9', u'\ufb90': u'\u06a9', u'\ufb91': u'\u06a9',
    u'\u06a9': u'\u06a9', u'\u06aa': u'\u06a9', u'\ufb8e': u'\u06a9',
    u'\u06af': u'\u06af', u'\ufb93': u'\u06af', u'\ufb94': u'\u06af', u'\ufb95': u'\u06af',
    u'\u0644': u'\u0644', u'\ufedd': u'\u0644', u'\ufede': u'\u0644', u'\ufedf': u'\u0644', u'\ufee0': u'\u0644',
    u'\u0645': u'\u0645', u'\ufee1': u'\u0645', u'\ufee2': u'\u0645', u'\ufee3': u'\u0645', u'\ufee4': u'\u0645',
    u'\u0646': u'\u0646', u'\ufee5': u'\u0646', u'\ufee6': u'\u0646', u'\ufee7': u'\u0646', u'\ufee8': u'\u0646',
    u'\u0648': u'\u0648', u'\ufeed': u'\u0648', u'\ufeee': u'\u0648',
    u'\u06cf': u'\u0648',
    u'\u0647': u'\u0647', u'\ufee9': u'\u0647', u'\ufeea': u'\u0647', u'\ufeeb': u'\u0647', u'\ufeec': u'\u0647',
    u'\u06be': u'\u0647',
    u'\u0649': u'\u06cc', u'\ufeef': u'\u06cc', u'\ufef0': u'\u06cc', u'\ufef1': u'\u06cc', u'\ufef2': u'\u06cc',
    u'\ufef3': u'\u06cc', u'\ufef4': u'\u06cc', u'\u06cc': u'\u06cc', u'\u06cd': u'\u06cc', u'\u06ce': u'\u06cc',
    u'\u06d0': u'\u06cc', u'\u06d1': u'\u06cc', u'\u06d2': u'\u06cc', u'\u06d3': u'\u06cc', u'\ufbfc': u'\u06cc',
    u'\ufbfd': u'\u06cc', u'\ufbfe': u'\u06cc', u'\ufbff': u'\u06cc', u'\ufe89': u'\u06cc',
    u'\ufef5': u'\ufefb', u'\ufef6': u'\ufefb', u'\ufef7': u'\ufefb', u'\ufef8': u'\ufefb', u'\ufef9': u'\ufefb',
    u'\ufefa': u'\ufefb', u'\ufefb': u'\ufefb', u'\ufefc': u'\ufefb',
    u'\u0621': u'\u0621', u'\u0654': u'\u0621', u'\ufe80': u'\u0621', u'\ufe8b': u'\u0621', u'\ufe8c': u'\u0621',
    u'\u0623': u'\u0627', u'\u0624': u'\u0648', u'\u0625': u'\u0627', u'\u0626': u'\u06cc', u'\u064a': u'\u06cc',
    # remove_harekat
    u'\u064b': u'', u'\u064c': u'', u'\u064d': u'', u'\u064e': u'', u'\u064f': u'', u'\u0650': u'',
    u'\u0651': u'', u'\u0652': u'', u'\u0653': u'', u'\u0655': u'', u'\u0656': u'', u'\u0657': u'',
    u'\u0658': u'', u'\u0659': u'', u'\u065a': u'', u'\u065b': u'', u'\u065c': u'', u'\u065d': u'', u'\u065e': u'',
    # numbers
    '0': u'\u0660', '1': u'\u0661', '2': u'\u0662', '3': u'\u0663', '4': u'\u0664',
    '5': u'\u0665', '6': u'\u0666', '7': u'\u0667', '8': u'\u0668', '9': u'\u0669',
    u'\u0030': u'\u0660', u'\u0031': u'\u0661', u'\u0032': u'\u0662', u'\u0033': u'\u0663', u'\u0034': u'\u0664',
    u'\u0035': u'\u0665', u'\u0036': u'\u0666', u'\u0037': u'\u0667', u'\u0038': u'\u0668', u'\u0039': u'\u0669',
    u'\u06F0': u'\u0660', u'\u06F1': u'\u0661', u'\u06F2': u'\u0662', u'\u06F3': u'\u0663', u'\u06F4': u'\u0664',
    u'\u06F5': u'\u0665', u'\u06F6': u'\u0666', u'\u06F7': u'\u0667', u'\u06F8': u'\u0668', u'\u06F9': u'\u0669',
    # symbols
    # u'\n':u'',
    u' ': u' ', u'\u200c': u'\u200c', u'\u066b': u'\u066b', u'\u061b': u'\u061b',
    u'\u060c': u'\u060c', u'\u066c': u'\u060c', u'?': u'?', u'\u061f': u'\u061f',
    u'_': u'_', u'\u0640': u'_', u'\u2026': u'\u2026',
    u'\u200d': u'\u200d', u'\u201d': u'\u201d', u'\u201c': u'\u201c',
    u'\u2666': u'\u2666', u'\u2013': u'\u2013',

    # emoji
    u'\U0001f602': u'\U0001f602', u'\U0001f534': u'\U0001f534', u'\U0001f539': u'\U0001f539', u'\u270c': u'\u270c',
    u'\U0001f447': u'\U0001f447', u'\U0001f538': u'\U0001f538', u'\U0001f339': u'\U0001f339', u'\u2764': u'\u2764',
    u'\U0001f448': u'\U0001f448', u'\u2b55': u'\u2b55', u'\U0001f601': u'\U0001f601', u'\U0001f53b': u'\U0001f53b',
    u'\U0001f3fb': u'\U0001f3fb', u'\U0001f1f7': u'\U0001f1f7', u'\U0001f614': u'\U0001f614',
    u'\U0001f64f': u'\U0001f64f',
    u'\U0001f1ee': u'\U0001f1ee', u'\U0001f610': u'\U0001f610', u'\U0001f923': u'\U0001f923',
    u'\U0001f622': u'\U0001f622',
    u'\U0001f4a5': u'\U0001f4a5', u'\U0001f914': u'\U0001f914', u'\U0001f44f': u'\U0001f44f',
    u'\U0001f53a': u'\U0001f53a',
    u'\U0001f38b': u'\U0001f38b', u'\U0001f60a': u'\U0001f60a', u'\U0001f605': u'\U0001f605',
    u'\U0001f62d': u'\U0001f62d',
    u'\U0001f60d': u'\U0001f60d', u'\U0001f341': u'\U0001f341', u'\U0001f5a4': u'\U0001f5a4',
    u'\U0001f604': u'\U0001f604',
    u'\U0001f490': u'\U0001f490', u'\U0001f609': u'\U0001f609', u'\U0001f44a': u'\U0001f44a',
    u'\U0001f44d': u'\U0001f44d',
    u'\U0001f611': u'\U0001f611', u'\u270a': u'\u270a', u'\U0001f499': u'\U0001f499', u'\U0001f60f': u'\U0001f60f',
    u'\U0001f621': u'\U0001f621', u'\U0001f337': u'\U0001f337', u'\U0001f494': u'',

    # English
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i',
    'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r',
    's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z',
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i',
    'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
    'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z',

    ')': '', '"': '', u'\U0001f4fd': '', '/': '', '\xa0': '', '+': '', '!': '', ',': '', ':': '', u'\ufe0f': '',
    '.': '', u'\u2063': '', u'\U0001f384': '', u'\U0001f4a2': '', u'\u2733': '', '\n': '\n', u'\u06d5': u'\u0647'
}
vocabulary_map = {'\u0627': 1, '\u0628': 2, '\u067e': 3, '\u062a': 4, '\u062b': 5, '\u062c': 6, '\u0686': 7,
                  '\u062d': 8, '\u062e': 9, '\u062f': 10, '\u0630': 11, '\u0631': 12, '\u0632': 13, '\u0698': 14,
                  '\u0633': 15, '\u0634': 16, '\u0635': 17, '\u0636': 18, '\u0637': 19, '\u0638': 20, '\u0639': 21,
                  '\u063a': 22, '\u0641': 23, '\u0642': 24, '\u06a9': 25, '\u06af': 26, '\u0644': 27, '\u0645': 28,
                  '\u0646': 29, '\u0648': 30, '\u0647': 31, '\u06cc': 32, '\ufefb': 33, '\u0621': 34, '\U0001f602': 35,
                  '\U0001f534': 36, '\U0001f539': 37, '\u270c': 38, '\U0001f447': 39, '\U0001f538': 40,
                  '\U0001f339': 41, '\u2764': 42, '\U0001f448': 43, '\u2b55': 44, '\U0001f601': 45, '\U0001f53b': 46,
                  '\U0001f3fb': 47, '\U0001f1f7': 48, '\U0001f614': 49, '\U0001f64f': 50, '\U0001f1ee': 51,
                  '\U0001f610': 52, '\U0001f923': 53, '\U0001f622': 54, '\u0660': 55, '\u0661': 56, '\u0662': 57,
                  '\u0663': 58, '\u0664': 59, '\u0665': 60, '\u0666': 61, '\u0667': 62, '\u0668': 63, '\u0669': 64,
                  ' ': 65, '\u200c': 66, '\u066b': 67, '\u061b': 68, '\u060c': 69, '?': 70, '\u061f': 71, 'a': 72,
                  'b': 73, 'c': 74, 'd': 75, 'e': 76, 'f': 77, 'g': 78, 'h': 79, 'i': 80, 'j': 81, 'k': 82, 'l': 83,
                  'm': 84, 'n': 85, 'o': 86, 'p': 87, 'q': 88, 'r': 89, 's': 90, 't': 91, 'u': 92, 'v': 93, 'w': 94,
                  'x': 95, 'y': 96, 'z': 97, '\n': 98, '_': 99, u'\u2026': 100, u'\u200d': 101, u'\u201d': 102,
                  u'\u201c': 103, u'\u2666': 104, u'\u2013': 105, u'\U0001f4a5': 106, u'\U0001f914': 107,
                  u'\U0001f44f': 108, u'\U0001f53a': 109, u'\U0001f38b': 110, u'\U0001f60a': 111, u'\U0001f605': 112,
                  u'\U0001f62d': 113, u'\U0001f60d': 114, u'\U0001f341': 115, u'\U0001f5a4': 116, u'\U0001f604': 117,
                  u'\U0001f490': 118, u'\U0001f609': 119, u'\U0001f44a': 120, u'\U0001f44d': 121, u'\U0001f611': 122,
                  u'\u270a': 123, u'\U0001f499': 124, u'\U0001f60f': 125, u'\U0001f621': 126, u'\U0001f337': 127}
vocabulary_map_reverse = {1: '\u0627', 2: '\u0628', 3: '\u067e', 4: '\u062a', 5: '\u062b', 6: '\u062c', 7: '\u0686',
                          8: '\u062d', 9: '\u062e', 10: '\u062f', 11: '\u0630', 12: '\u0631', 13: '\u0632', 14: '\u0698',
                          15: '\u0633', 16: '\u0634', 17: '\u0635', 18: '\u0636', 19: '\u0637', 20: '\u0638',
                          21: '\u0639', 22: '\u063a', 23: '\u0641', 24: '\u0642', 25: '\u06a9', 26: '\u06af',
                          27: '\u0644', 28: '\u0645', 29: '\u0646', 30: '\u0648', 31: '\u0647', 32: '\u06cc',
                          33: '\ufefb', 34: '\u0621', 35: '\U0001f602', 36: '\U0001f534', 37: '\U0001f539',
                          38: '\u270c', 39: '\U0001f447', 40: '\U0001f538', 41: '\U0001f339', 42: '\u2764',
                          43: '\U0001f448', 44: '\u2b55', 45: '\U0001f601', 46: '\U0001f53b', 47: '\U0001f3fb',
                          48: '\U0001f1f7', 49: '\U0001f614', 50: '\U0001f64f', 51: '\U0001f1ee', 52: '\U0001f610',
                          53: '\U0001f923', 54: '\U0001f622', 55: '\u0660', 56: '\u0661', 57: '\u0662', 58: '\u0663',
                          59: '\u0664', 60: '\u0665', 61: '\u0666', 62: '\u0667', 63: '\u0668', 64: '\u0669', 65: ' ',
                          66: '\u200c', 67: '\u066b', 68: '\u061b', 69: '\u060c', 70: '?', 71: '\u061f', 72: 'a',
                          73: 'b', 74: 'c', 75: 'd', 76: 'e', 77: 'f', 78: 'g', 79: 'h', 80: 'i', 81: 'j', 82: 'k',
                          83: 'l', 84: 'm', 85: 'n', 86: 'o', 87: 'p', 88: 'q', 89: 'r', 90: 's', 91: 't', 92: 'u',
                          93: 'v', 94: 'w', 95: 'x', 96: 'y', 97: 'z', 98: '\n', 99: '_', 100: u'\u2026', 101: u'\u200d',
                          102: u'\u201d', 103: u'\u201c', 104: u'\u2666', 105: u'\u2013', 106: u'\U0001f4a5',
                          107: u'\U0001f914', 108: u'\U0001f44f', 109: u'\U0001f53a', 110: u'\U0001f38b',
                          111: u'\U0001f60a', 112: u'\U0001f605', 113: u'\U0001f62d', 114: u'\U0001f60d',
                          115: u'\U0001f341', 116: u'\U0001f5a4', 117: u'\U0001f604', 118: u'\U0001f490',
                          119: u'\U0001f609', 120: u'\U0001f44a', 121: u'\U0001f44d', 122: u'\U0001f611',
                          123: u'\u270a', 124: u'\U0001f499', 125: u'\U0001f60f', 126: u'\U0001f621',
                          127: u'\U0001f337'}
