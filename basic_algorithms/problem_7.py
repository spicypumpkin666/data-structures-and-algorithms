# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)

    def insert(self, request_path, handler):
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
        sub_path_list = request_path.split("/")

        if len(sub_path_list) <= 1:
            return

        node = self.root
        for sub_path in sub_path_list[1:]:
            if sub_path in node.sub_path_dict:
                node = node.sub_path_dict[sub_path]
            else:
                child_route = RouteTrieNode()
                node.sub_path_dict[sub_path] = child_route
                node = child_route

        node.handler = handler

    def find(self, request_path):
    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
        if request_path[-1] == "/":
            request_path = request_path[:-1]

        sub_path_list = request_path.split("/")

        node = self.root

        if len(sub_path_list) <= 1:
            return node.handler

        for sub_path in sub_path_list[1:]:
            if sub_path in node.sub_path_dict:
                node = node.sub_path_dict[sub_path]
            else:
                return None
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
    #Initialize the node with children as before, plus a handler
        self.handler = handler
        self.sub_path_dict = dict()

    def insert(self, sub_path, handler=None):
    #Insert the node as before
        route_trie_node = RouteTrieNode(handler)
        self.sub_path_dict[sub_path] = route_trie_node

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, route_handler=None, not_found=None):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler=route_handler)
        self.not_found = not_found

    def add_handler(self, request_path, handler):
    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
        path = self.split_path(request_path)
        self.route_trie.insert(path, handler)

    def lookup(self, request_path):
    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        path = self.split_path(request_path)
        handler = self.route_trie.find(path)
        if handler is None:
            return self.not_found
        return handler

    def split_path(self, request_path):
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
        return request_path.split("/")

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one