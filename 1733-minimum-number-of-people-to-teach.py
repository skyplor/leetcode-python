class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        '''
        We will need an adjacency list of friends.
        If A is friend with B, that means B also is a friend of A. So we can go through the list of friendships and add both relationships into the adjacency list
        We will need a way to know that we have processed the particular friendship.
        The problem lies with needing to return the `minimum` number of users to teach. 

        e.g.
        - A knows language X
        - B knows language Y
        - C knows language X
        - They all are friends with each other

             - B
           /   |
         A     |
           \\  |
             - C

        We can either teach both A & C language Y, or just teach B language X
        The answer is just teach B language X

        If there's common language, we can remove the friendship so we don't process it anymore.
        Next, we get the list of broken friendships (friendships which have no common language)
        Next, we get the most popular language spoken by all of those broken friendships,
            then we can teach those users in the broken friendships who don't speak the popular language and that would be the minimum number of users to teach

        Logic:
        - Initialise a list of users (that are a part of some broken relationship).
        - Go through each friendship in friendships, for each group of users, check if they have common language. If no, add both users into the list of users.
            - To check if they have common language, get the languages that each user knows, then do intersection and check if the intersected set is empty. We can use `&` for intersection

        - Next, go through the list of users with broken relationship, add up the count of each language spoken
        - Find the language that is most spoken
        - Loop through the languages list, if the most spoken language isn't in the element and the user is in the list of broken relationships, add 1 to result
        - Return result

        Worst case analysis:
            L can be up to n (if someone speaks all languages)
            U ≤ 2F (at most 2 users per friendship)
            total_users is given as input

            Overall time complexity: O(F * n + total_users * n) = O((F + total_users) * n)
            In many cases, since friendships involve users, F and total_users are related, so this often simplifies to O(total_users * n).
        
        Space Complexity:

            broken_relationship_users set: O(U) ≤ O(2F)
            language_spoken_count array: O(n)
            Input storage: O(total_users * average_languages_per_user)

        Overall space complexity: O(F + n + total_users * L)
            In worst case where L = n: O(F + total_users * n)
        
        Summary:

            Time: O((F + total_users) * n)
            Space: O(F + total_users * n)

            where F = number of friendships, n = total possible languages, total_users = number of users.
        '''

        broken_relationship_users = set()
        for user_a, user_b in friendships:
            user_a_languages = languages[user_a-1]
            user_b_languages = languages[user_b-1]
            if len(set(user_a_languages) & set(user_b_languages)) == 0:
                broken_relationship_users.add(user_a)
                broken_relationship_users.add(user_b)

        language_spoken_count = [0] * (n+1)
        for user in broken_relationship_users:
            user_languages = languages[user-1]
            for language in user_languages:
                language_spoken_count[language] += 1

        most_spoken_language = 0
        max_count = 0
        for language, count in enumerate(language_spoken_count):
            if count > max_count:
                most_spoken_language = language
                max_count = count

        res = 0
        for idx, languages_spoken in enumerate(languages):
            user = idx + 1
            if user in broken_relationship_users and most_spoken_language not in languages_spoken:
                res += 1

        return res


sol = Solution()
n = 2
languages = [[1], [2], [1, 2]]
friendships = [[1, 2], [1, 3], [2, 3]]
print(f'output: {sol.minimumTeachings(n, languages, friendships)}, expected: 1')

n = 3
languages = [[2], [1, 3], [1, 2], [3]]
friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]
print(f'output: {sol.minimumTeachings(n, languages, friendships)}, expected: 2')
