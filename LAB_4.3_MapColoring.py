def is_safe(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def forward_check(assignment, domains, region, color, neighbors):
    new_domains = {r: set(domains[r]) for r in domains}
    for neighbor in neighbors[region]:
        if color in new_domains[neighbor]:
            new_domains[neighbor].remove(color)
    return new_domains

def backtrack(assignment, domains, neighbors, colors):
    if len(assignment) == len(domains):
        return assignment
    region = next(r for r in domains if r not in assignment)
    for color in list(domains[region]):
        if is_safe(region, color, assignment, neighbors):
            assignment[region] = color
            new_domains = forward_check(assignment, domains, region, color, neighbors)
            result = backtrack(assignment, new_domains, neighbors, colors)
            if result:
                return result
            del assignment[region]
    return None
# Example: Australia map
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []
}
colors = ['Red', 'Green', 'Blue']
domains = {region: set(colors) for region in neighbors}
solution = backtrack({}, domains, neighbors, colors)
print("Map coloring solution:", solution)