from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        '''
        We preprocess by creating a hashmap of keys and a list of indices. For each wordlist, we have a key that is the exact word, a key that is all lowercase, and a key that had the vowels replaced with '*'
            e.g. KiTe -> keys: KiTe, kite, k*t*
        Next, we have multiple checks based on the precedence rules and return as soon as we found a match
            1. exact match (case-sensitive): Search the hashmap for the exact key
            2. case-insensitive match (return first match based on the casing of the query string): Search the hashmap for the lowercase key and get the first idx
            3. vowel error match: Search the hashmap for the key that had the vowels replaced with '*' and get the first idx
            4. Lastly, return empty string if no match found
        '''
        def parse_to_regex_key(s: str) -> str:
            replaced_key_arr = []
            for c in s:
                if c.lower() in vowels:
                    replaced_key_arr.append('*')
                else:
                    replaced_key_arr.append(c.lower())
            return "".join(replaced_key_arr)

        words_set, case_insensitive, vowels_insensitive = set(wordlist), {}, {}

        vowels = {'a', 'e', 'i', 'o', 'u'}
        for idx, word in enumerate(wordlist):
            if word.lower() not in case_insensitive:
                case_insensitive[word.lower()] = word

            regex_key = parse_to_regex_key(word)
            if regex_key not in vowels_insensitive:
                vowels_insensitive[regex_key] = word

        result = []
        for query in queries:
            if query in words_set:
                result.append(query)
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            else:
                regex_key = parse_to_regex_key(query)
                if regex_key in vowels_insensitive:
                    result.append(vowels_insensitive[regex_key])
                else:
                    result.append('')

        return result


sol = Solution()
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE",
           "Hear", "hear", "keti", "keet", "keto"]
print(
    f'output: {sol.spellchecker(wordlist, queries)}, expected: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]')
# wordlist = ["yellow"]
# queries = ["YellOw"]
# print(f'output: {sol.spellchecker(wordlist, queries)}, expected: ["yellow"]')
# wordlist = ["Yellow"]
# queries = ["yellow"]
# print(f'output: {sol.spellchecker(wordlist, queries)}, expected: ["Yellow"]')
wordlist = ["YellOw"]
queries = ["yollow"]
print(f'output: {sol.spellchecker(wordlist, queries)}, expected: ["YellOw"]')
