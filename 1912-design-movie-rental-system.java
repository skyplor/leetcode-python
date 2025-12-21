import java.util.*;

class MovieRentingSystem {
    private Map<Integer, List<int[]>> movies = new HashMap<>();
    private Map<String, Integer> prices = new HashMap<>();
    private Set<String> rented = new HashSet<>();

    private String getMovieShopKey(int shop, int movie) {
        return movie + ":" + shop;
    }

    public MovieRentingSystem(int n, int[][] entries) {
        for (int i = 0; i < entries.length; i++) {
            int shop = entries[i][0];
            int movie = entries[i][1];
            int price = entries[i][2];
            int[] priceShop = { price, shop };
            if (!movies.containsKey(movie)) {
                movies.put(movie, new ArrayList<>());
            }
            movies.get(movie).add(priceShop);
            String key = getMovieShopKey(shop, movie);
            prices.put(key, price);
        }

        for (List<int[]> priceShopList : movies.values()) {
            Collections.sort(priceShopList, (a, b) -> {
                if (a[0] != b[0])
                    return Integer.compare(a[0], b[0]);

                return Integer.compare(a[1], b[1]);
            });
        }
    }

    public List<Integer> search(int movie) {
        List<int[]> priceShopList = movies.get(movie);
        if (priceShopList == null)
            return new ArrayList<>();

        List<Integer> result = new ArrayList<>();
        for (int[] priceShop : priceShopList) {
            String key = getMovieShopKey(priceShop[1], movie);
            if (!rented.contains(key)) {
                result.add(priceShop[1]);
                if (result.size() == 5) {
                    break;
                }
            }
        }
        return result;
    }

    public void rent(int shop, int movie) {
        rented.add(getMovieShopKey(shop, movie));
    }

    public void drop(int shop, int movie) {
        String key = getMovieShopKey(shop, movie);
        if (rented.contains(key)) {
            rented.remove(key);
        }
    }

    public List<List<Integer>> report() {
        List<List<Integer>> result = new ArrayList<>();
        List<int[]> rentedList = new ArrayList<>();

        for (String rentedMovie : rented) {
            String[] splitted = rentedMovie.split(":");
            int movie = Integer.parseInt(splitted[0]);
            int shop = Integer.parseInt(splitted[1]);

            int price = prices.get(rentedMovie);
            rentedList.add(new int[] { price, shop, movie });

        }

        Collections.sort(rentedList, (a, b) -> {
            if (a[0] != b[0])
                return Integer.compare(a[0], b[0]);
            if (a[1] != b[1])
                return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });

        for (int[] item : rentedList) {
            int shop = item[1];
            int movie = item[2];

            result.add(Arrays.asList(shop, movie));
            if (result.size() == 5) {
                break;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[][] entries = { { 0, 1, 5 }, { 0, 2, 6 }, { 0, 3, 7 }, { 1, 1, 4 }, { 1, 2, 7 }, { 2, 1, 5 } };
        MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, entries);
        System.out.println("output: " + movieRentingSystem.search(1) + ", expected: [1, 0, 2]"); // return [1, 0, 2],
                                                                                                 // Movies of ID 1 are
                                                                                                 // unrented at shops 1,
                                                                                                 // 0, and 2. Shop 1 is
                                                                                                 // cheapest; shop 0 and
                                                                                                 // 2 are the same
                                                                                                 // price, so order by
                                                                                                 // shop number.
        movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
        movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
        System.out.println("output: " + movieRentingSystem.report() + ", expected: [[0, 1], [1, 2]]"); // return [[0,
                                                                                                       // 1], [1, 2]].
                                                                                                       // Movie 1 from
                                                                                                       // shop 0 is
                                                                                                       // cheapest,
                                                                                                       // followed by
                                                                                                       // movie 2 from
                                                                                                       // shop 1.
        movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
        System.out.println("output: " + movieRentingSystem.search(2) + ", expected: [0, 1]"); // return [0, 1]. Movies
                                                                                              // of ID 2 are unrented at
                                                                                              // shops 0 and 1. Shop 0
                                                                                              // is cheapest, followed
                                                                                              // by shop 1.
    }
}
