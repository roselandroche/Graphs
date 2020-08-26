import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # maps IDs to user objects
        self.users = {}
        # adjacency list
        # maps user IDs to a list of other users who are their friends
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')
        # Create friendships
        # generate all possible friendships
        # avoid duplicate friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == user_id_2 cannot happen
                # if friendship between user_id and user_id_2 already exists
                    # don't add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) )
        # randomly select x friendships
        # the formula for x is num_users * avg_friendships // 2
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create an empty dict to track visited vertices
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # get all friend ids and add to visited as keys
        # do bfs on friend ids to get shortest path and add as value
        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            path = queue.dequeue()
            current_friend = path[-1]
            # if current friend is not in visited:
            if current_friend not in visited:
                # add current friend : (path to friend)
                visited[current_friend] = path
                # loop through friends of current friend
                for friend in self.friendships[current_friend]:
                    if friend not in visited:
                    # if friend not in visited:
                        new_path = list(path)
                        new_path.append(friend)
                        queue.enqueue(new_path)
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


'''
U
Input is user_id
Output
    dict containing
        every user in user_id's extended network
        shortest friendship path between each
P
BFT guarantees shortest path is the first path found
Starting at user_id
    traverse through connected ids
    save connected ids to visited dict as key
        length of connection as value
'''