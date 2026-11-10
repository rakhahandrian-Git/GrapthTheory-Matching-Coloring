def welsh_powell_timetabling(graph):

    # Step 1: Calculate the degree (number of conflicts) for each course
    degrees = {node: len(neighbors) for node, neighbors in graph.items()}
    
    # Step 2: Sort courses in descending order of their degrees
    sorted_nodes = sorted(degrees, key=degrees.get, reverse=True)
    
    coloring = {}
    current_color = 1
    
    # Step 3: Sequentially assign colors (timeslots)
    while len(coloring) < len(graph):
        uncolored_in_pass = []
        
        for node in sorted_nodes:
            if node not in coloring:
                # Check if any neighbor already has the current color
                conflict = False
                for neighbor in graph[node]:
                    if neighbor in coloring and coloring[neighbor] == current_color:
                        conflict = True
                        break
                
                if not conflict:
                    coloring[node] = current_color
                else:
                    uncolored_in_pass.append(node)
                    
        current_color += 1
        
    return coloring

# --- Example Execution Script ---
if __name__ == "__main__":
    # Sample conflict graph (Courses and their conflicting peers)
    sample_graph = {
        'Math': ['Physics', 'Chemistry'],
        'Physics': ['Math', 'Chemistry', 'Biology'],
        'Chemistry': ['Math', 'Physics', 'Computer Science'],
        'Biology': ['Physics', 'Computer Science'],
        'Computer Science': ['Chemistry', 'Biology']
    }
    
    schedule = welsh_powell_timetabling(sample_graph)
    print("Assigned Exam Timeslots (Colors):")
    for course, timeslot in schedule.items():
        print(f"  {course} -> Timeslot {timeslot}")
