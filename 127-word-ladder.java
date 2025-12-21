import java.util.*;

class WordLadderSolution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> visited = new HashSet<>();
        Deque<String> queue = new ArrayDeque<>();
        Map<String, List<String>> hashMap = new HashMap<>();

        boolean containsEndWord = false;
        for (String word : wordList) {
            addWord(word, hashMap, queue, false);
            if (word.equals(endWord)) {
                containsEndWord = true;
            }
        }
        if (!containsEndWord) {
            return 0;
        }

        // Add beginWord
        addWord(beginWord, hashMap, queue, true);

        int counter = 1;
        while (!queue.isEmpty()) {
            counter++;
            String curString;
            for (int i = 0; i < queue.size(); i++) {
                curString = queue.pollFirst();
                visited.add(curString);
                if (curString.equals(endWord)) {
                    return counter;
                }

                for (int j = 0; j < curString.length(); j++) {
                    String key = getKey(j, curString);
                    List<String> neighbours = hashMap.get(key);
                    for (String n : neighbours) {
                        if (!visited.contains(n)) {
                            queue.add(n);
                        }
                    }
                }
            }
        }

        return 0;
    }

    public void addWord(String word, Map<String, List<String>> hashMap, Deque<String> queue, boolean addQueue) {
        for (int i = 0; i < word.length(); i++) {
            String key = getKey(i, word);
            if (!hashMap.containsKey(key)) {
                hashMap.put(key, new ArrayList<>());
            }
            hashMap.get(key).add(word);
            if (addQueue) {
                queue.addAll(hashMap.get(key));
            }
        }
    }

    public String getKey(int i, String word) {
        StringBuilder stringBuilder = new StringBuilder();
        String asterisk = "*";
        stringBuilder.append(word.substring(0, i));
        stringBuilder.append(asterisk);
        stringBuilder.append(word.substring(i + 1));
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        WordLadderSolution solution = new WordLadderSolution();
        String beginWord = "hit";
        String endWord = "cog";
        List<String> wordList = new ArrayList<>(Arrays.asList("hot", "dot", "dog", "lot", "log", "cog"));
        int result = solution.ladderLength(beginWord, endWord, wordList);
        System.out.println("result: " + result);
    }
}