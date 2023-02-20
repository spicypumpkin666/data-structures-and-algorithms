# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
         self.root = RouteTrieNode(handler=handler)

    def insert(self, request_path, handler):
        if len(request_path) <= 1:
            return

        node = self.root
        for sub_path in request_path[1:]:
            if sub_path in node.sub_path_dict:
                node = node.sub_path_dict[sub_path]
            else:
                child_route = RouteTrieNode()
                node.sub_path_dict[sub_path] = child_route
                node = child_route

        node.handler = handler

    def find(self, request_path):
        if request_path[-1] == "/":
            request_path = request_path[:-1]

        node = self.root

        if len(request_path) <= 1:
            return node.handler

        for sub_path in request_path[1:]:
            if sub_path in node.sub_path_dict:
                node = node.sub_path_dict[sub_path]
            else:
                return None
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.sub_path_dict = dict()

    def insert(self, sub_path, handler=None):
        route_trie_node = RouteTrieNode(handler)
        self.sub_path_dict[sub_path] = route_trie_node

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, route_handler=None, not_found=None):
        self.route_trie = RouteTrie(handler=route_handler)
        self.not_found = not_found

    def add_handler(self, request_path, handler):
        path = self.split_path(request_path)
        self.route_trie.insert(path, handler)

    def lookup(self, request_path):
        if request_path[-1] == '/':
            request_path = request_path[:len(request_path) - 1]
        path = self.split_path(request_path)
        handler = self.route_trie.find(path)
        if handler is None:
            return self.not_found
        return handler

    def split_path(self, request_path):
        return request_path.split("/")

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me", "me handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one