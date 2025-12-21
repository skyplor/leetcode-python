import java.util.*;

class CountMentionsPerUser {

    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        events.sort((a, b) -> {
            if (Integer.parseInt(a.get(1)) == Integer.parseInt(b.get(1))) {
                return b.get(0).compareTo(a.get(0));
            }
            return Integer.parseInt(a.get(1)) - Integer.parseInt(b.get(1));
        });

        int[] mentions = new int[numberOfUsers];
        int ONLINE_TIME_OFFSET = 60;
        int[] usersOnlineTime = new int[numberOfUsers];
        int allMentioned = 0;

        for (List<String> event : events) {
            String type = event.get(0), users = event.get(2);
            int time = Integer.parseInt(event.get(1));
            if (type.equals("MESSAGE")) {
                if (users.equals("HERE")) {
                    for (int user = 0; user < numberOfUsers; user++) {
                        int onlineTime = usersOnlineTime[user];
                        if (time >= onlineTime) {
                            mentions[user]++;
                        }
                    }
                    continue;
                }
                if (users.equals("ALL")) {
                    allMentioned++;
                    continue;
                }
                String[] userList = users.split(" ");
                for (String user : userList) {
                    int userId = Integer.parseInt(user.substring(2));
                    mentions[userId]++;
                }
                continue;
            }
            usersOnlineTime[Integer.parseInt(users)] = time + ONLINE_TIME_OFFSET;
        }

        for (int user = 0; user < numberOfUsers; user++) {
            mentions[user] += allMentioned;
        }

        return mentions;
    }

    public static void main(String[] args) {
        CountMentionsPerUser sol = new CountMentionsPerUser();
        System.out.println("Output: " + Arrays.toString(sol.countMentions(2, Arrays.asList(Arrays.asList("MESSAGE","10","id1 id0"),Arrays.asList("OFFLINE","11","0"),Arrays.asList("MESSAGE","71","HERE")))) + ", expected: [2, 2]");
        System.out.println("Output: " + Arrays.toString(sol.countMentions(2, Arrays.asList(Arrays.asList("MESSAGE","10","id1 id0"),Arrays.asList("OFFLINE","11","0"),Arrays.asList("MESSAGE","12","ALL")))) + ", expected: [2, 2]");
        System.out.println("Output: " + Arrays.toString(sol.countMentions(2, Arrays.asList(Arrays.asList("OFFLINE","10","0"),Arrays.asList("MESSAGE","12","HERE")))) + ", expected: [0, 1]");
    }
}