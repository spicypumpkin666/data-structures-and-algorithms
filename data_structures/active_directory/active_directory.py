class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    groups = group.get_groups()

    if user == group.get_name():
        return True
    if user in group.get_users():
        return True
    for grp in groups:
        return is_user_in_group(user, grp)
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(f"child is in group return True: {is_user_in_group(sub_child_user, parent)}")

# Test Case 2
print(f"child is not in group / wrong input returns false: {is_user_in_group('blah', parent)}")

# Test Case 3
print(f"none returns false: {is_user_in_group('', parent)}")
