class Util:

    def mid(string, start, length):
        return string[start:start+length]

    def left(string, length):
        return string[:length]

    def containsAny(string, *characters):
        for char in characters:
            if char in string:
                return True
        return False

    # def mid(string, pos, length):
    #     if string is None:
    #         return None

    #     if pos < 0 or pos > len(string):
    #         return ""

    #     if pos < 0:
    #         pos = 0

    #     if pos + length > len(string):
    #         return string[pos:]

    #     return string[pos:pos+length]