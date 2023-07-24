from functools import reduce


def create_simple_string(string_words, width):

    if len(string_words) == 1:
        return string_words[0] + (' ' * (width - len(string_words[0])))
    
    else:
        sum_of_words_lengthes = reduce(lambda x, y: x + len(y),
                                       string_words,
                                       0
                                       )
        num_of_spaces = width - sum_of_words_lengthes
        num_of_gaps = len(string_words) - 1
        if num_of_spaces % num_of_gaps == 0:
            return (' ' * (num_of_spaces // num_of_gaps)).join(string_words)
        else:
            extra_spaces = num_of_spaces % num_of_gaps
            result = string_words[0]
            for i in range(1, len(string_words)):
                result = (result +
                          (' ' * (num_of_spaces // num_of_gaps)) +
                          (' ' if i <= extra_spaces else '') +
                          string_words[i])
            return result
        

         


print(create_simple_string(['as','a','a','sddf'], 22),"end",sep='')

