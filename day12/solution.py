class Path:
    def __init__(self, path=None):
        if path is None:
            self.vertices = []
        else:
            self.vertices = path.vertices[:]

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex):
        if self.is_complete() or (vertex.islower() and vertex in self.vertices):
            return False
        self.vertices.append(vertex)
        return True

    def get_last_vertex(self):
        return None if len(self.vertices) == 0 else self.vertices[len(self.vertices) - 1]

    def is_complete(self):
        return 'end' in self.vertices


class PathPartTwo(Path):
    def __init__(self, path=None):
        super().__init__(path)
        if path is None:
            self.small_cave_twice = (False, None)
        else:
            self.small_cave_twice = path.small_cave_twice

    def add_vertex(self, vertex):
        if self.is_complete():
            return False

        if vertex in ['start', 'end']:
            if vertex not in self.vertices:
                self.vertices.append(vertex)
                return True
            return False

        if self.small_cave_twice[0] is True:
            if vertex == self.small_cave_twice[1] or (vertex.islower() and vertex in self.vertices):
                return False

        self.vertices.append(vertex)

        if self.small_cave_twice[0] is False and vertex.islower():
            if len([v for v in self.vertices if v == vertex]) > 1:
                self.small_cave_twice = (True, vertex)

        return True


def get_adjacent_vertices(edges, vertex):
    return [v for e in edges for v in e if vertex in e and v != vertex]


def get_vertex_to_adjacent_vertices(edges):
    return {v: get_adjacent_vertices(edges, v) for e in edges for v in e}


def filter_completed_paths(paths):
    return [path for path in paths if path.is_complete()]


def find_paths(vertex_to_adjacent_vertices, paths, path_class=Path):
    for path in paths[:]:
        if path.is_complete():
            continue
        last_vertex = path.get_last_vertex()
        adjacent = vertex_to_adjacent_vertices[last_vertex]
        new_paths = []
        for a in adjacent:
            new_path = path_class(path)
            if new_path.add_vertex(a):
                new_paths.append(new_path)
        paths += find_paths(vertex_to_adjacent_vertices, new_paths, path_class=path_class)

    return filter_completed_paths(paths)


def part_one(edges):
    vertex_to_adjacent_vertices = get_vertex_to_adjacent_vertices(edges)
    path = Path()
    path.add_vertex('start')
    return len(find_paths(vertex_to_adjacent_vertices, [path]))


def part_two(edges):
    vertex_to_adjacent_vertices = get_vertex_to_adjacent_vertices(edges)
    path = PathPartTwo()
    path.add_vertex('start')
    return len(find_paths(vertex_to_adjacent_vertices, [path], PathPartTwo))


with open('input', 'r') as infile:
    edges = [tuple(line.strip().split('-')) for line in infile.readlines()]

print(part_one(edges))
print(part_two(edges))
